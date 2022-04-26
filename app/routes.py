from flask import Blueprint, jsonify, make_response, abort


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

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_result = []
    for planet in planets:
        planets_result.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            gravity = planet.gravity
        ))
    return jsonify(planets_result)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_planet(planet_id):
    try: 
        planet_id = int(planet_id)
    except:
        abort(make_response(jsonify(dict(details=f"planet id {planet_id} invalid")), 400))
        
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "gravity": planet.gravity
                
            }
    abort(make_response(jsonify(dict(details=f"planet id {planet_id} not found")), 404))
