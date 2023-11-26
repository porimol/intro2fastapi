from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('intro2fastapi/models/california_trained_model.pkl')

class HouseFeatures(BaseModel):
    # Include features from the California Housing dataset
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

def get_input_data(features: HouseFeatures):
    return np.array(list(features.dict().values())).reshape(1, -1)

def predict_price(input_data):
    return model.predict(input_data)

@app.get("/")
def home():
    return {
        "message": "Welcome to the California Housing Price Prediction API. Use POST /predict/ endpoint for predictions."
    }

@app.post("/predict")
def predict(features: HouseFeatures):
    input_data = get_input_data(features)
    prediction = predict_price(input_data)
    pred_rsp = {
        "predicted_price": prediction[0]
    }
    return pred_rsp
