from flask import request_finished
from app import db
import pytest
from app.models.cat import Cat

from app import create_app

@pytest.fixture
def app():
    app = create_app({"TESTING:True"})