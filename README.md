# 🧠 AI Diabetes Prediction System

## 📌 Overview

This project is a production-ready machine learning system that predicts
the likelihood of diabetes based on patient health data. It includes a
complete pipeline with data preprocessing, model training, a REST API,
and a simple frontend interface.

------------------------------------------------------------------------

## 🏗️ Project Structure

    AI-Diabetes-Prediction/
    │
    ├── api/                # FastAPI backend
    │   └── app.py
    │
    ├── frontend/           # Simple UI
    │   └── index.html
    │
    ├── data/               # Dataset
    │   └── diabetes_prediction_dataset.csv
    │
    ├── src/                # Core logic
    │   ├── data_preprocessing.py
    │   ├── model.py
    │   └── utils.py
    │
    ├── models/             # Saved models
    │   └── model.pkl
    │
    ├── main.py             # Training script
    ├── requirements.txt
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Project

### 1. Start API Server

``` bash
uvicorn api.app:app --reload
```

API will run on:

    http://127.0.0.1:8000

------------------------------------------------------------------------

### 2. Open Frontend

Open:

    frontend/index.html

------------------------------------------------------------------------

## 🔌 API Usage

### Endpoint:

    POST /predict

### Example Input:

``` json
{
  "age": 45,
  "bmi": 28.5,
  "glucose": 130
}
```

### Example Output:

``` json
{
  "prediction": 1
}
```

------------------------------------------------------------------------

## 🧪 Model Details

-   Algorithm: Random Forest
-   Type: Binary Classification
-   Target: Diabetes (0 = No, 1 = Yes)

------------------------------------------------------------------------

## 🚀 Deployment

### Backend:

-   Render
-   Railway

### Frontend:

-   GitHub Pages

------------------------------------------------------------------------

## 📊 Future Improvements

-   Add model evaluation metrics (F1-score, ROC)
-   Improve feature engineering
-   Add authentication
-   Deploy full-stack app

------------------------------------------------------------------------

## 📄 License

MIT License
