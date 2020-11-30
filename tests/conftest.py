import pytest

from user import User, create_app
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture(scope='module')
def new_user():
    user = User('Eric Anderson', 'testpass')
    return user


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    testing_client = app.test_client()
    ctx = app.app_context()

    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db = SQLAlchemy()
    db.drop_all(app=create_app())

    user1 = User(name='Eric Anderson', password='testpass2')
    user2 = User(name='Rochelle Anderson', password='Rochellepass')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db
