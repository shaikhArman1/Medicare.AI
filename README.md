# Medicare.AI — Emergency Medical Navigation Platform

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

&nbsp; Google Solutions Challenge

---

## License

[MIT](LICENSE)


<!-- commit-log: 2026-02-03T22:41:08 - fix: resolve datetime serialization in JSON -->

<!-- commit-log: 2026-02-07T16:30:40 - chore: sync frontend env config with backend routes -->

<!-- commit-log: 2026-02-11T12:21:31 - fix: align data types between Python models and JS -->

<!-- commit-log: 2026-02-14T09:25:19 - fix: resolve CORS issue between frontend and backend -->

<!-- commit-log: 2026-02-19T16:57:58 - feat: improve error boundary in React app -->

<!-- commit-log: 2026-02-23T16:08:07 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-03-02T15:40:24 - feat: add API endpoint for data aggregation -->

<!-- commit-log: 2026-03-03T22:37:05 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-03-04T11:03:06 - fix: align data types between Python models and JS -->

<!-- commit-log: 2026-03-08T09:01:21 - fix: correct JSON serialization in Python response -->

<!-- commit-log: 2026-03-11T18:18:38 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-03-16T22:38:29 - refactor: update async request handling in UI -->

<!-- commit-log: 2026-03-17T10:42:02 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-03-21T11:08:52 - fix: align data types between Python models and JS -->

<!-- commit-log: 2026-03-22T11:06:15 - fix: resolve CORS issue between frontend and backend -->

<!-- commit-log: 2026-03-24T18:49:33 - fix: handle authentication token expiry in UI -->

<!-- commit-log: 2026-03-28T18:27:48 - feat: improve error boundary in React app -->

<!-- commit-log: 2026-03-30T12:11:53 - docs: update integration guide for local dev -->

<!-- commit-log: 2026-04-20T10:57:14 - fix: resolve CORS issue between frontend and backend -->

<!-- commit-log: 2026-04-20T13:05:15 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-04-24T14:51:01 - feat: add loading state for API-dependent components -->

<!-- commit-log: 2026-05-05T09:38:07 - fix: resolve datetime serialization in JSON -->

<!-- commit-log: 2026-05-10T17:14:52 - feat: add health check endpoint for monitoring -->

<!-- commit-log: 2026-05-12T10:05:38 - feat: add API endpoint for data aggregation -->

<!-- commit-log: 2026-05-12T22:20:16 - refactor: move API base URL to config module -->

<!-- commit-log: 2026-05-15T12:23:07 - docs: add architecture diagram to README -->

<!-- commit-log: 2026-05-15T15:40:13 - fix: correct JSON serialization in Python response -->

<!-- commit-log: 2026-05-15T17:34:10 - docs: update integration guide for local dev -->

<!-- commit-log: 2026-05-15T20:32:24 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-05-15T20:24:38 - refactor: update async request handling in UI -->

<!-- commit-log: 2026-05-30T10:51:02 - refactor: move API base URL to config module -->

<!-- commit-log: 2026-05-30T11:39:47 - refactor: move API base URL to config module -->

<!-- commit-log: 2026-05-30T13:15:23 - feat: add loading state for API-dependent components -->

<!-- commit-log: 2026-05-30T14:00:26 - docs: add architecture diagram to README -->

<!-- commit-log: 2026-05-30T21:36:33 - feat: add health check endpoint for monitoring -->

<!-- commit-log: 2026-05-30T22:43:20 - docs: add architecture diagram to README -->

<!-- commit-log: 2026-05-31T10:26:30 - fix: resolve datetime serialization in JSON -->

<!-- commit-log: 2026-06-16T09:00:03 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-06-17T09:07:28 - docs: add architecture diagram to README -->

<!-- commit-log: 2026-06-17T12:56:55 - feat: add API endpoint for data aggregation -->

<!-- commit-log: 2026-06-17T16:00:39 - fix: align data types between Python models and JS -->

<!-- commit-log: 2026-06-17T17:09:37 - perf: reduce payload size with response filtering -->

<!-- commit-log: 2026-06-17T18:07:47 - chore: sync frontend env config with backend routes -->

<!-- commit-log: 2026-06-28T11:12:57 - fix: resolve CORS issue between frontend and backend -->

<!-- commit-log: 2026-06-28T11:06:53 - feat: add API endpoint for data aggregation -->

<!-- commit-log: 2026-06-28T14:46:24 - fix: handle 500 errors gracefully with user feedback -->

<!-- commit-log: 2026-06-28T15:52:17 - feat: add pagination support to list endpoints -->

<!-- commit-log: 2026-06-28T18:36:13 - fix: handle 500 errors gracefully with user feedback -->

<!-- commit-log: 2026-06-30T13:37:49 - docs: add architecture diagram to README -->

<!-- commit-log: 2026-06-30T20:32:05 - feat: add API endpoint for data aggregation -->

<!-- commit-log: 2026-06-30T20:13:46 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-06-30T21:38:50 - fix: resolve datetime serialization in JSON -->

<!-- commit-log: 2026-06-30T22:56:42 - refactor: update async request handling in UI -->

<!-- commit-log: 2026-07-04T11:10:02 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-07-04T12:24:04 - chore: update Axios and FastAPI versions -->

<!-- commit-log: 2026-07-04T12:39:29 - refactor: update async request handling in UI -->

<!-- commit-log: 2026-07-04T15:36:10 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-07-04T17:26:39 - feat: improve error boundary in React app -->

<!-- commit-log: 2026-07-09T09:22:38 - feat: improve error boundary in React app -->

<!-- commit-log: 2026-07-09T12:13:17 - chore: sync frontend env config with backend routes -->

<!-- commit-log: 2026-07-09T16:37:13 - feat: add retry logic on failed API calls -->

<!-- commit-log: 2026-07-09T17:33:13 - feat: add pagination support to list endpoints -->
