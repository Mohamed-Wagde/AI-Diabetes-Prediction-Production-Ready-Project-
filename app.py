from fastapi import FastAPI, HTTPException
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("models/model.pkl")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(data: dict):
    try:
        age = data.get("age")
        bmi = data.get("bmi")
        glucose = data.get("glucose")

        if age is None or bmi is None or glucose is None:
            raise HTTPException(status_code=400, detail="Missing input values")

        if age <= 0 or bmi <= 0 or glucose <= 0:
            raise HTTPException(status_code=400, detail="Invalid values")

        features = np.array([[age, bmi, glucose]])
        prediction = model.predict(features)[0]

        return {"prediction": int(prediction)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
