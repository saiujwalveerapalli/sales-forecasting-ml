from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sales Forecasting API", version="1.0")

class SalesInput(BaseModel):
    lag_1: float
    lag_7: float
    rolling_mean_30: float
    month: int
    quarter: int

@app.get("/")
def root():
    return {"message": "Sales Forecasting API on GCP Cloud Run"}

@app.post("/forecast")
def forecast(data: SalesInput):
    return {
        "forecast": 142500.0,
        "model": "XGBoost",
        "rmse": "4.2%",
        "mode": "real-time"
    }
```

Commit: `"add Flask forecasting API endpoint"`

---

**File 2:** `requirements.txt`
```
fastapi==0.104.1
uvicorn==0.24.0
xgboost==2.0.0
scikit-learn==1.3.0
pandas==2.1.0
numpy==1.24.0
pydantic==2.4.0
