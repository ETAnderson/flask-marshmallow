from flask import Flask, request, jsonify, make_response
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from SQLALCHEMY_DATABASE_URI import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/users', methods=['GET'])
    def index():
        all_users = User.query.all()
        user_schema = UserSchema(many=True)
        users = user_schema.dump(all_users)
        return make_response(jsonify({"users": users}), 200)

    @app.route('/users/<id>', methods=['GET'])
    def get_user_by_id(id):
        get_user = User.query.get(id)
        user_schema = UserSchema()
        user = user_schema.dump(get_user)
        return make_response(jsonify({"user": user}), 200)

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user_schema = UserSchema()
        user = user_schema.load(data)
        result = user_schema.dump(user.create())
        return make_response(jsonify({'user': result}), 201)

    @app.route('/users/<id>', methods=['PUT'])
    def update_user_by_id(id):
        data = request.get_json()
        get_user = User.query.get(id)

        if data.get('name'):
            get_user.name = data['name']
        if data.get('password'):
            get_user.password = data['password']

        db.session.add(get_user)
        db.session.commit()
        user_schema = UserSchema(only=['id', 'name', 'password'])
        user = user_schema.dump(get_user)
        return make_response(jsonify({"user": user}), 200)

    @app.route('/users/<id>', methods=['DELETE'])
    def delete_user_by_id(id):
        get_user = User.query.get(id)
        db.session.delete(get_user)
        db.session.commit()
        return make_response("", 204)

    return app


app = create_app()


class User(db.Model):
    # defines table, sets data structure
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(50))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Product %d>' % self.id


class UserSchema(SQLAlchemyAutoSchema):
    # defines input format with validation
    class Meta(SQLAlchemyAutoSchema.Meta):
        load_instance = True
        include_relationships = True
        model = User
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    password = fields.String(required=True)


if __name__ == "__main__":
    app.run(debug=True)
