# House_price_prediction
A full-stack Machine Learning project that predicts house prices using a trained model, deployed with a modern UI and API.

# 🏠 House Price Prediction System

A full-stack Machine Learning project that predicts house prices using a trained model, deployed with a modern UI and API.

---

## 🚀 Live Demo

- Frontend: https://your-vercel-link.vercel.app
- Backend API: https://your-render-link.onrender.com

---

## 📌 Features

- 🔹 Single house price prediction
- 🔹 Bulk prediction using CSV upload
- 🔹 Download predictions as CSV
- 🔹 Interactive chart (Predicted vs Average Price)
- 🔹 FastAPI backend with Swagger UI
- 🔹 Clean and responsive Next.js frontend

---

## 🧠 Tech Stack

### Backend
- FastAPI
- Scikit-learn
- Pandas
- NumPy

### Frontend
- Next.js
- Axios
- Recharts

### Deployment
- Render (Backend)
- Vercel (Frontend)

---

## 📊 Screenshots

### UI
![UI](screenshots/ui.png)

### Prediction
![Prediction](screenshots/prediction.png)

### Chart
![Chart](screenshots/chart.png)

### CSV Upload
![CSV](screenshots/csv_upload.png)

### Swagger API
![Swagger](screenshots/swagger.png)

---

## ⚙️ Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
