mock_hospitals = [
    {
        "id": "h1",
        "name": "Charnock Hospital",
        "address": "Chinar Park, Rajarhat, Kolkata",
        "lat": 22.6352,
        "lon": 88.4333,
        "reception_number": "+91-98765-43210",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "Neurologist": {"available_now": False, "next_available_in_hours": 2},
            "Pediatrician": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h2",
        "name": "Apollo Clinic (New Town)",
        "address": "The Galleria, Action Area IB, New Town, Kolkata",
        "lat": 22.5857,
        "lon": 88.4635,
        "reception_number": "+91-98333-11111",   
        "specialists": {
            "Cardiologist": {"available_now": False, "next_available_in_hours": 1},
            "Orthopedic": {"available_now": True, "next_available_in_hours": 0},
            "Dermatologist": {"available_now": False, "next_available_in_hours": 24}
        }
    },
    {
        "id": "h3",
        "name": "Spandan Hospital",
        "address": "VIP Road, Teghoria, Kolkata",
        "lat": 22.6180,
        "lon": 88.4410,
        "reception_number": "+91-99999-88888",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "General Surgeon": {"available_now": True, "next_available_in_hours": 0},
            "Pulmonologist": {"available_now": False, "next_available_in_hours": 8}
        }
    },
    {
        "id": "h4",
        "name": "AMRI Hospitals (Salt Lake)",
        "address": "JC Block, Sector III, Salt Lake, Kolkata",
        "lat": 22.5714,
        "lon": 88.4061,
        "reception_number": "+91-98300-12345",
        "specialists": {
            "Neurologist": {"available_now": True, "next_available_in_hours": 0},
            "Cardiologist": {"available_now": False, "next_available_in_hours": 4},
            "Orthopedic": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h5",
        "name": "Fortis Hospital (Anandapur)",
        "address": "730, Anandapur, EM Bypass, Kolkata",
        "lat": 22.5181,
        "lon": 88.4034,
        "reception_number": "+91-98300-23456",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "General Surgeon": {"available_now": False, "next_available_in_hours": 2},
            "Pediatrician": {"available_now": False, "next_available_in_hours": 12}
        }
    },
    {
        "id": "h6",
        "name": "Ruby General Hospital",
        "address": "Kasba Golpark, EM Bypass, Kolkata",
        "lat": 22.5126,
        "lon": 88.3934,
        "reception_number": "+91-98300-34567",
        "specialists": {
            "Pulmonologist": {"available_now": True, "next_available_in_hours": 0},
            "Orthopedic": {"available_now": True, "next_available_in_hours": 0},
            "Dermatologist": {"available_now": False, "next_available_in_hours": 3}
        }
    },
    {
        "id": "h7",
        "name": "Medica Superspecialty Hospital",
        "address": "Mukundapur, EM Bypass, Kolkata",
        "lat": 22.4938,
        "lon": 88.4013,
        "reception_number": "+91-98300-45678",
        "specialists": {
            "Cardiologist": {"available_now": False, "next_available_in_hours": 1},
            "Neurologist": {"available_now": True, "next_available_in_hours": 0},
            "General Surgeon": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h8",
        "name": "Peerless Hospital",
        "address": "Panchasayar, Kolkata",
        "lat": 22.4839,
        "lon": 88.3976,
        "reception_number": "+91-98300-56789",
        "specialists": {
            "Gastroenterologist": {"available_now": True, "next_available_in_hours": 0},
            "Cardiologist": {"available_now": False, "next_available_in_hours": 3},
            "Pediatrician": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h9",
        "name": "Woodlands Multispeciality",
        "address": "Alipore Road, Alipore, Kolkata",
        "lat": 22.5312,
        "lon": 88.3304,
        "reception_number": "+91-98300-67890",
        "specialists": {
            "Neurologist": {"available_now": False, "next_available_in_hours": 5},
            "General Surgeon": {"available_now": True, "next_available_in_hours": 0},
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h10",
        "name": "Belle Vue Clinic",
        "address": "Loudon Street, Elgin, Kolkata",
        "lat": 22.5401,
        "lon": 88.3518,
        "reception_number": "+91-98300-78901",
        "specialists": {
            "Dermatologist": {"available_now": True, "next_available_in_hours": 0},
            "Pediatrician": {"available_now": False, "next_available_in_hours": 2},
            "Cardiologist": {"available_now": False, "next_available_in_hours": 24}
        }
    }
]
