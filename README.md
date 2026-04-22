# Medicare.AI — Emergency Medical Navigation Platform

Patients in medical emergencies waste critical time because no platform tells them *which nearby hospital has their required specialist available right now*. MediRoute solves this by intelligently routing users to the right doctor, at the right hospital, at the right time.

---

## What It Does

**Smart Doctor & Hospital Discovery**
- Detects user location and fetches nearby hospitals
- User searches for a specialist (e.g., "Cardiologist")
- AI prioritizes hospitals based on doctor availability, distance, and emergency suitability

**Emergency Decision Assistance**
- Shows hospital details and availability status
- One-tap call to the hospital reception desk for confirmation
- Built for speed — fewer taps, faster decisions

**Prescription AI**
- Upload a prescription and get a plain-language breakdown
- Covers medicine names, dosage instructions, and warnings
- Designed for patients who struggle with medical terminology

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | Python, Flask |
| AI | Google Gemini API |
| Hospital Data | Mock JSON (static) |
| Config | python-dotenv |

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/harkirat-data/Medicare.AI.git
cd mediroute

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
MEDICARE.AI/
├── data/
│   └── mock_hospitals.py    # Mock hospital dataset
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── uploads/                 # Prescription image uploads
├── app.py                   # Main Flask app
├── index.html
├── requirements.txt
├── .env.example
└── README.md
```

---

## Roadmap

- [ ] Live doctor availability via hospital API integration
- [ ] Symptom → specialist AI recommendation
- [ ] Ambulance routing with optimized navigation
- [ ] Voice interface for elderly users
- [ ] Digital health record storage

---

## Built For

&nbsp; Google Solutions Challenge

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)
