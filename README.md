# MediRoute — Emergency Medical Navigation Platform

Patients in medical emergencies waste critical time because no platform tells them *which nearby hospital has their required specialist available right now*. MediRoute solves this by intelligently routing users to the right doctor, at the right hospital, at the right time.

---

## Tech Stack

### Backend
| | |
|---|---|
| Framework | Flask 3.0.2 |
| AI / ML | Google Generative AI — `google-generativeai==0.4.0` |
| Request Handling | Werkzeug 3.0.1 |
| Environment Config | python-dotenv 1.0.1 |
| Geolocation | geopy 2.4.1 + custom Haversine implementation |
| Language | Python |

### Frontend
| | |
|---|---|
| Markup | HTML5 (semantic) |
| Styling | CSS3 — variables, glass-morphism, responsive layout |
| Fonts | Outfit via Google Fonts |
| Scripting | Vanilla JavaScript |
| Maps | Leaflet 1.9.4 with OpenStreetMap tiles |
| Icons | Font Awesome 6.4.0 |

### Data
- Mock hospital database (Kolkata-based)
- Includes: coordinates, specialist availability, contact info

---

## Architecture

```
Browser (HTML/CSS/JS + Leaflet)
        │
        ▼
Flask Backend (app.py)
        │
        ├── /api/hospitals  ──▶  Haversine distance calc  ──▶  Mock DB
        │
        └── Gemini API  ──▶  Prescription AI
```

- **Client-Server Model** — Flask serves the frontend and exposes REST APIs
- **Geolocation** — Browser Geolocation API with manual city input as fallback
- **Distance Calculation** — Custom Haversine formula for real-time proximity ranking

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/harkirat-data/Medicare.git
cd Medicare

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key
cp .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here

# Run the app
python app.py
```

---

## Project Structure

```
mediroute/
├── data/
│   └── mock_hospitals.py    # Kolkata hospital mock data
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── uploads/                 # Prescription image uploads
├── app.py                   # Flask app — routes, Gemini, Haversine
├── index.html
├── requirements.txt
├── .env.example
└── README.md
```

---

## Features

- **Hospital Discovery** — finds nearby hospitals based on live user location
- **Specialist Search** — filter by doctor type (e.g., Cardiologist, Neurologist)
- **Availability Prioritization** — hospitals ranked by specialist availability
- **Interactive Map** — Leaflet-powered map with hospital markers
- **One-tap Contact** — direct call to hospital reception for confirmation
- **Prescription AI** — upload a prescription, get plain-language explanation via Gemini

---

## Roadmap

- [ ] Live doctor availability via real hospital API integration
- [ ] Symptom → specialist AI recommendation
- [ ] Ambulance routing with optimized navigation
- [ ] Voice interface for elderly users
- [ ] Digital health record storage

---

## Built For

Hackolution — IEM &nbsp;|&nbsp; Google Solutions Challenge

---

## License

[MIT](LICENSE)

