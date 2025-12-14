# 🔒 Détection de Fraude Bancaire Temps Réel

> Détecter 95% des fraudes en < 50ms pour protéger 2M€ de pertes annuelles.

## 📊 Problématique Business

**Contexte** : La banque subit **2M€ de pertes annuelles** dues à la fraude.

**Défi** : Les transactions frauduleuses représentent **0.17%** du volume mais **15%** des pertes.

**Objectif** : Détecter **95% des fraudes** en **< 50ms** par transaction.

---

## 🗂️ Dataset

- **Source** : [Credit Card Fraud Detection - Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Volume** : 284,807 transactions sur 2 jours
- **Features** : 30 variables (PCA transformées) + `Amount` + `Time`
- **Target** : `Class` (0 = Normal, 1 = Fraude)
- **Déséquilibre** : 99.83% normal / 0.17% fraude

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Precision** | > 90% (limiter faux positifs) |
| **Recall** | > 95% (capturer vraies fraudes) |
| **Latence API** | < 50ms |
| **F2-Score** | > 0.90 (pondération recall) |

---

## 🛠️ Stack

- **ML** : XGBoost, imbalanced-learn (SMOTE), scikit-learn
- **API** : FastAPI + Redis (cache)
- **Monitoring** : Prometheus + Grafana
- **Deploy** : Docker

---

## 📦 Structure

```
02-fraud-detection-banking/
├── notebooks/           # EDA, modeling
├── src/                # Feature engineering, training
├── api/                # FastAPI endpoints
├── monitoring/         # Prometheus config
└── data/               # Dataset (non versionné)
```

---

## 💡 Techniques Clés

**Gestion déséquilibre** :
- SMOTE (oversampling minoritaire)
- Class weight adjustment
- Focal Loss

**Feature Engineering** :
- Fréquence transactions par utilisateur
- Montant par rapport à historique
- Patterns temporels (heure, jour)

---

## 📚 Ressources

- [Credit Card Fraud - Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- [Imbalanced-learn docs](https://imbalanced-learn.org/)
