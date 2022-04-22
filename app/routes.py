from flask import Blueprint

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
