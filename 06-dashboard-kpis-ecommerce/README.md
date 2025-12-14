# 📊 Dashboard KPIs E-commerce

> Dashboard Power BI professionnel avec KPIs temps réel pour startup e-commerce.

## 📊 Problématique Business

**Contexte** : La startup e-commerce n'a **aucune visibilité** sur ses performances.

**Problème** : Excel ne suffit plus avec 500k+ transactions annuelles.

**Objectif** : Dashboard professionnel avec **KPIs temps réel** pour le CEO et l'équipe marketing.

---

## 🗂️ Dataset

- **Source** : [Online Retail Dataset - UCI](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Volume** : 541,909 transactions (1 an)
- **Enrichissement** : Faker Python pour données récentes
- **Métriques** : CA, panier moyen, conversion, RFM

---

## 🎯 KPIs Implémentés

**Ventes** :
- Chiffre d'affaires (jour, mois, année)
- Évolution CA vs N-1
- Top 10 produits

**Clients** :
- Nouveaux clients vs récurrents
- Panier moyen
- Taux de conversion
- Analyse RFM (Recency, Frequency, Monetary)

**Cohortes** :
- Rétention par mois de première commande
- LTV (Lifetime Value) par cohorte

---

## 🛠️ Stack

- **ETL** : Python (pandas, SQLAlchemy)
- **Database** : PostgreSQL (modèle en étoile)
- **BI** : Power BI Desktop + Power BI Service
- **Alternative** : Tableau Public (gratuit)

---

## 📦 Structure

```
06-dashboard-kpis-ecommerce/
├── src/
│   ├── etl_pipeline.py      # Nettoyage données
│   └── db_setup.py          # Création tables
├── sql/
│   ├── schema.sql           # Star schema
│   └── queries.sql          # Requêtes complexes
├── dashboards/
│   ├── ecommerce.pbix       # Power BI
│   └── ecommerce.twb        # Tableau
└── data/
    └── raw/                 # CSV brut
```

---

## 🎯 Critères de Réussite

- Dashboard < 3s de chargement
- Actualisation automatique quotidienne
- KPIs standards e-commerce complets
- Design professionnel

---

## 📚 Ressources

- [Online Retail UCI](https://archive.ics.uci.edu/dataset/352/online+retail)
- [Power BI Getting Started](https://learn.microsoft.com/power-bi/)
- [DAX Patterns](https://www.daxpatterns.com/)
