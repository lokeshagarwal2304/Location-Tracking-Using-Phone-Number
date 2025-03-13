import requests
import webbrowser

# Function to get location using IP and Wi-Fi signals
def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()

        ip = data.get("ip", "Unknown")
        city = data.get("city", "Unknown")
        region = data.get("region", "Unknown")
        country = data.get("country", "Unknown")
        loc = data.get("loc", "Unknown")  # Latitude and Longitude

        print(f"IP Address: {ip}")
        print(f"Location: {city}, {region}, {country}")
        print(f"Coordinates: {loc}")

        # Open Google Maps with coordinates
        if loc != "Unknown":
            maps_url = f"https://www.google.com/maps?q={loc}"
            print(f"Opening Google Maps: {maps_url}")
            webbrowser.open(maps_url)
        else:
            print("Location not found.")

    except Exception as e:
        print("Error fetching location:", e)

# Run the function
get_location()

print("Location tracking completed. Thank you!")
