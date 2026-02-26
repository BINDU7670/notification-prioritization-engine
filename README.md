🚀 AI-Native Notification Prioritization Engine

A FastAPI-based backend system that intelligently classifies incoming notifications into:

🔥 Now  
⏳ Later  
❌ Never  

The system evaluates notifications using priority scoring, deduplication logic, and rule-based decision processing.

💡 Why This Project?

Modern applications generate thousands of notifications daily.  
This project demonstrates how backend systems can intelligently prioritize alerts to reduce noise and improve user productivity.

It simulates a real-world notification processing engine using scoring logic, deduplication strategies, and rule-based decision systems.

🧠 How It Works

1. Incoming notifications are received via API.
2. The system checks for duplicate messages.
3. A priority score is calculated.
4. Rule-based logic classifies the notification into:
   - Now
   - Later
   - Never

📌 Features

- Notification classification (Now / Later / Never)
- Priority scoring engine
- Deduplication support
- Rule-based decision engine
- REST API using FastAPI
- Interactive Swagger documentation
- Clean modular architecture

🏗️ Project Structure

notification-prioritization-engine/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── rule_engine.py
│   ├── decision_engine.py
│   └── dedupe.py
│
├── requirements.txt
└── README.md

⚙️ Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Git & GitHub

 ▶️ How to Run Locally

1. Clone the repository

git clone https://github.com/BINDU7670/notification-prioritization-engine.git
cd notification-prioritization-engine.

2. Install dependencies

pip install -r requirements.txt

 3. Run the server
    
uvicorn app.main:app --reload

Server runs at:

http://127.0.0.1:8000

Swagger docs available at:

http://127.0.0.1:8000/docs

🧪 Example API Request

POST `/evaluate`

```json
{
  "user_id": "user1",
  "event_type": "alert",
  "message": "Payment failed",
  "source": "billing",
  "priority_hint": 0.8,
  "timestamp": "2026-02-26T18:00:00",
  "channel": "push"
}
```
Example Response

```json
{
  "decision": "Now",
  "reason": "High priority score"
}
```

---

Use Cases

- E-commerce platforms  
- FinTech systems  
- Enterprise alert systems  
- AI-driven notification filtering  

 👩‍💻 Author

Bindu Shree  
GitHub: https://github.com/BINDU7670

📄 License

This project is created for educational and demonstration purposes.

