# KPRHX1170
### CODE X's Thief monitoring using AI and Face Recognition.

# 🚨 Advanced Surveillance Policing System (ASPS)

An AI-powered surveillance and crime analysis platform for real-time object detection, facial recognition, smart alerts, and criminal network mapping. Designed to support law enforcement in enhancing public safety and enabling rapid, data-driven response.

---

## 📌 Key Features

- **🔍 Real-time Object Detection**
  - Detects weapons (guns, knives), fights, falls, crashes, and suspicious behaviors.
  - Model: [YOLOv8](https://github.com/ultralytics/ultralytics) trained with custom and Roboflow-augmented datasets.

- **🧠 Real-time Facial Recognition**
  - Identifies known suspects from live CCTV feeds.
  - Models: ArcFace for embedding, RetinaFace for detection, FAISS/Milvus for real-time retrieval.

- **🧬 Graph-Based Crime Network Analysis**
  - Tracks links between suspects, locations, and events.
  - Powered by Neo4j or NetworkX for visual queries and analysis.

- **🚨 Smart Alerting System**
  - Multi-channel alerts for weapons, fights, accidents, and suspect recognition.
  - Supports SMS (Twilio), Email, and dashboard notifications.

- **📼 Forensic Video Analysis**
  - Upload & analyze historical footage for automated tagging and matching.

- **📁 Evidence Management**
  - Organized and secure storage of video evidence, detection frames, and metadata.
  - MongoDB GridFS (media), PostgreSQL (metadata).

- **📊 Predictive Crime Analytics** *(Future Scope)*
  - Analyze historical crime data to predict high-risk zones and behavioral patterns.

---

## 🧱 Tech Stack

|    Layer   |              Technology             |
|------------|-------------------------------------|
| Backend    | Flask + FastAPI Microservices       |
| Frontend   | HTML/CSS/JS (or React - optional)   |
| AI Models  | YOLOv8, Retina Face                 |
| Databases  | MongoDB                             |
| Tools      | Roboflow, TensorFlow                |
| Deployment | Docker, Gunicorn, Nginx (optional)  |

---

## 🚀 Deployment Guide (Flask)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/advanced-surveillance-system.git
cd advanced-surveillance-system
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_APP=app.py
FLASK_ENV=production
SECRET_KEY=your-secret-key

# Twilio for Alerts
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_PHONE_NUMBER=+1234567890

# Neo4j Credentials
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

### 5. Run the Flask Server

```bash
flask run
```

---

## 🎯 Roadmap

- ✅ Real-time surveillance detection
- ✅ Facial recognition and matching
- ✅ Graph-based crime network visualization
- ✅ SMS/Email alert integration
- 🔜 Predictive analytics engine
- 🔜 Dashboard UI with live feed monitoring

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss proposed changes.

---

## 📧 Contact

**Project Maintainers':** Santhosh I, Vinu Karthick D, Natarajan V, Deepak K M and Srishanth P M.

**Email:** sandytamizhan2006@gmial.com, vinukarthick6@gmail.com, vnadarajan15@gmail.com, kmariandeepak@gamil.com and srishanth232007@gmail.com 


