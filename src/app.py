import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Credit Scoring AI API", version="1.0")

class UserData(BaseModel):
    eta: int
    reddito_annuale: float
    debito_totale: float
    punteggio_credito: int

@app.get("/")
def home():
    return {"status": "API is running"}

@app.post("/predict")
def predict_credit_risk(user: UserData):
    prediction = 1 if user.punteggio_credito > 600 else 0
    return {"status": "Approvato" if prediction == 1 else "Rifiutato"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080, loop="asyncio")
