from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///distilledsch.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Car(db.Model):
    __tablename__ = 'car'
    make = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=True)
    chassis_id = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    last_updated = db.Column(
        db.DateTime, default=datetime.now(), nullable=False)
    price = db.Column(db.Integer, nullable=True)


class CarSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('make', 'model', 'year', 'id', 'last_updated', 'price')


car_schema = CarSchema()
cars_schema = CarSchema(many=True)


# return all cars in database
@app.route("/car/", methods=["GET"])
def all_cars():
    all_cars = Car.query.all()
    result = cars_schema.dump(all_cars)
    return jsonify(result.data)


# return cars with specific id
@app.route("/car/<id>", methods=["GET"])
def car_id(id):
    car = Car.query.filter(Car.id == id).first()
    return car_schema.jsonify(car)


#  return the avg price of cars with given criteria
@app.route("/avgprice", methods=["POST"])
def add_user():
    data = request.get_json()
    make = data['make']
    model = data['model']
    year = data['year']
    result = Car.query.filter(Car.make == make, Car.model ==
                              model, Car.year == year).value(func.avg(Car.price))
    return jsonify(result)


# add car to the database
@app.route("/car", methods=["POST"])
def user_update():
    data = request.get_json()
    make = data['make']
    model = data['model']
    year = data['year']
    chassis_id = data['chassis_id']
    car = Car(make=make, model=model, year=year, chassis_id=chassis_id)
    db.session.add(car)
    db.session.commit()
    return car_schema.jsonify(car)


if __name__ == '__main__':
    app.run(debug=True)
