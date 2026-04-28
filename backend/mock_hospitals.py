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


    # ─── CHINAR PARK / NEW TOWN AREA (3 Hospitals) ───

    {
        "id": "h32",
        "name": "AMRI Hospitals - Salt Lake",
        "address": "Block A, Salt Lake City, Near Chinar Park, Kolkata",
        "lat": 22.5863,
        "lon": 88.4132,
        "reception_number": ["+91-033-6606-3800", "+91-033-6606-3801"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Arindam Pande", "experience": "22+ years", "rating": 4.7, "fee": 1200, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Suvro Banerjee", "experience": "18+ years", "rating": 4.5, "fee": 1000, "available_now": False, "next_available_in_hours": 2}
            ],
            "Neurologist": [
                {"name": "Dr. Amitabha Ghosh", "experience": "25+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Suparna Ganguly", "experience": "16+ years", "rating": 4.4, "fee": 1000, "available_now": False, "next_available_in_hours": 3}
            ],
            "Orthopaedic": [
                {"name": "Dr. Debashis Roy", "experience": "20+ years", "rating": 4.6, "fee": 1100, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Kaushik Bhattacharya", "experience": "15+ years", "rating": 4.3, "fee": 900, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Physician": [
                {"name": "Dr. Subhasis Roychowdhury", "experience": "28+ years", "rating": 4.7, "fee": 800, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Anindita Sinha", "experience": "14+ years", "rating": 4.3, "fee": 600, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Mahesh Goenka", "experience": "30+ years", "rating": 4.9, "fee": 1500, "available_now": False, "next_available_in_hours": 4}
            ],
            "Gynecologist": [
                {"name": "Dr. Rinku Sengupta Dhar", "experience": "20+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "Pulmonologist": [
                {"name": "Dr. Raja Dhar", "experience": "24+ years", "rating": 4.8, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "Dermatologist": [
                {"name": "Dr. Saumya Panda", "experience": "19+ years", "rating": 4.5, "fee": 800, "available_now": False, "next_available_in_hours": 2}
            ]
        }
    },
    {
        "id": "h33",
        "name": "Tata Medical Center",
        "address": "14 Major Arterial Road, New Town, Near Chinar Park, Kolkata",
        "lat": 22.5920,
        "lon": 88.4678,
        "reception_number": ["+91-033-6605-7000", "+91-033-6605-7011"],
        "specialists": {
            "Oncologist": [
                {"name": "Dr. Mammen Chandy", "experience": "35+ years", "rating": 4.9, "fee": 2000, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Sanjit Agrawal", "experience": "22+ years", "rating": 4.7, "fee": 1800, "available_now": False, "next_available_in_hours": 3},
                {"name": "Dr. Deepak Dabkara", "experience": "16+ years", "rating": 4.5, "fee": 1500, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Surgeon": [
                {"name": "Dr. Gaurav Das", "experience": "18+ years", "rating": 4.6, "fee": 1200, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Saugata Sen", "experience": "20+ years", "rating": 4.7, "fee": 1400, "available_now": False, "next_available_in_hours": 2}
            ],
            "Radiologist": [
                {"name": "Dr. Sanjoy Chatterjee", "experience": "25+ years", "rating": 4.8, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Arnab Gupta", "experience": "20+ years", "rating": 4.6, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Pediatrician": [
                {"name": "Dr. Shekhar Krishnan", "experience": "22+ years", "rating": 4.7, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Hematologist": [
                {"name": "Dr. Reena Nair", "experience": "18+ years", "rating": 4.6, "fee": 1500, "available_now": True, "next_available_in_hours": 1}
            ]
        }
    },
    {
        "id": "h34",
        "name": "Charnock Hospital",
        "address": "Chinar Park, New Town, Rajarhat, Kolkata",
        "lat": 22.6260,
        "lon": 88.4354,
        "reception_number": ["+91-033-4040-5000", "+91-098300-54321"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Soumitra Kumar", "experience": "26+ years", "rating": 4.7, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Physician": [
                {"name": "Dr. Partha Pratim Dey", "experience": "18+ years", "rating": 4.5, "fee": 700, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Snigdha Patra", "experience": "12+ years", "rating": 4.3, "fee": 600, "available_now": False, "next_available_in_hours": 2}
            ],
            "Orthopaedic": [
                {"name": "Dr. Suman Kundu", "experience": "20+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Rana Das", "experience": "14+ years", "rating": 4.3, "fee": 800, "available_now": False, "next_available_in_hours": 3}
            ],
            "Gynecologist": [
                {"name": "Dr. Kakali Ghosh Dastidar", "experience": "22+ years", "rating": 4.6, "fee": 900, "available_now": True, "next_available_in_hours": 0}
            ],
            "Urologist": [
                {"name": "Dr. Nilanjan Mitra", "experience": "17+ years", "rating": 4.5, "fee": 1000, "available_now": False, "next_available_in_hours": 2}
            ],
            "ENT Specialist": [
                {"name": "Dr. Bivas Adhikary", "experience": "15+ years", "rating": 4.4, "fee": 700, "available_now": True, "next_available_in_hours": 1}
            ],
            "Dermatologist": [
                {"name": "Dr. Anupama Ghosh", "experience": "16+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Pediatrician": [
                {"name": "Dr. Tapas Kumar Sabui", "experience": "24+ years", "rating": 4.6, "fee": 800, "available_now": False, "next_available_in_hours": 2}
            ]
        }
    },

    # ─── ACROSS KOLKATA (12 Hospitals) ───

    {
        "id": "h35",
        "name": "Apollo Gleneagles Hospital",
        "address": "58 Canal Circular Road, Kadapara, Phool Bagan, Kolkata",
        "lat": 22.5726,
        "lon": 88.3990,
        "reception_number": ["+91-033-2320-3040", "+91-033-2320-2122"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Anil Mishra", "experience": "30+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Aftab Khan", "experience": "22+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Neurologist": [
                {"name": "Dr. Jayanta Roy", "experience": "28+ years", "rating": 4.7, "fee": 1400, "available_now": True, "next_available_in_hours": 1}
            ],
            "Nephrologist": [
                {"name": "Dr. Dilip Kumar Pahari", "experience": "25+ years", "rating": 4.7, "fee": 1300, "available_now": False, "next_available_in_hours": 3}
            ],
            "General Surgeon": [
                {"name": "Dr. Debasish Banerjee", "experience": "26+ years", "rating": 4.6, "fee": 1200, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Shoubhik Das Gupta", "experience": "18+ years", "rating": 4.4, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopaedic": [
                {"name": "Dr. Arijit Chattopadhyay", "experience": "22+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gynecologist": [
                {"name": "Dr. Gita Ganguly Mukherjee", "experience": "32+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Joydeep Ghosh", "experience": "20+ years", "rating": 4.5, "fee": 1200, "available_now": True, "next_available_in_hours": 1}
            ],
            "Pulmonologist": [
                {"name": "Dr. Arup Kumar Halder", "experience": "18+ years", "rating": 4.4, "fee": 1000, "available_now": False, "next_available_in_hours": 2}
            ],
            "General Physician": [
                {"name": "Dr. Kushal Nag", "experience": "20+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h36",
        "name": "SSKM Hospital (PG Hospital)",
        "address": "244 AJC Bose Road, Bhowanipore, Kolkata",
        "lat": 22.5371,
        "lon": 88.3430,
        "reception_number": ["+91-033-2223-4567", "+91-033-2223-5678"],
        "specialists": {
            "General Physician": [
                {"name": "Dr. Apurba Ghosh", "experience": "30+ years", "rating": 4.7, "fee": 200, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Mrinmoy Das", "experience": "22+ years", "rating": 4.5, "fee": 200, "available_now": True, "next_available_in_hours": 1}
            ],
            "Cardiologist": [
                {"name": "Dr. Ratan Kumar Datta", "experience": "28+ years", "rating": 4.7, "fee": 300, "available_now": False, "next_available_in_hours": 2}
            ],
            "Neurologist": [
                {"name": "Dr. Shankar Prasad Saha", "experience": "35+ years", "rating": 4.8, "fee": 300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Orthopaedic": [
                {"name": "Dr. Dibyendu Saha", "experience": "24+ years", "rating": 4.6, "fee": 250, "available_now": True, "next_available_in_hours": 1},
                {"name": "Dr. Goutam Guha", "experience": "20+ years", "rating": 4.5, "fee": 250, "available_now": False, "next_available_in_hours": 3}
            ],
            "Nephrologist": [
                {"name": "Dr. Dipankar Sircar", "experience": "20+ years", "rating": 4.5, "fee": 250, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Surgeon": [
                {"name": "Dr. Somak Das", "experience": "25+ years", "rating": 4.6, "fee": 300, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gynecologist": [
                {"name": "Dr. Sudipta Banerjee", "experience": "22+ years", "rating": 4.5, "fee": 250, "available_now": True, "next_available_in_hours": 1}
            ],
            "Pediatrician": [
                {"name": "Dr. Jaydeep Choudhury", "experience": "26+ years", "rating": 4.7, "fee": 250, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h37",
        "name": "Fortis Hospital Anandapur",
        "address": "730 EM Bypass, Anandapur, Kolkata",
        "lat": 22.5110,
        "lon": 88.3970,
        "reception_number": ["+91-033-6628-4444", "+91-033-6628-4445"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Kunal Sarkar", "experience": "30+ years", "rating": 4.9, "fee": 2000, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Rabin Chakraborty", "experience": "25+ years", "rating": 4.7, "fee": 1500, "available_now": False, "next_available_in_hours": 2}
            ],
            "Neurologist": [
                {"name": "Dr. Ambar Chakravarty", "experience": "32+ years", "rating": 4.8, "fee": 1800, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopaedic": [
                {"name": "Dr. Partha Pratim Das", "experience": "20+ years", "rating": 4.6, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Aniruddha Pratap Singh", "experience": "18+ years", "rating": 4.5, "fee": 1200, "available_now": False, "next_available_in_hours": 3}
            ],
            "General Surgeon": [
                {"name": "Dr. Somnath Chattopadhyay", "experience": "24+ years", "rating": 4.7, "fee": 1500, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Subhash Ranjan Dutta", "experience": "22+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Indrani Lodh", "experience": "20+ years", "rating": 4.5, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Urologist": [
                {"name": "Dr. Santosh Kumar Mandal", "experience": "22+ years", "rating": 4.6, "fee": 1300, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h40",
        "name": "Ruby General Hospital",
        "address": "576 Anandapur, EM Bypass, Kasba, Kolkata",
        "lat": 22.5180,
        "lon": 88.3920,
        "reception_number": ["+91-033-6609-4444", "+91-033-6609-4445"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. S B Roy", "experience": "25+ years", "rating": 4.6, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "Orthopaedic": [
                {"name": "Dr. K K Sharma", "experience": "28+ years", "rating": 4.7, "fee": 1300, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Raman Haldar", "experience": "18+ years", "rating": 4.5, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Physician": [
                {"name": "Dr. Kushal Bandyopadhyay", "experience": "22+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Shila Mitra", "experience": "26+ years", "rating": 4.7, "fee": 1200, "available_now": True, "next_available_in_hours": 1}
            ],
            "Neurologist": [
                {"name": "Dr. Asim Kumar Maji", "experience": "20+ years", "rating": 4.5, "fee": 1100, "available_now": False, "next_available_in_hours": 3}
            ],
            "Pediatrician": [
                {"name": "Dr. Subroto Dagupta", "experience": "24+ years", "rating": 4.6, "fee": 900, "available_now": True, "next_available_in_hours": 0}
            ],
            "ENT Specialist": [
                {"name": "Dr. Rupa Mukherjee", "experience": "16+ years", "rating": 4.4, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "General Surgeon": [
                {"name": "Dr. Amal Ranjan Das", "experience": "30+ years", "rating": 4.7, "fee": 1400, "available_now": False, "next_available_in_hours": 2}
            ]
        }
    },
    {
        "id": "h41",
        "name": "Peerless Hospital & B.K. Roy Research Centre",
        "address": "360 Panchasayar, Gariahat, Kolkata",
        "lat": 22.5020,
        "lon": 88.3690,
        "reception_number": ["+91-033-4011-2222", "+91-033-4011-2200"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Amal Kumar Banerjee", "experience": "32+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Ranjan Kanti Shen", "experience": "24+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Gopal Krishna Dhali", "experience": "28+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 1}
            ],
            "Neurologist": [
                {"name": "Dr. Ashis Kumar Saha", "experience": "26+ years", "rating": 4.7, "fee": 1300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Orthopaedic": [
                {"name": "Dr. Asit Baran Adhya", "experience": "30+ years", "rating": 4.7, "fee": 1200, "available_now": False, "next_available_in_hours": 3}
            ],
            "General Physician": [
                {"name": "Dr. Saroj Kanti Das", "experience": "25+ years", "rating": 4.6, "fee": 800, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Srabani Mukhopadhyay", "experience": "22+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "Dermatologist": [
                {"name": "Dr. Bikash Ranjan Kar", "experience": "18+ years", "rating": 4.5, "fee": 800, "available_now": False, "next_available_in_hours": 2}
            ],
            "Psychiatrist": [
                {"name": "Dr. Jay Ranjan Ram", "experience": "20+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h43",
        "name": "Woodland Hospital",
        "address": "8/5 Alipore Road, Alipore, Kolkata",
        "lat": 22.5340,
        "lon": 88.3370,
        "reception_number": ["+91-033-4050-7070", "+91-033-4050-7071"],
        "specialists": {
            "General Physician": [
                {"name": "Dr. Sukumar Mukherjee", "experience": "40+ years", "rating": 4.9, "fee": 1500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Arindam Biswas", "experience": "18+ years", "rating": 4.5, "fee": 800, "available_now": True, "next_available_in_hours": 1}
            ],
            "Cardiologist": [
                {"name": "Dr. Soumitra Mondal", "experience": "22+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Rajiv Sarkar", "experience": "20+ years", "rating": 4.5, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Mohua Sen", "experience": "24+ years", "rating": 4.6, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopaedic": [
                {"name": "Dr. Rajat Basu", "experience": "22+ years", "rating": 4.6, "fee": 1100, "available_now": False, "next_available_in_hours": 3}
            ],
            "Dermatologist": [
                {"name": "Dr. Abir Saraswati", "experience": "14+ years", "rating": 4.4, "fee": 700, "available_now": True, "next_available_in_hours": 0}
            ]
        }
    },
    {
        "id": "h44",
        "name": "Narayana Superspecialty Hospital",
        "address": "120/1 Andul Road, Howrah, Kolkata",
        "lat": 22.5760,
        "lon": 88.2920,
        "reception_number": ["+91-033-7122-0000", "+91-1800-102-6000"],
        "specialists": {
            "Cardiologist": [
                {"name": "Dr. Devi Prasad Shetty", "experience": "35+ years", "rating": 4.9, "fee": 2000, "available_now": False, "next_available_in_hours": 5},
                {"name": "Dr. Ajay Kaul", "experience": "28+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0}
            ],
            "Neurologist": [
                {"name": "Dr. Rana Saha", "experience": "20+ years", "rating": 4.6, "fee": 1200, "available_now": True, "next_available_in_hours": 1}
            ],
            "Nephrologist": [
                {"name": "Dr. Arup Ratan Dutta", "experience": "22+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "General Surgeon": [
                {"name": "Dr. Tapas Sarkar", "experience": "24+ years", "rating": 4.7, "fee": 1300, "available_now": True, "next_available_in_hours": 0}
            ],
            "Orthopaedic": [
                {"name": "Dr. Pradeep Kumar Neogi", "experience": "20+ years", "rating": 4.5, "fee": 1100, "available_now": True, "next_available_in_hours": 1}
            ],
            "Pediatrician": [
                {"name": "Dr. Sumantra Raut", "experience": "18+ years", "rating": 4.5, "fee": 900, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Physician": [
                {"name": "Dr. Mihir Sarkar", "experience": "22+ years", "rating": 4.5, "fee": 800, "available_now": False, "next_available_in_hours": 2}
            ],
            "Gynecologist": [
                {"name": "Dr. Sharmila Sehgal", "experience": "26+ years", "rating": 4.7, "fee": 1200, "available_now": True, "next_available_in_hours": 1}
            ]
        }
    },
    {
        "id": "h45",
        "name": "Belle Vue Clinic",
        "address": "9 Dr. U. N. Brahmachari Street, Ballygunge, Kolkata",
        "lat": 22.5380,
        "lon": 88.3580,
        "reception_number": ["+91-033-4039-8888", "+91-033-4039-8889"],
        "specialists": {
            "General Physician": [
                {"name": "Dr. Sudarshan Ballav", "experience": "30+ years", "rating": 4.8, "fee": 1500, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Amal Dasgupta", "experience": "20+ years", "rating": 4.5, "fee": 1000, "available_now": True, "next_available_in_hours": 1}
            ],
            "Cardiologist": [
                {"name": "Dr. Sabyasachi Mitra", "experience": "24+ years", "rating": 4.7, "fee": 1500, "available_now": False, "next_available_in_hours": 2}
            ],
            "Orthopaedic": [
                {"name": "Dr. Tarun Kumar Dutta", "experience": "28+ years", "rating": 4.7, "fee": 1300, "available_now": True, "next_available_in_hours": 1}
            ],
            "Gastroenterologist": [
                {"name": "Dr. Kshitiz Murdia", "experience": "18+ years", "rating": 4.5, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "Gynecologist": [
                {"name": "Dr. Kaushiki Dwivedee", "experience": "22+ years", "rating": 4.6, "fee": 1200, "available_now": False, "next_available_in_hours": 2}
            ],
            "Dermatologist": [
                {"name": "Dr. Sanjay Ghosh", "experience": "16+ years", "rating": 4.4, "fee": 900, "available_now": True, "next_available_in_hours": 0}
            ],
            "Psychiatrist": [
                {"name": "Dr. Jai Ranjan Ram", "experience": "26+ years", "rating": 4.7, "fee": 1500, "available_now": True, "next_available_in_hours": 1}
            ]
        }
    },
    {
        "id": "h46",
        "name": "Institute of Neurosciences Kolkata",
        "address": "185/1 AJC Bose Road, Park Circus, Kolkata",
        "lat": 22.5420,
        "lon": 88.3610,
        "reception_number": ["+91-033-4020-6363", "+91-033-4020-6364"],
        "specialists": {
            "Neurologist": [
                {"name": "Dr. Hashi Ghosh", "experience": "30+ years", "rating": 4.9, "fee": 2000, "available_now": True, "next_available_in_hours": 0},
                {"name": "Dr. Suparna Sen", "experience": "22+ years", "rating": 4.7, "fee": 1500, "available_now": False, "next_available_in_hours": 2},
                {"name": "Dr. Baisali Sarkar", "experience": "16+ years", "rating": 4.5, "fee": 1200, "available_now": True, "next_available_in_hours": 1}
            ],
            "Psychiatrist": [
                {"name": "Dr. Sujit Kumar Kar", "experience": "18+ years", "rating": 4.5, "fee": 1200, "available_now": True, "next_available_in_hours": 0}
            ],
            "General Physician": [
                {"name": "Dr. Bikash Lal Saha", "experience": "24+ years", "rating": 4.6, "fee": 900, "available_now": True, "next_available_in_hours": 1}
            ],
            "Orthopaedic": [
                {"name": "Dr. Debraj Shyam", "experience": "20+ years", "rating": 4.5, "fee": 1100, "available_now": False, "next_available_in_hours": 3}
            ]
        }
    }
]