from app import db


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_from_sun = db.Column(db.Integer)
    name = db.Column(db.String)
    description = db.Column(db.String)
    gravity = db.Column(db.String)
    moons = db.relationship("Moon", back_populates = "planet")
