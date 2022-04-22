from flask import Blueprint

<<<<<<< HEAD
planets_bp = Blueprint("planets", __name__, url_prefix)="planets")
=======
class Planet:
    def __init__(self, id, name, description, gravity):
        self.id = id
        self.name = name
        self.description = description
        self.gravity = gravity

planets = [
    Planet(1, 'Mercury', 'The closest planet to the sun! REALLY HOT!', '3.7 m/s2'),
    Planet(2, 'Venus',  'Another hot planet', '8.87 m/s2'),
    Planet(3, 'Earth', 'Third Planet from the Sun. Maybe a little special', '9.8 m/s2')
]
>>>>>>> 24657bcde3dd9f27d8a371dc5cd46f5ce7898273
