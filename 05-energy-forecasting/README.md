# ⚡ Prévision Consommation Énergétique

> Prédire la demande H+1 et H+24 pour éviter 100k€/h de coûts.

## 📊 Problématique

**Contexte** : Le gestionnaire réseau doit équilibrer production et consommation.

**Coût** : Une erreur coûte **100k€/heure** (déséquilibre réseau).

**Objectif** : Prédire la demande à **H+1** et **H+24** avec MAPE < 3%.

## 🗂️ Dataset

- **Source** : [Hourly Energy Consumption - Kaggle](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)
- **API Météo** : OpenWeatherMap (gratuit)
- **Volume** : 10 ans données horaires

## 🛠️ Stack

- Polars (feature engineering temporel)
- Prophet + LSTM (ensemble models)
- FastAPI (API prédictions)
- Grafana (monitoring)

## 🎯 Livrables

1. Pipeline données météo temps réel
2. Ensemble LSTM + XGBoost
3. API avec intervalles de confiance
4. Dashboard monitoring performances
