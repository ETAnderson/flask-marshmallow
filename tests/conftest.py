import pytest

from user import User, create_app, db
# from flask_sqlalchemy import SQLAlchemy


def init_database():
    db.create_all()

    user1 = User(name='Eric Anderson', password='testpass2')
    user2 = User(name='Rochelle Anderson', password='Rochellepass')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()


@pytest.fixture(scope='module')
def new_user():
    user = User('Eric Anderson', 'testpass')
    return user


@pytest.fixture(scope='module')
def test_client():
    app = create_app()

    with app.app_context() as ctx:
        ctx.push()

        init_database()

        yield app.test_client()

        db.session.remove()
        db.drop_all()

        ctx.pop()
