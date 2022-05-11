from app import db
from app.models.planet import Planet
from app.models.moon import Moon
from flask import Blueprint, jsonify, make_response, request, abort


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/teapot", methods=["GET", "POST"])
def handle_teapot():
    return make_response("I'm a teapot!", 418)

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
        "order_from_sun": planet.order_from_sun,
        "name": planet.name,
        "description": planet.description,
        "gravity": planet.gravity
    }

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    order_from_sun_query = request.args.get("order_from_sun")
    if name_query:
        planets = Planet.query.filter_by(name=name_query)
    elif description_query:
        planets = Planet.query.filter(Planet.description.ilike("%" + description_query + "%"))
    elif order_from_sun_query:
        planets = Planet.query.filter_by(order_from_sun =order_from_sun_query)
    else:
        planets = Planet.query.all()
    
    planets_response = []
    for planet in planets: 
        planets_response.append({
            "id": planet.id,
            "order_from_sun": planet.order_from_sun,
            "name": planet.name,
            "description": planet.description,
            "gravity": planet.gravity
        })
    return jsonify(planets_response)

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"], 
        order_from_sun=request_body["order_from_sun"], 
        description=request_body["description"], 
        gravity=request_body["gravity"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@planets_bp.route("/<planet_id>/moons", methods=["POST"])
def add_moon(planet_id):
    moons_planet = validate_planet(planet_id)
    request_body = request.get_json()
    # request_body_keys = request_body.keys()
    if not request_body:
        return make_response(f"Invalid request body", 400)
    else:
        new_moon = Moon(
            name = request_body["name"],
            description = request_body["description"],
            planet_id = planet_id)

        # if "name" in request_body_keys:
        #     moon.name = request_body["name"]
        # if "description" in request_body_keys:
        #     moon.description = request_body["description"]

        db.session.add(new_moon)
        db.session.commit()

        return make_response(f"Moon #{new_moon.id} successfully updated", 200)



@planets_bp.route("/<planet_id>", methods=["PUT"])
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
    if "order_from_sun" in request_body_keys:
        planet.order_from_sun = request_body["order_from_sun"]

    db.session.commit()
    return make_response(f"Planet #{planet.id} successfully updated", 200)

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet #{planet.id} successfully deleted", 200)

