from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API keys
SKYSCANNER_API_KEY = "abcdef1234567890"
HOTELS_COMBINED_API_KEY = "ghijkl1234567890"
OPENWEATHERMAP_API_KEY = "mnopqr1234567890"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        destination = request.form["destination"]
        travel_dates = request.form["travel_dates"]

        # Fetch flight data from Skyscanner API
        skyscanner_url = f"https://api.example.com/skyscanner?api_key={SKYSCANNER_API_KEY}&destination={destination}&dates={travel_dates}"
        skyscanner_response = requests.get(skyscanner_url)
        flight_data = skyscanner_response.json()
        
        # Fetch hotel data from Hotels Combined API
        hotels_combined_url = f"https://api.example.com/hotelscombined?api_key={HOTELS_COMBINED_API_KEY}&destination={destination}&dates={travel_dates}"
        hotels_combined_response = requests.get(hotels_combined_url)
        hotel_data = hotels_combined_response.json()
        
        # Fetch weather data from OpenWeatherMap API
        openweathermap_url = f"https://api.example.com/openweathermap?api_key={OPENWEATHERMAP_API_KEY}&destination={destination}"
        weather_response = requests.get(openweathermap_url)
        weather_data = weather_response.json()
        
        # Combine and format the data
        combined_data = {
            "flight_data": flight_data,
            "hotel_data": hotel_data,
            "weather_data": weather_data
        }
        
        return render_template("index.html", data=combined_data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

