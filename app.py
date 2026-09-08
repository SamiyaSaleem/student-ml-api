from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="student-ml-api",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "1.0.0"
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = request.value * 2

    return {
        "input": request.value,
        "prediction": prediction
    }

