from fastapi import FastAPI
from app.schemas import HeartData
import joblib
import numpy as np

app = FastAPI(title="Heart Disease Prediction API")

# Load model
model = joblib.load("model/heart_model.joblib")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def model_info():
    return {
        "model_type": str(type(model).__name__),
        "features": ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
                     "thalach", "exang", "oldpeak", "slope", "ca", "thal"]
    }

@app.post("/predict")
def predict(data: HeartData):
    features = np.array([[data.age, data.sex, data.cp, data.trestbps, data.chol,
                          data.fbs, data.restecg, data.thalach, data.exang,
                          data.oldpeak, data.slope, data.ca, data.thal]])
    prediction = model.predict(features)[0]
    return {"heart_disease": bool(prediction)}
