from fastapi import FastAPI
from app.model import load_model, predict

app = FastAPI()

model = load_model()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_api(x: float):
    result = predict(model, x)
    return {"prediction": result}
