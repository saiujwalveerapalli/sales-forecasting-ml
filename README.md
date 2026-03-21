# 📈 Sales Forecasting with Machine Learning

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/XGBoost-FF6600?style=flat)](https://xgboost.readthedocs.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> End-to-end ML pipeline comparing 5 regression models for monthly sales forecasting. Best model (XGBoost) achieved **RMSE of 4.2%** — an **18% improvement** over linear baseline. Published in IRJET 2024.

---

## 📊 Results

| Model | RMSE | MAE | R² |
|---|---|---|---|
| Linear Regression (baseline) | 5.1% | 4.3% | 0.81 |
| Ridge Regression | 4.9% | 4.1% | 0.83 |
| Random Forest | 4.6% | 3.8% | 0.86 |
| Gradient Boosting | 4.4% | 3.6% | 0.88 |
| **XGBoost (best)** | **4.2%** | **3.4%** | **0.90** |

> XGBoost reduced RMSE by **18%** vs baseline through feature engineering and cross-validated hyperparameter tuning.

---

## 🔍 Approach

- Feature engineering: lag features, rolling means, seasonality, trend decomposition
- Model comparison: 5 models, 5-fold cross validation
- Tuning: GridSearchCV on 12 hyperparameters
- Evaluation: MSE, RMSE, MAE on holdout test set

---

## 🚀 Quick Start
```bash
git clone https://github.com/saiujwal-glitch/sales-forecasting-ml.git
cd sales-forecasting-ml
pip install -r requirements.txt
python src/pipeline.py --data data/sales_data.csv --model xgboost
```

---

## 📂 Project Structure
```
sales-forecasting-ml/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Comparison.ipynb
│   └── 04_XGBoost_Tuning.ipynb
├── src/
│   ├── features.py
│   ├── models.py
│   ├── evaluate.py
│   └── pipeline.py
├── models/
│   └── xgboost_best.pkl
├── requirements.txt
└── README.md
```

---

## 📦 Requirements
```
xgboost>=1.7
scikit-learn>=1.0
pandas>=1.4
numpy>=1.22
matplotlib>=3.5
seaborn>=0.11
jupyter>=1.0
```

---

## 📚 Publication

> **Sales Forecasting using Machine Learning** — IRJET, 2024

---

## 👤 Author

**Sai Ujwal Veerapalli**
- LinkedIn: [linkedin.com/in/saiujwalveerapalli](https://www.linkedin.com/in/saiujwalveerapalli)
- Email: saiujwal@iastate.edu
