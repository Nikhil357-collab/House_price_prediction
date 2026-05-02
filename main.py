from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from fastapi import UploadFile, File
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#odel = joblib.load(os.path.join(BASE_DIR, "House_Price_PredictionModel/models/model.pkl"))
#eatures = joblib.load(os.path.join(BASE_DIR, "House_Price_PredictionModel/models/features.pkl"))
#-------------------------
print("Main file loaded")

app = FastAPI(title="House Price Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#----------------
# Load model
model = joblib.load(os.path.join(BASE_DIR, "models/model.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "models/features.pkl"))

# Input schema
class HouseInput(BaseModel):
    LotArea: float = 5000
    OverallQual: float = 5
    OverallCond: float = 5
    YearBuilt: float = 2000
    GrLivArea: float = 1500
    TotalBsmtSF: float = 800
    GarageCars: float = 2
    GarageArea: float = 400
    FullBath: float = 2
    HalfBath: float = 1
    Neighborhood_B: float = 0
    Neighborhood_C: float = 0
    HouseStyle_2Story: float = 0
    BldgType_Duplex: float = 0
    MSZoning_RM: float = 0

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

AVG_PRICE = 180000  # replace with real dataset mean

@app.post("/predict")
def predict(input_data: HouseInput):
    data_dict = input_data.dict()
    input_list = [data_dict.get(f, 0) for f in features]
    arr = np.array([input_list])

    prediction = model.predict(arr)[0]

    return {
    "predicted_price": float(prediction),
    "average_price": 180000
}
    
###--------------------------

@app.post("/predict-csv")
async def predict_csv(file: UploadFile = File(...)):

    content = await file.read()
    s = str(content, "utf-8")

    df = pd.read_csv(StringIO(s))

    # Ensure same columns as training
    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df[features]

    preds = model.predict(df)

    df["PredictedPrice"] = preds

    return df.to_dict(orient="records")