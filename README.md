# AI Threat Detection System (Dockerized Microservices)

A containerized AI-powered threat detection system built using Flask, MySQL, and Docker Compose.  
This project demonstrates microservices architecture, container networking, database persistence, and REST API integration.

---

## 🧠 System Architecture

User → ML Service → MySQL Database → Dashboard

### Components

- **ML Service**
  - REST API built with Flask
  - Analyzes logs
  - Classifies as `attack` or `normal`
  - Stores results in MySQL

- **Database**
  - MySQL 8
  - Persistent Docker volume
  - Stores alert logs and predictions

- **Dashboard**
  - Flask web interface
  - Fetches alerts from database
  - Displays stored threat logs

---

## 🏗 Tech Stack

- Python (Flask)
- MySQL 8
- Docker & Docker Compose
- REST API
- Microservices Architecture
- SSH-based GitHub authentication

---

## 📂 Project Structure

```
ai-threat-detection/
├── docker-compose.yml
├── README.md
│
├── ml-service/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── dashboard/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│
└── .gitignore
```

---

## 🚀 How To Run

### 1️⃣ Clone Repository

```bash
git clone git@github.com:abhijitkar10/ai-threat-detection.git
cd ai-threat-detection
```

---

### 2️⃣ Build and Start Containers

```bash
docker compose up --build
```

To run in background:

```bash
docker compose up --build -d
```

---

## 🔍 Services

| Service     | Port  | Description |
|------------|-------|-------------|
| ML Service | 8000  | Log analysis API |
| Dashboard  | 5050  | Web dashboard |
| MySQL      | 3307  | Database |

---

## 📡 Test ML API

Send a test log:

```bash
curl -X POST http://localhost:8000/analyze \
-H "Content-Type: application/json" \
-d '{"log":"failed login attempt from 192.168.1.5"}'
```

Response:

```json
{"prediction":"attack"}
```

---

## 🖥 Access Dashboard

Open in browser:

```
http://localhost:5050
```

Refresh page to see stored alerts.

---

## 💾 Data Persistence

MySQL uses a Docker named volume:

```
mysql_data:/var/lib/mysql
```

This ensures data is preserved even if containers are restarted.

---

## 🔐 Git Setup

This project uses SSH authentication for secure GitHub access.

---

## 🛠 Future Improvements

- Replace rule-based detection with trained ML model (scikit-learn)
- Add authentication to dashboard
- Implement real-time auto-refresh
- Add logging and monitoring
- Deploy to cloud (AWS / Azure)

---

## 📌 Resume Description

Built a Dockerized microservice-based AI threat detection system using Flask and MySQL with persistent containerized storage and REST API integration.

---

## 📄 License

MIT
