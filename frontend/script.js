// Configure this to your deployed backend URL (Render/Railway)
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? ''  // Use relative URLs for local development
    : 'https://your-backend-url.onrender.com';  // ← Replace with your actual deployed backend URL

document.addEventListener('DOMContentLoaded', () => {
    // Basic Navigation
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('main > section');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            navLinks.forEach(l => l.classList.remove('active'));
            sections.forEach(s => {
                s.classList.remove('active-section');
                s.classList.add('hidden-section');
            });
            
            link.classList.add('active');
            const targetId = link.getAttribute('href').substring(1);
            const targetSec = document.getElementById(targetId);
            targetSec.classList.add('active-section');
            targetSec.classList.remove('hidden-section');
            
            // Re-render map to fix sizing issue on unhide
            if(targetId === 'discovery' && map) {
                setTimeout(() => map.invalidateSize(), 100);
            }
        });
    });

    // --- State ---
    let userLocation = { lat: 22.6280, lon: 88.4360 }; // Default Chinar Park, Kolkata
    let map;
    let markersLayer = new L.LayerGroup();

    // --- Module 1 & 2: Map & Location ---
    const locationModal = document.getElementById('location-modal');
    const allowLocBtn = document.getElementById('allow-location');
    const manualLocBtn = document.getElementById('submit-manual-location');
    const manualCityInput = document.getElementById('manual-city');

    function initMap() {
        map = L.map('map').setView([userLocation.lat, userLocation.lon], 12);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);
        markersLayer.addTo(map);
        
        // Add user marker
        L.marker([userLocation.lat, userLocation.lon]).addTo(map)
            .bindPopup('Your Location').openPopup();
    }

    function hideModalAndInitMap() {
        locationModal.classList.remove('active');
        initMap();
        fetchHospitals(); // Fetch initial without specialty
    }

    allowLocBtn.addEventListener('click', () => {
        if ("geolocation" in navigator) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    userLocation = {
                        lat: position.coords.latitude,
                        lon: position.coords.longitude
                    };
                    hideModalAndInitMap();
                },
                (error) => {
                    alert("Location access denied or unavailable. Using default (NY).");
                    hideModalAndInitMap();
                }
            );
        }
    });

    manualLocBtn.addEventListener('click', () => {
        const city = manualCityInput.value;
        if(city.toLowerCase().includes('york')) {
            hideModalAndInitMap();
        } else {
            alert("For this demo, just type 'New York' or allow location.");
            hideModalAndInitMap();
        }
    });

    // --- Search & Fetch Data ---
    const searchBtn = document.getElementById('search-btn');
    const searchInput = document.getElementById('specialist-search');
    const hospitalList = document.getElementById('hospital-list');

    searchBtn.addEventListener('click', fetchHospitals);
    searchInput.addEventListener('keypress', (e) => {
        if(e.key === 'Enter') fetchHospitals();
    });

    async function fetchHospitals() {
        const specialty = searchInput.value.trim();
        hospitalList.innerHTML = `<div class="empty-state"><div class="spinner" style="margin:0 auto;"></div><p>Searching for ${specialty || 'hospitals'}...</p></div>`;
        
        try {
            const res = await fetch(`${API_BASE_URL}/api/hospitals?lat=${userLocation.lat}&lon=${userLocation.lon}&specialty=${encodeURIComponent(specialty)}`);
            const data = await res.json();
            renderHospitals(data, specialty);
        } catch(error) {
            console.error("Error fetching hospitals", error);
            hospitalList.innerHTML = `<div class="empty-state"><i class="fa-solid fa-circle-exclamation text-danger"></i><p>Failed to load data. Ensure backend is running.</p></div>`;
        }
    }

    const defaultIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    const activeIcon = new L.Icon({
        iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    function renderHospitals(hospitals, specialty) {
        hospitalList.innerHTML = '';
        markersLayer.clearLayers();
        let mapMarkers = [];

        if(hospitals.length === 0) {
            hospitalList.innerHTML = `<div class="empty-state"><i class="fa-solid fa-bed-pulse"></i><p>No hospitals found matching criteria.</p></div>`;
            return;
        }

        hospitals.forEach((h, index) => {
            // Map Marker using exact coordinates
            const marker = L.marker([h.lat, h.lon], {icon: defaultIcon});
            marker.bindPopup(`<b>${h.name}</b><br>${h.address}`);
            markersLayer.addLayer(marker);
            mapMarkers.push(marker);

            // UI Card
            const card = document.createElement('div');
            card.className = 'hospital-card';
            
            let availHtml = '';
            if(h.available_now) {
                availHtml = `<div class="availability avail-now"><div class="dot"></div> Doc Available Now</div>`;
            } else if (h.next_available_in_hours > 0) {
                availHtml = `<div class="availability avail-later"><div class="dot"></div> Available in ${h.next_available_in_hours}h</div>`;
            }

            card.innerHTML = `
                <div class="card-header">
                    <div>
                        <h3>${index + 1}. ${h.name}</h3>
                        <p style="color:var(--text-secondary); font-size:0.9rem">${h.address}</p>
                    </div>
                    <div class="dist-badge"><i class="fa-solid fa-location-arrow"></i> ${h.distance_km} km</div>
                </div>
                ${availHtml}
                <div class="card-footer">
                    <div class="phone"><i class="fa-solid fa-phone"></i> Desk: ${h.reception_number}</div>
                    <a href="tel:${h.reception_number}" class="btn-call"><i class="fa-solid fa-phone-volume"></i> Call Now</a>
                </div>
            `;
            
            card.addEventListener('click', () => {
                // Reset all markers
                mapMarkers.forEach(m => m.setIcon(defaultIcon));
                // Set active marker style
                marker.setIcon(activeIcon);
                
                // Highlight card visually
                document.querySelectorAll('.hospital-card').forEach(c => {
                    c.style.borderColor = 'var(--glass-border)';
                    c.style.background = 'var(--glass-bg)';
                });
                card.style.borderColor = 'var(--accent-primary)';
                card.style.background = 'rgba(2, 132, 199, 0.05)'; // slight tint

                map.setView(marker.getLatLng(), 14);
                marker.openPopup();
            });

            hospitalList.appendChild(card);
        });

        if(hospitals.length > 0) {
            const group = new L.featureGroup(markersLayer.getLayers());
            group.addLayer(L.marker([userLocation.lat, userLocation.lon]));
            map.fitBounds(group.getBounds().pad(0.1));
        }
    }


    // --- Module 3: Prescription AI ---
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const uploadContent = document.getElementById('upload-content');
    const analyzingContent = document.getElementById('analyzing-content');
    const analysisResults = document.getElementById('analysis-results');
    const content = document.getElementById('analysis-content');
    
    // Drag & Drop
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });
    dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        if(e.dataTransfer.files.length) {
            handleFileUpload(e.dataTransfer.files[0]);
        }
    });
    
    fileInput.addEventListener('change', (e) => {
        if(e.target.files.length) {
            handleFileUpload(e.target.files[0]);
        }
    });

    async function handleFileUpload(file) {
        // Switch to analyzing state
        uploadContent.classList.add('hidden');
        analyzingContent.classList.remove('hidden');
        analysisResults.classList.add('hidden');
        dropZone.classList.add('analyzing');
        dropZone.classList.remove('has-results');

        const formData = new FormData();
        formData.append('file', file);

        try {
            const res = await fetch(`${API_BASE_URL}/api/analyze-prescription`, {
                method: 'POST',
                body: formData
            });

            const data = await res.json();
            
            if(data.error) throw new Error(data.error);
            
            renderPrescriptionData(data);

            // Switch to results state
            analyzingContent.classList.add('hidden');
            analysisResults.classList.remove('hidden');
            dropZone.classList.remove('analyzing');
            dropZone.classList.add('has-results');
            
        } catch (err) {
            console.error(err);
            alert("Error analyzing prescription: " + err.message);
            // Reset back to upload state
            analyzingContent.classList.add('hidden');
            uploadContent.classList.remove('hidden');
            dropZone.classList.remove('analyzing');
            dropZone.classList.remove('has-results');
        } finally {
            fileInput.value = ''; // reset
        }
    }

    function renderPrescriptionData(data) {
        const diseaseSummary = document.getElementById('disease-summary');
        const medList = document.getElementById('medicines-list');
        const warningList = document.getElementById('warnings-list');

        diseaseSummary.innerHTML = '';
        if(data.disease_summary) {
            diseaseSummary.innerHTML = `<h4><i class="fa-solid fa-stethoscope"></i> Suspected Diagnosis:</h4><p>${data.disease_summary}</p>`;
        }

        medList.innerHTML = '';
        if(data.medicines && data.medicines.length > 0) {
            data.medicines.forEach(m => {
                medList.innerHTML += `
                    <div class="med-item">
                        <strong>${m.name}</strong>
                        <div><i class="fa-solid fa-pills" style="color:var(--text-secondary)"></i> Dosage: ${m.dosage || 'N/A'}</div>
                        <div><i class="fa-solid fa-clock-rotate-left" style="color:var(--text-secondary)"></i> Frequency: ${m.frequency || 'N/A'}</div>
                        <div><i class="fa-regular fa-calendar" style="color:var(--text-secondary)"></i> Duration: ${m.duration || 'N/A'}</div>
                    </div>
                `;
            });
        } else {
            medList.innerHTML = '<p>No medicines found.</p>';
        }

        warningList.innerHTML = '';
        if(data.warnings && data.warnings.length > 0) {
            data.warnings.forEach(w => {
                warningList.innerHTML += `<li>${w}</li>`;
            });
        } else {
            warningList.innerHTML = '<li>No specific warnings.</li>';
        }
    }
});
