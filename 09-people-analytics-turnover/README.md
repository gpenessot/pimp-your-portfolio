# 👥 People Analytics - Prédiction Turnover

> Prédire et prévenir les départs (25% turnover, 50k€/départ).

## 📊 Problématique

**Contexte** : L'entreprise a **25% de turnover** (vs 15% marché).

**Coût** : Chaque départ coûte **50k€** (recrutement, formation, perte productivité).

**Objectif** : Prédire les départs 3 mois avant et réduire turnover à 18%.

## 🗂️ Dataset

- **Source** : [IBM HR Analytics - Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Benchmark marché** : [Adzuna API](https://developer.adzuna.com/) (gratuit, salaires réels extraits des offres d'emploi)
- **Volume** : 1,470 employés avec 35 variables
- **Target** : Attrition (Yes/No)

## 🛠️ Stack

- Polars (EDA rapide)
- scikit-learn (modèle explicable)
- SHAP (explainability)
- Streamlit (dashboard RH)

## 🎯 Facteurs Analysés

- Satisfaction travail
- Équilibre vie pro/perso
- Années depuis promotion
- Distance domicile-travail
- Niveau salaire vs marché
