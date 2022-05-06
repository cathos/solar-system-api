import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_planets(app):
    Earth = Planet(id=3, order_from_sun= 3, name="Earth", description= "something about earth", gravity= "9.81 m/s2")
    Venus = Planet(id=2, order_from_sun= 2, name="Venus", description= "Very hot planet with a dense atmosphere", gravity= "8.87 m/s2")
    

    db.session.add(Earth)
    db.session.add(Venus)
    db.session.commit()
