import sys
import os
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from preprocessing import clean_text

sys.modules["clean_text"] = clean_text

# Load the model
model = joblib.load("./preprocessing/Sentiment_Model.pkl")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailData(BaseModel):
    email: str


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(data: EmailData):
    prediction = model.predict([data.email])[0]

    # Try to get probability confidence
    confidence = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba([data.email])[0]
        confidence = float(max(proba))

    return {"sentiment": str(prediction), "confidence": confidence}
