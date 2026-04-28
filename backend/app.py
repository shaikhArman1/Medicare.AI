import os
import math
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load mock data
from mock_hospitals import mock_hospitals

load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Vercel frontend

# Configure Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Ensure upload directory exists
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

@app.route('/')
def index():
    return jsonify({"status": "ok", "message": "Medicare.ai API is running"})

@app.route('/api/hospitals', methods=['GET'])
def get_hospitals():
    user_lat = request.args.get('lat', type=float)
    user_lon = request.args.get('lon', type=float)
    specialty = request.args.get('specialty', default='', type=str).strip().title()

    if not user_lat or not user_lon:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    results = []
    
    for hospital in mock_hospitals:
        # Check if they have the specialty
        if specialty and specialty not in hospital['specialists']:
            continue
            
        distance = haversine_distance(user_lat, user_lon, hospital['lat'], hospital['lon'])
        
        # Determine availability
        if specialty:
            avail = hospital['specialists'][specialty]
            available_now = avail['available_now']
            next_available = avail['next_available_in_hours']
        else:
            # If no specialty provided, just list them
            available_now = True
            next_available = 0
            
        hospital_data = {
            "id": hospital["id"],
            "name": hospital["name"],
            "address": hospital["address"],
            "reception_number": hospital["reception_number"],
            "lat": hospital["lat"],
            "lon": hospital["lon"],
            "distance_km": round(distance, 2),
            "available_now": available_now,
            "next_available_in_hours": next_available
        }
        results.append(hospital_data)
        
    # Sort by Availability (True first), then by distance
    results.sort(key=lambda x: (not x['available_now'], x['next_available_in_hours'], x['distance_km']))

    return jsonify(results)

@app.route('/api/analyze-prescription', methods=['POST'])
def analyze_prescription():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    if not GEMINI_API_KEY:
        return jsonify({"error": "Gemini API key not configured"}), 500

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        # Uploading to Gemini
        gemini_file = genai.upload_file(filepath)
        
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        prompt = """
        Analyze this medical prescription.
        Extract and return a structured list with the following information:
        - Suspected Diagnosis or Disease Summary (What the patient is likely suffering from)
        - List of Medicines
        - Dosage instructions, frequency, and duration for each medicine
        - Warnings or Contraindications (if any general advice based on the medicines).
        Format the output clearly in JSON matching this schema:
        {
          "disease_summary": "...",
          "medicines": [
            {"name": "Med 1", "dosage": "...", "frequency": "...", "duration": "..."}
          ],
          "warnings": ["Warning 1", "Warning 2"]
        }
        Do not use markdown blocks, just return raw JSON string.
        """
        
        response = model.generate_content([prompt, gemini_file])
        
        try:
            import json
            result_json = json.loads(response.text.strip())
            return jsonify(result_json)
        except json.JSONDecodeError:
            # Fallback if it returns text instead of strict JSON
            # try removing markdown ticks
            text = response.text.strip()
            if text.startswith('```json'): text = text[7:]
            if text.startswith('```'): text = text[3:]
            if text.endswith('```'): text = text[:-3]
            try:
                result_json = json.loads(text.strip())
                return jsonify(result_json)
            except:
                return jsonify({"error": "Failed to parse model output as JSON", "raw_text": response.text}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
