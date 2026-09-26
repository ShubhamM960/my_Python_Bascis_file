from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

#map the web URLs to pyton fuctions
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



# HTTP GET - for RANDOM Cafe Record
@app.route("/random", methods = ['GET'] )
def get_cafe_name():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not cafes:
        return jsonify(error={"Not Found": "No cafes in database."}), 404

    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict()), 200
# =============ALTERNATIVE WAY TO GET A RANDOM CAFE========

#  total = db.session.execute(
#         db.select(func.count()).select_from(Cafe)
#     ).scalar_one()
#     if total == 0:
#         return jsonify(error={"Not Found": "No cafes in database."}), 404
#     offset = random.randint(0, total - 1)
#     random_cafe = db.session.execute(
#         db.select(Cafe).offset(offset).limit(1)
#     ).scalars().first()
#     return jsonify(cafe=random_cafe.to_dict()), 200
 #================================================================

#HTTP GET - for all cafe record
@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200


def _to_bool(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"true", "1", "yes", "y"}

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.get_json(silent=True) or request.form 
    
    required_fields = [
        "name", "map_url", "img_url", "location", "seats",
        "has_toilet", "has_wifi", "has_sockets", "can_take_calls"
    ]
    missing = [f for f in required_fields if data.get(f) is None]
    if missing:
        return jsonify(error={"Missing fields": missing}), 400

    new_cafe = Cafe(
        name=data.get("name"),
        map_url=data.get("map_url"),
        img_url=data.get("img_url"),
        location=data.get("location"),
        seats=data.get("seats"),
        has_toilet=_to_bool(data.get("has_toilet")),
        has_wifi=_to_bool(data.get("has_wifi")),
        has_sockets=_to_bool(data.get("has_sockets")),
        can_take_calls=_to_bool(data.get("can_take_calls")),
        coffee_price=data.get("coffee_price")
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."}), 201


### HTTP PUT/PATCH - Update Record , HTTP Patch request  --> params = {"new_price" : "5.32"}
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Bad Request": "Please provide new_price as a query parameter."}), 400

    try:
        cafe = db.session.execute(
            db.select(Cafe).where(Cafe.id == cafe_id)
        ).scalar_one_or_none()
        cafe.coffee_price = new_price
        db.session.commit()
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found."}), 404

    return jsonify(response={"success": "Successfully updated the price."}), 200

# HTTP DELETE - Delete Record, HTTP Delete request  --> params = {"api-key" : "TopSecretAPIKey"}
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    
    if request.args.get('api-key') == 'TopSecretAPIKey':
        try : 
            cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)
            ).scalar_one_or_none()
        except AttributeError:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        else :
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
    else :
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)

