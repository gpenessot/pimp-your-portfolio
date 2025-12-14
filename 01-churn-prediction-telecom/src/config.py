"""
Configuration pour le projet Churn Prediction
"""
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"

# Data
DATA_FILE = "telco_churn.csv"
TARGET_COL = "Churn"

# Features
NUMERICAL_FEATURES = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

CATEGORICAL_FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]

# Model
MODEL_NAME = "xgboost_churn"
MODEL_VERSION = "1.0.0"
RANDOM_STATE = 42
TEST_SIZE = 0.2

# XGBoost hyperparameters
XGBOOST_PARAMS = {
    "max_depth": 6,
    "learning_rate": 0.1,
    "n_estimators": 200,
    "objective": "binary:logistic",
    "eval_metric": "logloss",
    "scale_pos_weight": 3,  # Gestion déséquilibre (73.5/26.5)
    "random_state": RANDOM_STATE,
}

# Thresholds
CHURN_THRESHOLD = 0.5  # Probabilité seuil pour prédire churn
HIGH_RISK_THRESHOLD = 0.7  # Seuil pour risque élevé

# MLflow
MLFLOW_TRACKING_URI = "./mlruns"
EXPERIMENT_NAME = "churn_prediction"

# API
API_TITLE = "Churn Prediction API"
API_VERSION = "1.0.0"
API_HOST = "0.0.0.0"
API_PORT = 8000
