# 🏠 House Price Prediction System (Full Stack ML Project)

## 🚀 Overview

This project is a full-stack machine learning application that predicts house prices based on property features.

It integrates:

* Machine Learning model
* Backend API
* Interactive frontend dashboard

---

## 🧠 Tech Stack

### Backend

* Python
* FastAPI
* Pandas, NumPy
* Scikit-learn

### Frontend

* Next.js (App Router)
* Tailwind CSS
* Recharts (Data Visualization)

---

## ⚙️ Features

* 📂 Upload CSV dataset
* 🤖 Predict house prices using trained ML model
* 📊 Interactive charts (Line + Bar)
* 📋 Tabular data display
* ⬇️ Download predictions as CSV
* 🌙 Clean dark dashboard UI

---

## 📊 Demo Workflow

1. Upload CSV file
2. Backend processes data
3. Model generates predictions
4. Results displayed in UI with charts
5. Option to download predictions

---

## 🖼️ Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Charts

![Charts](screenshots/chart.png)

---

## 🛠️ Installation

### 1. Clone repo

```bash
git clone https://github.com/yourusername/house-price-ml.git
cd house-price-ml
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## 🌐 API Endpoints

| Endpoint       | Method | Description         |
| -------------- | ------ | ------------------- |
| `/predict`     | POST   | Single prediction   |
| `/predict-csv` | POST   | Bulk CSV prediction |

---

## 📈 Future Improvements

* Model optimization
* Deployment vercel
* Authentication system
* Real-time analytics dashboard

---

## 👨‍💻 Author

Nikhil
Engineering Student | AI/ML Enthusiast
