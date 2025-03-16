# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

# Create the database tables within the application context
with app.app_context():
    db.create_all()

@app.route('/track_number', methods=['POST'])
def track_number():
    number = request.json.get('phone_number')
    api_key = "8e5f6daaa50f47488ab5bc36b295e7a5"  # Replace with your OpenCage API Key

    # Parse the phone number
    phone_number = phonenumbers.parse(number)

    # Get location and service provider
    location = geocoder.description_for_number(phone_number, "en")
    service_provider = carrier.name_for_number(phone_number, "en")

    # Get latitude and longitude using OpenCage API
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(location)

    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        response = {
            "location": location,
            "service_provider": service_provider,
            "latitude": lat,
            "longitude": lng
        }
    else:
        response = {"error": "Location not found"}

    return jsonify(response)

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    new_location = Location(latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(new_location)
    db.session.commit()
    return jsonify({"status": "success", "data": data})

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return jsonify([{"latitude": loc.latitude, "longitude": loc.longitude} for loc in locations])

if __name__ == '__main__':
    app.run(debug=True)