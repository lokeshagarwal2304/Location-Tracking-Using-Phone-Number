# phone_location_tracker.py
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

def get_phone_location(phone_number, api_key):
    # Parse the phone number
    parsed_number = phonenumbers.parse(phone_number)

    # Get location and service provider
    location = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")

    # Get latitude and longitude using OpenCage API
    geocoder = OpenCageGeocode(api_key)
    results = geocoder.geocode(location)

    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        return {
            "location": location,
            "service_provider": service_provider,
            "latitude": lat,
            "longitude": lng
        }
    else:
        return {"error": "Location not found"}

if __name__ == "__main__":
    # Input your OpenCage API Key here
    api_key = "8e5f6daaa50f47488ab5bc36b295e7a5"  # Replace with your OpenCage API Key

    # Input phone number
    phone_number = input("Enter the phone number with country code (e.g., +919154151265 ")

    # Get location details
    location_info = get_phone_location(phone_number, api_key)

    # Print the results
    print(location_info)
