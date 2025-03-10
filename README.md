# 📍 Phone Number Tracker API
🚀 A Flask-based API to track phone numbers, retrieve their geographical location, and store location data!

## 🌟 Features
✅ Track phone numbers to get their location and service provider.
✅ Retrieve latitude and longitude using the OpenCage API.
✅ Store and retrieve location data in an SQLite database.
✅ Simple REST API endpoints for easy integration.

## ⚙️ Tech Stack
🔹 Backend: Python 🐍 (Flask, Flask-SQLAlchemy)
🔹 API Integration: OpenCage Geocoder 🌍, phonenumbers 📞
🔹 Database: SQLite 🛢️
🔹 Deployment: Localhost / Cloud ☁️
🔹 Version Control: GitHub 🛠️

## 🚀 Installation & Usage
1️⃣ **Clone the Repository**
```bash
$ git clone https://github.com/lokeshagarwal2304/Location-Tracking-Using-Phone-Number.git
$ cd Location-Tracking-Using-Phone-Number
```
2️⃣ **Install Dependencies**
```bash
$ pip install -r requirements.txt
```
3️⃣ **Set Up API Key**(Will be Soon Announced)
Replace the placeholder OpenCage API key in `app.py` with your actual key:
```python
api_key = "your_opencage_api_key_here"
```
4️⃣ **Run the Application**
```bash
$ python app.py
```

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/track_number` | Track phone number location |
| POST | `/update_location` | Store location data |
| GET | `/locations` | Retrieve stored locations |

### 📤 Request: `/track_number`
```json
{
  "phone_number": "+91 9154151265"
}
```
### 📥 Response:
```json
{
  "location": "Hyd, India",
  "service_provider": "Verizon",
  "latitude": 12.7128,
  "longitude": 78.0060
}
```

## 🔥 Projecting Skills & Contributions
✔️ API Development – Designing scalable, production-ready REST APIs.
✔️ Geolocation Services – Using OpenCage Geocoder for real-world mapping.
✔️ Database Management – Storing and retrieving location data efficiently.
✔️ Flask Framework – Building lightweight, high-performance APIs.
✔️ Scalability & Optimization – Ensuring fast response times.

## 💡 Future Enhancements
🔹 User Authentication – Secure API with OAuth2/JWT.
🔹 Web Dashboard – Visualize tracked locations on a map.
🔹 Cloud Deployment – Host on AWS/GCP for public access.

## 📜 License
This project is licensed under the MIT License and Used python .gitignore .

## 🤝 Contributing
Contributions are welcome! 🎉
- Fork the repository 🍴
- Create a new branch 🔀
- Make improvements 🔧
- Submit a pull request ✨
- I'm fast and ready to collab,so Please Support 
## 📬 Contact
📧 Email: lokeshagarwal2304@gmail.com
💼 LinkedIn: lokeshagarwal2304
🐦 Twitter: lagarwal2304

