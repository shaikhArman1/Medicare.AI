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
        "address": "New Town, Kolkata",
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
        "address": "VIP Road, Kolkata",
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
        "address": "Salt Lake, Kolkata",
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
        "address": "EM Bypass, Kolkata",
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
        "address": "Kasba, Kolkata",
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
        "address": "Mukundapur, Kolkata",
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
        "name": "Woodlands Hospital",
        "address": "Alipore, Kolkata",
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
        "address": "Elgin, Kolkata",
        "lat": 22.5401,
        "lon": 88.3518,
        "reception_number": "+91-98300-78901",
        "specialists": {
            "Dermatologist": {"available_now": True, "next_available_in_hours": 0},
            "Pediatrician": {"available_now": False, "next_available_in_hours": 2},
            "Cardiologist": {"available_now": False, "next_available_in_hours": 24}
        }
    },

    # 🔥 EXTRA DATA (for strong demo)

    {
        "id": "h11",
        "name": "SSKM Hospital",
        "address": "AJC Bose Road, Kolkata",
        "lat": 22.5383,
        "lon": 88.3430,
        "reception_number": "+91-98300-11111",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "Neurologist": {"available_now": True, "next_available_in_hours": 0},
            "Orthopedic": {"available_now": False, "next_available_in_hours": 3}
        }
    },
    {
        "id": "h12",
        "name": "Medical College Kolkata",
        "address": "College Street",
        "lat": 22.5726,
        "lon": 88.3639,
        "reception_number": "+91-98300-22222",
        "specialists": {
            "General Physician": {"available_now": True, "next_available_in_hours": 0},
            "Cardiologist": {"available_now": False, "next_available_in_hours": 2},
            "Pediatrician": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h13",
        "name": "Desun Hospital",
        "address": "Kasba, Kolkata",
        "lat": 22.5130,
        "lon": 88.4025,
        "reception_number": "+91-98300-33333",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "Pulmonologist": {"available_now": False, "next_available_in_hours": 5},
            "Dermatologist": {"available_now": True, "next_available_in_hours": 0}
        }
    },
    {
        "id": "h14",
        "name": "ILS Hospital",
        "address": "Salt Lake",
        "lat": 22.5835,
        "lon": 88.4172,
        "reception_number": "+91-98300-44444",
        "specialists": {
            "Orthopedic": {"available_now": True, "next_available_in_hours": 0},
            "General Surgeon": {"available_now": True, "next_available_in_hours": 0},
            "Neurologist": {"available_now": False, "next_available_in_hours": 6}
        }
    },
    {
        "id": "h15",
        "name": "CMRI Hospital",
        "address": "Alipore",
        "lat": 22.5222,
        "lon": 88.3375,
        "reception_number": "+91-98300-55555",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "Gastroenterologist": {"available_now": True, "next_available_in_hours": 0},
            "Dermatologist": {"available_now": False, "next_available_in_hours": 4}
        }
    },
    {
        "id": "h16",
        "name": "Narayana Multispeciality Hospital",
        "address": "Howrah",
        "lat": 22.5958,
        "lon": 88.2636,
        "reception_number": "+91-98300-66666",
        "specialists": {
            "Cardiologist": {"available_now": True, "next_available_in_hours": 0},
            "Neurologist": {"available_now": False, "next_available_in_hours": 2},
            "Orthopedic": {"available_now": True, "next_available_in_hours": 0}
        }
    }
]