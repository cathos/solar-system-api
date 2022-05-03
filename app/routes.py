from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

# class Planet:
#     def __init__(self, id, name, description, gravity):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.gravity = gravity

# planets = [
#     Planet(1, 'Mercury', 'The closest planet to the sun! REALLY HOT!', '3.7 m/s2'),
#     Planet(2, 'Venus',  'Another hot planet! Actually hotter than Mercury!', '8.87 m/s2'),
#     Planet(3, 'Earth', 'Third Planet from the Sun. Maybe a little special. Much colder than the first two.', '9.8 m/s2')
# ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Planet {planet_id} invalid"}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response({"message":f"Planet {planet_id} not found"}, 404))

    return planet

@planets_bp.route("/<planet_id>", methods = ["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "gravity": planet.gravity
    }

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    # planets_result = []
    # for planet in planets:
    #     planets_result.append(dict(
    #         id = planet.id,
    #         name = planet.name,
    #         description = planet.description,
    #         gravity = planet.gravity
    #     ))
    # return jsonify(planets_result)
    planets = Planet.query.all()
    planets_response = []
    for planet in planets: 
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "gravity": planet.gravity
        })
    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"], gravity=request_body["gravity"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods=["PATCH"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()
    request_body_keys = request_body.keys()

    if "name" in request_body_keys:
        planet.name = request_body["name"]
    if "description" in request_body_keys:
        planet.description = request_body["description"]
    if "gravity" in request_body_keys:
        planet.gravity = request_body["gravity"]

    # planet.name = request_body["name"]
    # planet.description = request_body["description"]
    # planet.gravity = request_body["gravity"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated", 200)

# @planets_bp.route("/<planet_id>", methods = ["GET"])
# def get_planet(planet_id):
#     try: 
#         planet_id = int(planet_id)
#     except:
#         abort(make_response(jsonify(dict(details=f"planet id {planet_id} invalid")), 400))
        
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "gravity": planet.gravity
                
#             }
#     abort(make_response(jsonify(dict(details=f"planet id {planet_id} not found")), 404))
