# 😊 Smile for Attendance 👀
### Face Authentication Based Attendance System

A real-time face authentication attendance system built using **Python, OpenCV, and Streamlit**.  
The project allows students to register their face, punch in, and punch out using a live camera feed, with attendance automatically logged in a CSV file.

This project focuses on **practical usability**, **clean UI**, and **real-world constraints** such as lighting variations and state handling.

---

## 📌 Features

- 📸 Face registration using live camera
- 🧠 Face recognition using LBPH algorithm
- 🕒 Punch In / Punch Out attendance system
- 👥 Multiple student support
- 📄 Attendance stored in CSV format
- 🎨 Streamlit-based aesthetic and interactive UI
- 🔁 Real-time updates without restarting the app
- ⚠️ Basic spoof prevention via live camera input

---

## 🛠️ Tech Stack

| Category | Tools / Libraries |
|--------|------------------|
| Language | Python |
| Computer Vision | OpenCV |
| Face Recognition | LBPH |
| Frontend | Streamlit |
| Data Handling | Pandas, CSV |

---

## 📁 Project Structure

```text
Face-Authentication-Attendance-System/
│
├── app.py
├── face_detection.py
├── face_registration.py
├── face_recognition.py
├── attendance.csv
├── dataset/   (ignored in GitHub)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Streamlit app
```bash
python -m streamlit run app.py
```

---


## 🔮 Future Improvements

- Eye-blink / liveness detection
- Database integration
- Admin dashboard
- Export attendance reports

---


