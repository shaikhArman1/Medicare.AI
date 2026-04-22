mock_hospitals = [
    {
        "id": "h17",
        "name": "Narayana Memorial Hospital",
        "address": "Behala, Kolkata",
        "lat": 22.4956,
        "lon": 88.3169,
        "reception_number": ["+91-033-6640-0000", "+91-7383086144"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Bimal Kahar", "experience": "15+ years", "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Md Rashid Zeya Ayubi", "experience": "10+ years", "available_now": False, "next_available_in_hours": 2}
            ],
            "Dermatologist": [
                {"name": "Dr. Nisha Agarwal", "experience": "12+ years", "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Aniruddha Ghosh", "experience": "8+ years", "available_now": False, "next_available_in_hours": 3}
            ]
        }
    },
    {
        "id": "h18",
        "name": "Kolkata Port Trust Hospital",
        "address": "New Alipore, Kolkata",
        "lat": 22.518,
        "lon": 88.318,
        "reception_number": "+91-033-2401-4503",
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Jaideep Das Gupta", "experience": "Interventional Cardiologist", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Orthopaedic": [
                {"name": "General Orthopaedic Specialist", "experience": "Hospital Department", "rating": 4.2, "fee": 500, "available_now": True, "next_available_in_hours": 1}
            ],
            "Ophthalmologist": [
                {"name": "Eye Specialist Team", "experience": "Hospital Unit", "rating": 4.0, "fee": 400, "available_now": False, "next_available_in_hours": 2}
            ],
            "ENT Specialist": [
                {"name": "ENT Department", "experience": "Hospital Unit", "rating": 4.1, "fee": 400, "available_now": True, "next_available_in_hours": 0}
            ],
            "Dermatologist": [
                {"name": "Skin Specialist", "experience": "Hospital Unit", "rating": 4.0, "fee": 450, "available_now": False, "next_available_in_hours": 3}
            ],
            "General Physician": [
                {"name": "General Medicine Doctor", "experience": "Hospital Staff", "rating": 4.3, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Pediatrician": [
                {"name": "Child Specialist", "experience": "Hospital Staff", "rating": 4.2, "fee": 350, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Surgeon": [
                {"name": "Surgery Department", "experience": "Spine & Plastic Surgery", "rating": 4.4, "fee": 700, "available_now": False, "next_available_in_hours": 4}
            ]
        }
    },
    {
        "id": "h19",
        "name": "B.P. Poddar Hospital",
        "address": "New Alipore, Kolkata",
        "lat": 22.5118,
        "lon": 88.3322,
        "reception_number": "+91-085850-35846",
        "specialists": {
            "General Physician": [
                {"name": "Dr. Satyaki Basu", "experience": "Medicine", "rating": 4.5, "fee": 500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. M K Chaudhuri", "experience": "Internal Medicine", "rating": 4.2, "fee": 500, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Buddhadev Roy", "experience": "Internal Medicine", "rating": 4.1, "fee": 450, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Neha Karnani Agarwal", "experience": "Medicine", "rating": 4.3, "fee": 500, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Puspita Mondal", "experience": "Medicine", "rating": 4.0, "fee": 450, "available_now": True, "next_available_in_hours": 0}
            ],
            "Pediatrician": [
                {"name": "Dr. Jitabrata Ray", "experience": "Pediatrics", "rating": 4.4, "fee": 400, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Surgeon": [
                {"name": "Dr. Saptarshi Kundu", "experience": "General Surgery", "rating": 4.6, "fee": 700, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Sayanika Pratihar", "experience": "Surgery", "rating": 4.3, "fee": 650, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Somak Ghosh", "experience": "Surgery", "rating": 4.2, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "Gynecologist": [
                {"name": "Dr. Rajib Sarkar", "experience": "Obstetrics & Gynaecology", "rating": 4.5, "fee": 600, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Ayan Mukopadhyay", "experience": "Gynaecology", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 0}
            ],
            "Cardiologist": [
                {"name": "Dr. R S Agarwal", "experience": "Cardiology", "rating": 4.6, "fee": 800, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Abhijit Aich Bhowmick", "experience": "Cardiology", "rating": 4.4, "fee": 750, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Santanu Dutta", "experience": "Cardiology", "rating": 4.3, "fee": 700, "available_now": False, "next_available_in_hours": 2}
            ],
            "Orthopaedic": [
                {"name": "Dr. Abhijit Sen", "experience": "Orthopaedics", "rating": 4.5, "fee": 600, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Suday Mukherjee", "experience": "Orthopaedics", "rating": 4.2, "fee": 550, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Shibratan Pathak", "experience": "Gastroenterology", "rating": 4.4, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Psychiatrist": [
                {"name": "Dr. Angshuman Das", "experience": "Psychiatry", "rating": 4.2, "fee": 500, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Debdatta Pati", "experience": "Neuropsychiatry", "rating": 4.1, "fee": 500, "available_now": True, "next_available_in_hours": 0}
            ],
            "Ophthalmologist": [
                {"name": "Dr. Nandini Chandak", "experience": "Eye Specialist", "rating": 4.3, "fee": 400, "available_now": True, "next_available_in_hours": 0}
            ],
            "Dentist": [
                {"name": "Dr. Vipin Patel", "experience": "Dental", "rating": 4.0, "fee": 300, "available_now": False, "next_available_in_hours": 2}
            ],
            "Pulmonologist": [
                {"name": "Dr. Samadarshi Datta", "experience": "Pulmonology", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ]
        }
    },
    {
        "id": "h20",
        "name": "Vidyasagar State General Hospital",
        "address": "Behala, Kolkata",
        "lat": 22.4987,
        "lon": 88.3155,
        "reception_number": ["+91-033-2397-1591", "+91-090073-55352"],
        "specialists": {
            "General Physician": [
                {"name": "Dr. Somnath Ghosh", "experience": "General Medicine", "rating": 4.2, "fee": 300, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Bijoy Guha Roy", "experience": "General Medicine", "rating": 4.1, "fee": 300, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Bijali Majumdar", "experience": "General Medicine", "rating": 4.0, "fee": 300, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Arunabha Saha", "experience": "General Medicine", "rating": 4.1, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Archita Biswas", "experience": "Obstetrics & Gynaecology", "rating": 4.3, "fee": 350, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Saswati Naskar", "experience": "Gynaecology", "rating": 4.2, "fee": 350, "available_now": False, "next_available_in_hours": 2}
            ],
            "Dentist": [
                {"name": "Dr. Srija Sanyal", "experience": "Dental Surgery", "rating": 4.2, "fee": 200, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Surgeon": [
                {"name": "Dr. Diptendu Bikas Sengupta", "experience": "General Surgery", "rating": 4.4, "fee": 400, "available_now": False, "next_available_in_hours": 3}
            ],
            "Dermatologist": [
                {"name": "Dr. Sneharanjan Bhattacharyya", "experience": "Dermatology", "rating": 4.1, "fee": 300, "available_now": True, "next_available_in_hours": 1}
            ],
            "Radiologist": [
                {"name": "Dr. Arun Ghosal", "experience": "Radiology", "rating": 4.0, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Anesthesiologist": [
                {"name": "Dr. Subal Bag", "experience": "Anesthesiology", "rating": 4.1, "fee": 300, "available_now": False, "next_available_in_hours": 2}
            ]
        }
    },
    {
        "id": "h21",
        "name": "RSV Hospital",
        "address": "Tollygunge, Kolkata",
        "lat": 22.5033,
        "lon": 88.3421,
        "reception_number": ["+91-033-4081-8000", "+91-033-3001-3000", "+91-099039-99659", "+91-099039-99660"],
        "specialists": {
            "Gynecologist": [
                {"name": "Dr. Susmita Mitra", "experience": "32+ years", "rating": 4.7, "fee": 600, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Nibedita Ray Gaheer", "experience": "26+ years", "rating": 4.5, "fee": 600, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Sujoy Dasgupta", "experience": "Gynaecology", "rating": 4.3, "fee": 550, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopaedic": [
                {"name": "Dr. Abhishek Saha", "experience": "Orthopaedics", "rating": 4.6, "fee": 700, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Kaushik Sarkar", "experience": "Orthopaedics", "rating": 4.4, "fee": 650, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Jagat Jyoti Dhara", "experience": "Orthopaedics", "rating": 4.3, "fee": 650, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Samir Kumar Bhattacharya", "experience": "41+ years", "rating": 4.8, "fee": 500, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Saugata Kumar Bhattacharya", "experience": "General Medicine", "rating": 4.4, "fee": 500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Gautam Sarkar", "experience": "General Medicine", "rating": 4.3, "fee": 450, "available_now": True, "next_available_in_hours": 1}
            ],
            "Psychiatrist": [
                {"name": "Dr. Amlan Kusum Jana", "experience": "Psychiatry", "rating": 4.5, "fee": 600, "available_now": False, "next_available_in_hours": 3}
            ],
            "Nephrologist": [
                {"name": "Dr. Arjun Ray", "experience": "Nephrology", "rating": 4.4, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Dermatologist": [
                {"name": "Dr. Joyeeta Chowdhury", "experience": "Dermatology", "rating": 4.3, "fee": 400, "available_now": True, "next_available_in_hours": 0}
            ],
            "ENT Specialist": [
                {"name": "Dr. Subhadeep Karanjai", "experience": "ENT", "rating": 4.2, "fee": 400, "available_now": False, "next_available_in_hours": 2}
            ],
            "Neurologist": [
                {"name": "Dr. Kanchan Sarkar Chakraborty", "experience": "Neurology/Neurosurgery", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "Pediatrician": [
                {"name": "Dr. Dipankar Roy", "experience": "Pediatric Surgery", "rating": 4.4, "fee": 500, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Leena Sarkar", "experience": "Pediatrics", "rating": 4.3, "fee": 450, "available_now": True, "next_available_in_hours": 0}
            ],
            "Cardiologist": [
                {"name": "Dr. Gautam Sarkar", "experience": "Cardiology", "rating": 4.4, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "Urologist": [
                {"name": "Dr. Kaushik Sarkar", "experience": "Urology", "rating": 4.3, "fee": 700, "available_now": False, "next_available_in_hours": 3}
            ]
        }
    },
    {
        "id": "h22",
        "name": "Behala Balananda Brahmachari Hospital",
        "address": "Behala, Kolkata",
        "lat": 22.51,
        "lon": 88.32,
        "reception_number": "+91-62922672432",
        "specialists": {
            "General Surgeon": [
                {"name": "Dr. Pallab Saha", "experience": "General Surgery", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Prasenjit Mukherjee", "experience": "General Surgery", "rating": 4.2, "fee": 600, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Sayandev Dasgupta", "experience": "General Surgery", "rating": 4.4, "fee": 650, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. N R Chakraborty", "experience": "General Surgery", "rating": 4.3, "fee": 600, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gynecologist": [
                {"name": "Dr. Nidhi Shankar", "experience": "Gynecology", "rating": 4.5, "fee": 600, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Mamta Kar", "experience": "Gynecology", "rating": 4.4, "fee": 550, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Sujoy Dasgupta", "experience": "Infertility Specialist", "rating": 4.6, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Urologist": [
                {"name": "Dr. Kunal Kapoor", "experience": "Urology", "rating": 4.5, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Oncologist": [
                {"name": "Dr. Kanishka Sarkar", "experience": "Oncology", "rating": 4.4, "fee": 800, "available_now": False, "next_available_in_hours": 3}
            ],
            "Pediatrician": [
                {"name": "Dr. Anjanika Pal", "experience": "Pediatrics", "rating": 4.5, "fee": 500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Surojit Basu", "experience": "Rehabilitation", "rating": 4.3, "fee": 450, "available_now": False, "next_available_in_hours": 2}
            ],
            "Ophthalmologist": [
                {"name": "Dr. Chandni Chakraborty", "experience": "Ophthalmology", "rating": 4.4, "fee": 400, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Ranjan Choudhury", "experience": "Ophthalmology", "rating": 4.3, "fee": 400, "available_now": False, "next_available_in_hours": 2}
            ],
            "Microbiologist": [
                {"name": "Dr. Raja Ray", "experience": "Microbiology", "rating": 4.2, "fee": 400, "available_now": True, "next_available_in_hours": 1}
            ],
            "Cardiologist": [
                {"name": "Dr. Chanchal Kundu", "experience": "Cardiology", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Rohit Kumar", "experience": "Cardiology", "rating": 4.4, "fee": 750, "available_now": False, "next_available_in_hours": 2}
            ],
            "Physiotherapist": [
                {"name": "Dr. Basudeb Dey", "experience": "Physiotherapy", "rating": 4.3, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h23",
        "name": "Apex Clinic Private Limited",
        "address": "Behala, Kolkata",
        "lat": 22.486,
        "lon": 88.303,
        "reception_number": ["+91-033-2406-8071", "+91-033-2570-2257"],
        "specialists": {
            "Urologist": [
                {"name": "Dr. Pushkar Shyam Chowdhury", "experience": "23+ years", "rating": 4.7, "fee": 900, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopedic Surgeon": [
                {"name": "Dr. Rajinder Singh Gaheer", "experience": "28+ years", "rating": 4.8, "fee": 1000, "available_now": False, "next_available_in_hours": 3}
            ],
            "Gynecologist": [
                {"name": "Dr. Subhra Das", "experience": "37+ years", "rating": 4.9, "fee": 800, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Nibedita Ray Gaheer", "experience": "26+ years", "rating": 4.7, "fee": 850, "available_now": False, "next_available_in_hours": 2}
            ],
            "Dermatologist": [
                {"name": "Dr. Shouvik Ghosh", "experience": "14+ years", "rating": 4.5, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "Psychiatrist": [
                {"name": "Dr. Madhurima Ghosh", "experience": "18+ years", "rating": 4.6, "fee": 700, "available_now": False, "next_available_in_hours": 2}
            ],
            "General Physician": [
                {"name": "Dr. Pranab Kanti Roy", "experience": "53+ years", "rating": 4.9, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Plastic Surgeon": [
                {"name": "Dr. Amitava Dasgupta", "experience": "44+ years", "rating": 4.8, "fee": 1200, "available_now": False, "next_available_in_hours": 4}
            ]
        }
    },
    {
        "id": "h24",
        "name": "UMRI Hospital",
        "address": "Barisha, Kolkata",
        "lat": 22.4782,
        "lon": 88.3129,
        "reception_number": "+91-090736-99003",
        "specialists": {
            "General Surgeon": [
                {"name": "Dr. Tarun Kumar Kundu", "experience": "15+ years", "rating": 4.5, "fee": 700, "available_now": True, "next_available_in_hours": 0}
            ],
            "Pediatric Surgeon": [
                {"name": "Dr. Tanushree Kundu", "experience": "20+ years", "rating": 4.6, "fee": 800, "available_now": False, "next_available_in_hours": 2}
            ],
            "Dentist": [
                {"name": "Dr. Anubhav Das Adhikari", "experience": "12+ years", "rating": 4.4, "fee": 500, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Available Consultant", "experience": "10+ years", "rating": 4.2, "fee": 500, "available_now": True, "next_available_in_hours": 0}
            ],
            "Cardiologist": [
                {"name": "Dr. Visiting Cardiologist", "experience": "15+ years", "rating": 4.3, "fee": 900, "available_now": False, "next_available_in_hours": 3}
            ],
            "Orthopedic": [
                {"name": "Dr. Orthopedic Specialist", "experience": "12+ years", "rating": 4.3, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Gynecologist": [
                {"name": "Dr. Gyne Specialist", "experience": "14+ years", "rating": 4.4, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "ENT Specialist": [
                {"name": "Dr. ENT Specialist", "experience": "10+ years", "rating": 4.2, "fee": 500, "available_now": False, "next_available_in_hours": 2}
            ],
            "Ophthalmologist": [
                {"name": "Dr. Eye Specialist", "experience": "11+ years", "rating": 4.3, "fee": 500, "available_now": True, "next_available_in_hours": 1}
            ],
            "Dermatologist": [
                {"name": "Dr. Skin Specialist", "experience": "13+ years", "rating": 4.4, "fee": 600, "available_now": True, "next_available_in_hours": 0}
            ],
            "Oncologist": [
                {"name": "Dr. Oncology Consultant", "experience": "18+ years", "rating": 4.5, "fee": 1000, "available_now": False, "next_available_in_hours": 4}
            ]
        }
    },
    {
        "id": "h25",
        "name": "Kasturi Das Memorial Super Speciality Hospital",
        "address": "Maheshtala, Kolkata",
        "lat": 22.52,
        "lon": 88.27,
        "reception_number": "+91-033-7120-0000",
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. A R Rahman", "experience": "18+ years", "rating": 4.5, "fee": 900, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Suman Halder", "experience": "15+ years", "rating": 4.4, "fee": 850, "available_now": False, "next_available_in_hours": 2}
            ],
            "Dermatologist": [
                {"name": "Dr. A K Mondal", "experience": "14+ years", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Sombit Chowdhury", "experience": "12+ years", "rating": 4.2, "fee": 550, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Saswati Sengupta", "experience": "13+ years", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. S Harlalka", "experience": "20+ years", "rating": 4.6, "fee": 700, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Biswaroop Mukherjee", "experience": "16+ years", "rating": 4.4, "fee": 650, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Sibayan Sarkar", "experience": "12+ years", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Surgeon": [
                {"name": "Dr. S Ahmed", "experience": "18+ years", "rating": 4.5, "fee": 900, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Arka Bandopadhyay", "experience": "15+ years", "rating": 4.4, "fee": 850, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Sumanta Dutta", "experience": "14+ years", "rating": 4.3, "fee": 800, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Sibasis Maity", "experience": "13+ years", "rating": 4.3, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopedic": [
                {"name": "Dr. Soumen Kar", "experience": "17+ years", "rating": 4.5, "fee": 900, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. R K Sinha", "experience": "20+ years", "rating": 4.6, "fee": 950, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Krishna Singh", "experience": "16+ years", "rating": 4.4, "fee": 900, "available_now": True, "next_available_in_hours": 1}
            ],
            "ENT Specialist": [
                {"name": "Dr. A K Mondal", "experience": "14+ years", "rating": 4.3, "fee": 600, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Deep Anurag", "experience": "12+ years", "rating": 4.2, "fee": 550, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Anindya Halder", "experience": "13+ years", "rating": 4.3, "fee": 600, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. S N Sharma", "experience": "18+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Trisha Das", "experience": "14+ years", "rating": 4.4, "fee": 700, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. C K Sarkar", "experience": "20+ years", "rating": 4.6, "fee": 850, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Soumen Mondal", "experience": "15+ years", "rating": 4.4, "fee": 750, "available_now": False, "next_available_in_hours": 2}
            ],
            "Pediatrician": [
                {"name": "Dr. Swastika Pal", "experience": "10+ years", "rating": 4.4, "fee": 600, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Sabyasachi Das", "experience": "12+ years", "rating": 4.3, "fee": 550, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Some Suvro Bose", "experience": "11+ years", "rating": 4.3, "fee": 550, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. P K Sharma", "experience": "15+ years", "rating": 4.5, "fee": 600, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Mukesh Vijay", "experience": "13+ years", "rating": 4.4, "fee": 600, "available_now": True, "next_available_in_hours": 1}
            ],
            "Nephrologist": [
                {"name": "Dr. Asit Mondal", "experience": "18+ years", "rating": 4.5, "fee": 900, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Abhinandan Banerjee", "experience": "14+ years", "rating": 4.4, "fee": 850, "available_now": True, "next_available_in_hours": 1}
            ]
        }
    },
    {
        "id": "h26",
        "name": "Tarangini Nursing Home",
        "address": "Behala, Kolkata",
        "lat": 22.4968,
        "lon": 88.3172,
        "reception_number": "+91-093307-07401",
        "specialists": {
            "General Physician": [
                {
                    "name": "Dr. Nazrul Islam",
                    "experience": "31+ years",
                    "rating": 4.6,
                    "fee": 400,
                    "available_now": True,
                    "next_available_in_hours": 0,
                    "special_focus": ["Piles", "Fistula", "Fissure", "Ayurvedic Treatment"]
                }
            ]
        }
    },
    {
        "id": "h27",
        "name": "BM Birla Heart Research Centre",
        "address": "Alipore, Kolkata",
        "lat": 22.5328,
        "lon": 88.3282,
        "reception_number": ["+91-080-6213-6586", "+91-080-6213-6585"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. R S Agarwal", "experience": "Cardiology", "rating": 4.6, "fee": 800, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Abhijit Aich Bhowmick", "experience": "Cardiology", "rating": 4.4, "fee": 750, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Santanu Dutta", "experience": "Cardiology", "rating": 4.3, "fee": 700, "available_now": False, "next_available_in_hours": 2}
            ]
        }
    },
    {
        "id": "h28",
        "name": "DM Hospitals Private Limited",
        "address": "Thakurpukur, Kolkata",
        "lat": 22.47,
        "lon": 88.31,
        "reception_number": ["+91-098367-29186", "+91-033-2453-6222"],
        "specialists": {
            "General Physician": [
                {"name": "Dr. Satyaki Basu", "experience": "Medicine", "rating": 4.5, "fee": 500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. M K Chaudhuri", "experience": "Internal Medicine", "rating": 4.2, "fee": 500, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Buddhadev Roy", "experience": "Internal Medicine", "rating": 4.1, "fee": 450, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Neha Karnani Agarwal", "experience": "Medicine", "rating": 4.3, "fee": 500, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Puspita Mondal", "experience": "Medicine", "rating": 4.0, "fee": 450, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h29",
        "name": "Manipal Hospitals Dhakuria",
        "address": "Dhakuria, Kolkata",
        "lat": 22.4988,
        "lon": 88.3758,
        "reception_number": "+91-033-6907-0000",
        "specialists": {
            "ENT Specialist": [
                {"name": "Dr. Anirban Sinha", "experience": "12+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Arghya Chattopadhyay", "experience": "10+ years", "rating": 4.4, "fee": 700, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h30",
        "name": "Command Hospital (Eastern Command)",
        "address": "Alipore, Kolkata",
        "lat": 22.5304,
        "lon": 88.3317,
        "reception_number": "+91-033-2479-1567",
        "specialists": {
            "Dermatologist": [
                {"name": "Dr. Manas Chatterjee", "experience": "20+ years", "rating": 4.6, "fee": 500, "available_now": False, "next_available_in_hours": 3}
            ],
            "General Physician": [
                {"name": "Dr. Amit Das", "experience": "15+ years", "rating": 4.4, "fee": 400, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h31",
        "name": "Tapan Sinha Memorial Hospital",
        "address": "Tollygunge, Kolkata",
        "lat": 22.49,
        "lon": 88.34,
        "reception_number": "+91-033-2255-4473",
        "specialists": {
            "General Physician": [
                {"name": "General Physician", "experience": "Hospital Staff", "rating": 4.0, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    }
]