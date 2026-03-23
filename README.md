# 📈 Sales Forecasting with ML — REST API on GCP Cloud Run

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat)](https://xgboost.readthedocs.io)
[![GCP](https://img.shields.io/badge/GCP_Cloud_Run-4285F4?style=flat&logo=googlecloud&logoColor=white)](https://cloud.google.com/run)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)

> XGBoost model deployed as a **REST API on GCP Cloud Run** with full ETL pipeline for batch and real-time processing. Benchmarked 5 regression models — XGBoost achieved **RMSE 4.2%** on holdout set. Published in **IRJET 2024**.

---

## 📊 Model Comparison

| Model | RMSE | R² |
|-------|------|----|
| Linear Regression | 5.1% | 0.81 |
| Ridge Regression | 4.9% | 0.83 |
| Random Forest | 4.6% | 0.86 |
| Gradient Boosting | 4.4% | 0.88 |
| **XGBoost (best)** | **4.2%** | **0.90** |

XGBoost reduced RMSE by **18%** vs baseline via feature engineering and cross-validated tuning.

---

## 🧱 Pipeline Architecture
```
Raw Sales Data → ETL Pipeline → Feature Engineering
(lag features, rolling means, seasonality)
→ XGBoost Training → REST API (GCP Cloud Run)
→ Batch + Real-time Processing
```

---

## 📡 API Usage
```bash
POST /forecast
Content-Type: application/json

{
  "lag_1": 142000,
  "lag_7": 138500,
  "rolling_mean_30": 140200,
  "month": 3,
  "quarter": 1
}
```

Response:
```json
{
  "forecast": 142500.0,
  "rmse": "4.2%",
  "model": "XGBoost",
  "processing": "real-time"
}
```

---

## 🚀 Run Locally
```bash
git clone https://github.com/saiujwalveerapalli/sales-forecasting-ml.git
cd sales-forecasting-ml
pip install -r requirements.txt
uvicorn app:app --reload
```

## 🐳 Docker
```bash
docker build -t sales-api .
docker run -p 8080:8080 sales-api
```

---

## 📁 Project Structure
```
sales-forecasting-ml/
├── app.py              # REST API
├── src/
│   ├── features.py     # Feature engineering
│   └── etl.py          # ETL pipeline
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📚 Publication

**Sales Forecasting using Machine Learning** — IRJET, 2024

---

## 👤 Author

**Sai Ujwal Veerapalli** · [LinkedIn](https://linkedin.com/in/saiujwalveerapalli) · [Portfolio](https://saiujwalveerapalli.github.io)
