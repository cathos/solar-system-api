# # from flasky:

# from flask import request_finished
# from app import db
# import pytest
# from app.models.cat import Cat 

# from app import create_app

# @pytest.fixture
# def app():
#     app = create_app({"TESTING": True})

#     @request_finished.connect_via(app)
#     def expire_session(sender,response, **extra):
#         db.session.remove()
    
#     with app.app_context():
#         db.create_all() 
#         yield app
    
#     with app.app_context():
#         db.drop_all()

# @pytest.fixture
# def client(app):
#     return app.test_client()

# @pytest.fixture
# def two_cats(app):
#     fluffy = Cat(id=1, name="fluffy", color="grey", personality="likes to cuddle")
#     sleepy = Cat(id=2, name="sleepy", color="orange", personality="likes to take naps")

#     db.session.add(fluffy)
#     db.session.add(sleepy)
#     db.session.commit()

# * * *

# # from hello-books

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
