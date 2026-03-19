# A simple backend for the Fresh Bridge application using Flask.
# This code creates a web server with API endpoints to simulate AI functionalities.

# --- Installation ---
# Before running, you need to install Flask:
# pip install Flask Flask-Cors

from flask import Flask, jsonify, request
from flask_cors import CORS
import random
import datetime

# --- App Setup ---
# Initialize the Flask application
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) to allow our front-end HTML file 
# to communicate with this server.
CORS(app)

# --- Mock Database ---
# In a real application, this data would be in a SQL database.
# We are using a simple list of dictionaries to store the data in memory.
mock_db = {
    "listings": [
        {'id': 'm1', 'type': 'SELL', 'user': 'Ramesh K.', 'crop': 'Tomatoes', 'quantity': 200, 'price': 30, 'location': 'Nashik', 'img': '1f9c5', 'category': 'vegetable', 'owner': 'farmer_user' },
        {'id': 'm2', 'type': 'BUY', 'user': 'Mumbai Grocers', 'crop': 'Onions', 'quantity': 1000, 'price': 22, 'location': 'Mumbai', 'img': '1f9c6', 'category': 'vegetable' },
        {'id': 'm3', 'type': 'STORAGE', 'user': 'Pune Cold Storage', 'crop': 'Available Space', 'quantity': 5000, 'price': 5, 'location': 'Pune', 'img': '1f9ca', 'category': 'all' },
        {'id': 'm4', 'type': 'SELL', 'user': 'Sunita P.', 'crop': 'Mangoes', 'quantity': 500, 'price': 150, 'location': 'Ratnagiri', 'img': '1f96d', 'category': 'fruit', 'owner': 'other_user' }
    ]
}

# --- API Endpoints for Listings (CRUD Operations) ---

# Endpoint to get all listings
@app.route('/api/listings', methods=['GET'])
def get_listings():
    return jsonify(mock_db['listings'])

# Endpoint to add a new listing
@app.route('/api/listings', methods=['POST'])
def add_listing():
    new_listing_data = request.json
    # In a real app, you'd do validation here
    new_listing_data['id'] = 'm' + str(int(datetime.datetime.now().timestamp()))
    mock_db['listings'].append(new_listing_data)
    return jsonify(new_listing_data), 201


# --- AI Simulation Endpoints ---

# 1. AI Demand Forecast Endpoint
@app.route('/api/forecast', methods=['GET'])
def get_demand_forecast():
    # Get parameters from the front-end request, e.g., /api/forecast?crop=Tomatoes&market=Pune
    crop = request.args.get('crop', 'Unknown')
    market = request.args.get('market', 'Unknown')

    # --- AI Simulation Logic ---
    # A real AI model would take crop, market, historical data, and weather as inputs.
    # We will simulate this by generating a plausible-looking forecast.
    forecast_data = []
    base_demand = random.randint(50, 80) # Base demand percentage
    for i in range(7):
        # Add some random daily fluctuation
        daily_fluctuation = random.randint(-15, 15)
        demand = max(20, min(100, base_demand + daily_fluctuation))
        forecast_data.append(demand)
        # Slightly adjust the base demand for the next day
        base_demand += random.randint(-5, 5)

    # Generate a dynamic AI insight based on the forecast
    peak_day = forecast_data.index(max(forecast_data)) + 1
    insight = f"AI predicts a demand peak for {crop} in {market} around day {peak_day}. Consider adjusting supply."
    
    response = {
        "crop": crop,
        "market": market,
        "forecast": forecast_data, # A list of 7 numbers representing demand
        "insight": insight
    }
    return jsonify(response)


# 2. AI Route Optimization Endpoint
@app.route('/api/route', methods=['GET'])
def get_optimal_route():
    # Get parameters from the front-end, e.g., /api/route?origin=Nashik&destination=Mumbai
    origin = request.args.get('origin', 'Unknown')
    destination = request.args.get('destination', 'Unknown')

    # --- AI Simulation Logic ---
    # A real AI would use Google Maps API, traffic data (e.g., Here API), and weather APIs.
    # It would find the best route considering spoilage time, traffic, and available cold storages.
    # We will simulate this with realistic-looking dummy data.
    
    # Simulate a traffic alert
    traffic_alert = ""
    if random.random() > 0.5: # 50% chance of a traffic alert
        traffic_alert = f"Heavy traffic reported near Thane. AI suggests a minor detour via Ghodbunder Road."

    # Simulate a cold storage suggestion
    storage_suggestion = ""
    if random.random() > 0.6: # 60% chance of a storage suggestion
        storage_suggestion = f"'Cold Storage A' has {random.randint(60,95)}% capacity available. Recommended for temporary storage if market prices at {destination} are low."

    response = {
        "origin": origin,
        "destination": destination,
        "distance_km": random.randint(150, 200),
        "duration_mins": random.randint(180, 240),
        "traffic_alert": traffic_alert,
        "storage_suggestion": storage_suggestion,
        # In a real app, this would be a series of coordinates for the map
        "route_path": "simulated_path_data"
    }
    return jsonify(response)


# --- Main Execution ---
if __name__ == '__main__':
    # This makes the server accessible on your local network.
    # The debug=True flag means the server will automatically reload if you change the code.
    app.run(host='0.0.0.0', port=5000, debug=True)