# 15 Projets Data pour un Portfolio Professionnel

> Des projets concrets avec de vraies problématiques business pour démarquer votre portfolio des projets académiques classiques.

## 🎯 Objectif

Ce repository propose 15 projets data avec :
- Des problématiques métier réelles
- Des datasets publics et APIs gratuites
- Des architectures techniques modernes
- Des livrables professionnels attendus

**Pas de Titanic. Du concret.**

---

## 🔬 DATA SCIENTIST (5 projets)

### 1. Prédiction de Churn Client - Télécoms

**🎯 Problématique Business**
L'entreprise de télécommunications perd 25% de ses clients chaque année. Le coût d'acquisition d'un nouveau client (CAC) est 5x plus élevé que la rétention. Objectif : identifier les clients à risque 3 mois avant leur départ.

**📊 Dataset**
- **Source** : [Telco Customer Churn - IBM](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Volume** : 7,043 clients avec 21 features
- **Features clés** : Démographie, services souscrits, historique paiements, support client
- **Enrichissement** : Simuler des events temps réel avec Faker Python

**🏗️ Architecture Technique**
```
Data Source → Feature Engineering → ML Pipeline → API → Dashboard
    ↓              ↓                   ↓          ↓        ↓
  Kaggle        Polars            Scikit-learn  FastAPI  Streamlit
  CSV           Feature Store        MLflow     Docker   Monitoring
```

**📦 Livrables Attendus**
1. **Notebook d'exploration** avec analyse des patterns de churn
2. **Pipeline ML** avec validation temporelle et feature importance
3. **API REST** pour scoring en temps réel (FastAPI)
4. **Dashboard métier** interactif pour le customer success
5. **Monitoring** du modèle avec détection de drift

**🎯 Critères de Réussite**
- Recall > 80% sur la classe churn (minimiser les faux négatifs)
- API avec latence < 100ms
- Dashboard utilisable par des non-techniques

**🛠️ Stack Recommandée**
- **ML** : Python, scikit-learn, XGBoost, MLflow
- **Data** : Polars (plus rapide que pandas)
- **API** : FastAPI, Pydantic
- **Deploy** : Docker, GitHub Actions

---

### 2. Détection de Fraude Bancaire Temps Réel

**🎯 Problématique Business**
La banque subit 2M€ de pertes annuelles dues à la fraude. Les transactions frauduleuses représentent 0.17% du volume mais 15% des pertes. Objectif : détecter 95% des fraudes en < 50ms.

**📊 Dataset**
- **Source** : [Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Volume** : 284,807 transactions sur 2 jours
- **Simulation** : Créer un stream avec Python + générateur de nouvelles fraudes
- **Features** : 30 variables (PCA transformées) + montant + temps

**🏗️ Architecture Technique**
```
Transaction Stream → Processing → ML Model → Decision → Alert
        ↓              ↓            ↓          ↓        ↓
    CSV + Faker    Streaming     XGBoost    Redis   Webhook
    Simulation      DuckDB       Online      Rules   Dashboard
```

**📦 Livrables Attendus**
1. **Simulateur de transactions** avec Faker pour stream temps réel
2. **Pipeline streaming** local avec asyncio Python
3. **Modèle ML** avec gestion du déséquilibre (SMOTE)
4. **Système d'alertes** avec niveaux de risque
5. **Dashboard monitoring** Streamlit temps réel

**🎯 Critères de Réussite**
- Precision > 90% (limiter les faux positifs)
- Latence < 50ms par prédiction
- Gestion de 1000 transactions/seconde en local

**🛠️ Stack Recommandée**
- **ML** : Python, XGBoost, Imbalanced-learn
- **Streaming** : asyncio, threading
- **Cache** : Redis local ou dict Python
- **Viz** : Streamlit avec refresh auto

---

### 3. Optimisation Prix E-commerce

**🎯 Problématique Business**
La marketplace e-commerce veut maximiser son chiffre d'affaires en ajustant les prix selon la demande et l'élasticité. Objectif : +15% de CA sans perdre de volume.

**📊 Dataset**
- **Source** : [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **Volume** : 100k commandes, 32k produits
- **Enrichissement** : [API Exchange Rates](https://exchangeratesapi.io/) pour variations devise
- **Features** : Prix, catégorie, reviews, saisonnalité, géolocalisation

**🏗️ Architecture Technique**
```
Historical Data → Analysis → Price Model → Simulation → Dashboard
      ↓             ↓           ↓            ↓          ↓
   Kaggle CSV     Polars    Elasticity    Monte Carlo  Marimo
   Parquet        DuckDB    Optimization    A/B Sim    Interactive
```

**📦 Livrables Attendus**
1. **Analyse élasticité prix** par catégorie de produits
2. **Modèle de demande** avec saisonnalité (Prophet)
3. **Algorithme d'optimisation** des prix (scipy.optimize)
4. **Simulateur A/B** pour tester les stratégies
5. **Dashboard Marimo** interactif pour les PMs

**🎯 Critères de Réussite**
- Identification de l'élasticité par segment
- Simulation montrant +10% CA potentiel
- Interface simple pour tester des scénarios

**🛠️ Stack Recommandée**
- **Data** : Polars, DuckDB
- **Modeling** : Prophet, statsmodels
- **Optimization** : scipy, OR-Tools
- **Viz** : Marimo (notebooks interactifs)

---

### 4. Analyse Sentiment Avis Produits

**🎯 Problématique Business**
L'entreprise reçoit des milliers d'avis clients mais n'a pas le temps de les analyser. Objectif : extraire automatiquement les points positifs/négatifs par produit.

**📊 Dataset**
- **Source principale** : [Amazon Product Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- **API temps réel** : [Reddit API](https://www.reddit.com/dev/api/) (gratuit avec limits)
- **Volume** : 568,454 avis Amazon + flux Reddit
- **Languages** : Principalement anglais

**🏗️ Architecture Technique**
```
Reviews Data → NLP Pipeline → Topic Analysis → Insights → Dashboard
     ↓            ↓              ↓             ↓          ↓
  CSV+Reddit   Transformers    BERTopic    Clustering  Streamlit
  PRAW API     Sentiment      Aspects      Keywords    WordCloud
```

**📦 Livrables Attendus**
1. **Collecteur Reddit** avec PRAW (Python Reddit API Wrapper)
2. **Pipeline sentiment** avec Hugging Face models
3. **Extraction topics** automatique (BERTopic)
4. **Analyse aspects** (price, quality, shipping)
5. **Dashboard** avec nuages de mots et tendances

**🎯 Critères de Réussite**
- Accuracy > 85% sur classification sentiment
- Détection automatique des pain points majeurs
- Actualisation quotidienne avec Reddit

**🛠️ Stack Recommandée**
- **APIs** : PRAW pour Reddit
- **NLP** : transformers, spaCy
- **Topics** : BERTopic, Top2Vec
- **Viz** : Streamlit, WordCloud

---

### 5. Prévision Consommation Énergétique

**🎯 Problématique Business**
Le gestionnaire réseau doit équilibrer production et consommation. Une erreur coûte 100k€/heure. Objectif : prédire la demande à H+1 et H+24.

**📊 Dataset**
- **Source historique** : [Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption)
- **Météo temps réel** : [OpenWeatherMap API](https://openweathermap.org/api) (gratuit)
- **Volume** : 10 ans données horaires + météo live
- **Features** : Consommation, température, calendrier

**🏗️ Architecture Technique**
```
Time Series → Feature Engineering → ML Models → API → Monitoring
     ↓              ↓                 ↓         ↓        ↓
  CSV+Weather     Polars          LSTM+XGB   FastAPI  Grafana
  OpenWeather   Lag Features     Ensemble    Cache    Alerts
```

**📦 Livrables Attendus**
1. **Pipeline données** avec API météo temps réel
2. **Feature engineering** temporel (lags, rolling)
3. **Ensemble models** (LSTM + XGBoost)
4. **API prédiction** avec intervalles de confiance
5. **Dashboard monitoring** des performances

**🎯 Critères de Réussite**
- MAPE < 3% pour H+1
- API temps réel avec météo actuelle
- Alertes sur prédictions anormales

**🛠️ Stack Recommandée**
- **Time Series** : statsmodels, Prophet
- **Deep Learning** : TensorFlow/PyTorch
- **API météo** : requests + cache
- **Deploy** : Docker, FastAPI

---

## 📊 DATA ANALYST (5 projets)

### 6. Dashboard KPIs E-commerce

**🎯 Problématique Business**
La startup e-commerce n'a aucune visibilité sur ses performances. Excel ne suffit plus. Objectif : dashboard professionnel avec KPIs temps réel.

**📊 Dataset**
- **Source** : [Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Enrichissement** : [Faker](https://faker.readthedocs.io/) pour simuler données récentes
- **Volume** : 541,909 transactions + simulation temps réel
- **Métriques** : CA, panier moyen, conversion, cohortes

**🏗️ Architecture Technique**
```
Raw Data → Transformation → Metrics → Visualization → Sharing
    ↓           ↓            ↓          ↓            ↓
  Excel       DuckDB        SQL      Streamlit    Public URL
  CSV         Polars      Metrics     Plotly     GitHub Pages
```

**📦 Livrables Attendus**
1. **ETL pipeline** avec DuckDB pour performance
2. **Metrics layer** avec définitions SQL claires
3. **Dashboard interactif** Streamlit multi-pages
4. **Simulation temps réel** avec auto-refresh
5. **Documentation** des KPIs et calculs

**🎯 Critères de Réussite**
- Chargement dashboard < 3 secondes
- KPIs standards e-commerce (CAC, LTV, etc.)
- Exportable et partageable facilement

**🛠️ Stack Recommandée**
- **Data** : DuckDB (SQL engine)
- **Transform** : Polars + SQL
- **Viz** : Streamlit + Plotly
- **Deploy** : Streamlit Cloud (gratuit)

---

### 7. Analyse Cohortes Application Mobile

**🎯 Problématique Business**
L'app mobile perd 60% des utilisateurs après J+1. Objectif : comprendre les comportements et améliorer la rétention.

**📊 Dataset**
- **Source** : [Mobile App User Behavior](https://www.kaggle.com/datasets/daniilgorev/mobile-app-user-behavior-dataset)
- **Simulation events** : Générateur Python pour events in-app
- **Volume** : 100k users + events générés
- **Events** : Install, sessions, purchases, uninstall

**🏗️ Architecture Technique**
```
Event Data → Cohort Analysis → Retention → Segmentation → Actions
     ↓             ↓              ↓           ↓           ↓
  CSV+Faker     Polars         Lifelines   Clustering   Marimo
  Generator    Cohorts        Survival     K-means     Report
```

**📦 Livrables Attendus**
1. **Générateur d'events** réalistes avec patterns
2. **Analyse cohortes** par source d'acquisition
3. **Courbes de rétention** avec survival analysis
4. **Segmentation** comportementale des users
5. **Notebook Marimo** interactif avec insights

**🎯 Critères de Réussite**
- Identification de 3 segments utilisateurs clairs
- Recommandations actionnables pour le PM
- Visualisations compréhensibles

**🛠️ Stack Recommandée**
- **Analysis** : Polars, lifelines
- **Viz** : Plotly, seaborn
- **Interactive** : Marimo notebooks
- **Stats** : scipy, statsmodels

---

### 8. Attribution Marketing Multi-Touch

**🎯 Problématique Business**
L'entreprise dépense sur Google, Facebook, email sans savoir ce qui convertit. Objectif : modèle d'attribution pour optimiser le budget.

**📊 Dataset**
- **Source** : [Multi-Channel Marketing](https://www.kaggle.com/datasets/sudhanshu2198/multi-channel-marketing-data)
- **Google Trends** : [pytrends](https://pypi.org/project/pytrends/) pour données SEO
- **Volume** : 500k user journeys + trends temps réel
- **Canaux** : Paid search, social, email, organic

**🏗️ Architecture Technique**
```
Journey Data → Attribution → ROAS Analysis → Optimization → Report
      ↓           ↓             ↓              ↓           ↓
   CSV Data   Markov Chain   Channel ROI    Linear Prog  Quarto
   pytrends    Heuristics    Incrementality  Budget Opt  Dashboard
```

**📦 Livrables Attendus**
1. **Customer journey** visualization
2. **Modèles attribution** (first/last click, data-driven)
3. **Analyse ROAS** par canal avec trends
4. **Optimiseur budget** avec contraintes
5. **Rapport Quarto** automatisé mensuel

**🎯 Critères de Réussite**
- Attribution model vs reality check
- Budget recommendations claires
- Dashboard actionnable pour marketing

**🛠️ Stack Recommandée**
- **Attribution** : Python, ChannelAttribution
- **Trends** : pytrends API
- **Optimization** : PuLP, scipy
- **Report** : Quarto + great_tables

---

### 9. People Analytics - Turnover

**🎯 Problématique Business**
L'entreprise a 25% de turnover (vs 15% marché). Chaque départ coûte 50k€. Objectif : prédire et prévenir les départs.

**📊 Dataset**
- **Source** : [IBM HR Analytics](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- **Glassdoor API** : [API non officielle](https://github.com/scrapfly/glassdoor-scraper) pour benchmarks
- **Volume** : 1,470 employés avec 35 variables
- **Features** : Satisfaction, salaire, promotion, distance

**🏗️ Architecture Technique**
```
HR Data → Statistical Analysis → ML Model → Risk Score → Actions
   ↓            ↓                 ↓           ↓          ↓
 Kaggle     Polars/DuckDB    Scikit-learn  Dashboard   Email
 CSV          EDA Stats       Explainable   Streamlit  Alerts
```

**📦 Livrables Attendus**
1. **Analyse exploratoire** des facteurs de départ
2. **Tests statistiques** (chi2, t-test, ANOVA)
3. **Modèle prédictif** interprétable (logistic, trees)
4. **Dashboard RH** avec profils à risque
5. **Recommandations** concrètes par profil

**🎯 Critères de Réussite**
- AUC > 0.85 sur prédiction départ
- Identification top 5 facteurs
- Plan d'action RH personnalisé

**🛠️ Stack Recommandée**
- **Analysis** : Polars, scipy
- **ML** : scikit-learn, SHAP
- **Viz** : Streamlit, Plotly
- **Deploy** : Streamlit Cloud

---

### 10. Supply Chain Analytics

**🎯 Problématique Business**
Le distributeur subit 15% de ruptures et 30% de surstocks. Objectif : optimiser les niveaux de stock et prédire les ruptures.

**📊 Dataset**
- **Source** : [Supply Chain Dataset](https://www.kaggle.com/datasets/harshsingh2209/supply-chain-dataset)
- **Simulation** : Générateur Python pour events logistiques
- **Volume** : 180k commandes, 20 entrepôts
- **Features** : Ventes, stocks, délais, saisonnalité

**🏗️ Architecture Technique**
```
Supply Data → Analytics → Forecasting → Optimization → Monitoring
     ↓           ↓           ↓             ↓            ↓
  CSV+Sim      DuckDB     Prophet      Inventory    Great Tables
  Events       Metrics    Time Series   Algorithm    Reports
```

**📦 Livrables Attendus**
1. **KPIs supply chain** (taux service, rotation)
2. **Segmentation ABC/XYZ** des produits
3. **Prévisions demande** avec Prophet
4. **Calculateur stock** sécurité optimal
5. **Tableaux de bord** avec great_tables

**🎯 Critères de Réussite**
- Réduction ruptures de 50%
- Optimisation stocks de 20%
- Alertes automatiques fonctionnelles

**🛠️ Stack Recommandée**
- **Analytics** : DuckDB + Polars
- **Forecasting** : Prophet
- **Viz** : great_tables, Plotly
- **Automation** : Python scripts

---

## ⚙️ DATA ENGINEER (5 projets)

### 11. Pipeline Crypto Trading

**🎯 Problématique Business**
Analyser les cryptos nécessite des données temps réel multi-sources. Objectif : pipeline robuste pour 50+ cryptos avec historique et live.

**📊 Dataset**
- **APIs publiques** : [CoinGecko API](https://www.coingecko.com/en/api) (gratuit)
- **Historique** : [Binance API](https://binance-docs.github.io/apidocs/) (gratuit)
- **Volume** : 50 cryptos, données minute
- **Features** : Prix, volume, market cap, social metrics

**🏗️ Architecture Technique**
```
APIs → Collection → Storage → Processing → Serving → Monitoring
  ↓        ↓          ↓         ↓          ↓         ↓
Binance  Asyncio    DuckDB    Polars    FastAPI   Grafana
CoinGecko Schedule  Parquet   Window    REST API  Prometheus
```

**📦 Livrables Attendus**
1. **Collecteurs API** asynchrones avec retry
2. **Storage optimisé** (Parquet partitionné)
3. **Pipeline incremental** avec windowing
4. **API serving** pour backtesting
5. **Monitoring** santé du pipeline

**🎯 Critères de Réussite**
- 99% uptime sur collecte données
- Latence API < 100ms
- Historique + temps réel unifié

**🛠️ Stack Recommandée**
- **Collection** : httpx, asyncio
- **Storage** : DuckDB, Parquet
- **Processing** : Polars
- **API** : FastAPI
- **Orchestration** : APScheduler

---

### 12. ETL Open Data Gouvernement

**🎯 Problématique Business**
Les données publiques sont éparpillées et mal formatées. Objectif : créer un data warehouse unifié pour analyses citoyennes.

**📊 Dataset**
- **Sources multiples** :
  - [data.gouv.fr API](https://doc.data.gouv.fr/api/reference/)
  - [INSEE API](https://api.insee.fr/catalogue/)
  - [OpenDataSoft](https://public.opendatasoft.com/api/v2/)
- **Volume** : 100+ datasets publics
- **Formats** : CSV, JSON, XML, APIs

**🏗️ Architecture Technique**
```
Open Data → Ingestion → Cleaning → Warehouse → API → Portal
    ↓          ↓          ↓          ↓        ↓       ↓
Multiple    Airbyte    Pandas    DuckDB   FastAPI  Datasette
Sources     Python    Cleaning   Storage   GraphQL  Explorer
```

**📦 Livrables Attendus**
1. **Catalogue datasets** avec métadonnées
2. **Pipeline ETL** générique multi-format
3. **Data quality** checks automatisés
4. **API unifiée** REST + GraphQL
5. **Data portal** avec Datasette

**🎯 Critères de Réussite**
- 50+ datasets intégrés
- Update automatique quotidien
- Documentation API complète

**🛠️ Stack Recommandée**
- **ETL** : Python, Airbyte
- **Storage** : DuckDB
- **Quality** : Great Expectations
- **API** : FastAPI, Strawberry GraphQL
- **Portal** : Datasette

---

### 13. Streaming Twitter/X Analytics

**🎯 Problématique Business**
Analyser les tendances Twitter nécessite du traitement temps réel. Objectif : pipeline de sentiment analysis sur sujets trending.

**📊 Dataset**
- **Source streaming** : [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) (gratuit limité)
- **Alternative** : [ntscraper](https://github.com/bocchilorenzo/ntscraper) (sans API)
- **Volume** : 1000 tweets/minute sur keywords
- **Features** : Texte, metrics, user info, géo

**🏗️ Architecture Technique**
```
Twitter → Stream Processing → NLP → Storage → Analytics → Alerts
   ↓           ↓              ↓       ↓         ↓         ↓
 API v2     AsyncIO      Transformers DuckDB  Streamlit  Discord
Scraper    Queue/Buffer  Sentiment   Time DB  Real-time  Webhook
```

**📦 Livrables Attendus**
1. **Collecteur Twitter** respectant rate limits
2. **Queue processing** avec buffer local
3. **NLP pipeline** sentiment + entities
4. **Storage** time-series optimisé
5. **Dashboard** temps réel + alertes

**🎯 Critères de Réussite**
- Processing < 1 sec par tweet
- Détection trending topics automatique
- Visualisation temps réel fluide

**🛠️ Stack Recommandée**
- **Streaming** : tweepy, asyncio
- **Queue** : Python Queue, Redis
- **NLP** : transformers
- **Storage** : DuckDB + TimescaleDB
- **Viz** : Streamlit avec auto-refresh

---

### 14. Data Quality Platform

**🎯 Problématique Business**
Les équipes data passent 40% du temps à debugger des erreurs de qualité. Objectif : plateforme de monitoring automatisé.

**📊 Dataset**
- **Sources** : Vos propres projets data !
- **Simulation** : Générateur de données avec anomalies
- **Volume** : Multi-sources, multi-formats
- **Tests** : Schéma, distribution, business rules

**🏗️ Architecture Technique**
```
Data Sources → Profiling → Testing → Monitoring → Alerts
      ↓           ↓          ↓         ↓          ↓
   Various    ydata-profiling  GE    Evidently  Slack
   Formats     Pandas Profile Soda   ML Drift   Email
```

**📦 Livrables Attendus**
1. **Auto-profiling** des nouveaux datasets
2. **Test suite** avec Great Expectations
3. **Drift detection** pour ML data
4. **Dashboard qualité** centralisé
5. **Alerting** multi-canal configurable

**🎯 Critères de Réussite**
- Détection 95% des anomalies data
- Réduction 50% temps debugging
- Adoption par toute l'équipe data

**🛠️ Stack Recommandée**
- **Profiling** : ydata-profiling
- **Testing** : Great Expectations, Soda
- **Drift** : Evidently AI
- **Orchestration** : Prefect
- **Monitoring** : Metabase

---

### 15. Modern Data Stack Local

**🎯 Problématique Business**
Construire une infrastructure data moderne sans cloud pour apprendre. Objectif : stack complète tournant sur un laptop.

**📊 Dataset**
- **NYC Taxi** : [TLC Trip Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **E-commerce** : [Brazilian Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **IoT simulé** : Générateur Python
- **Volume** : 10GB+ pour tester les limites

**🏗️ Architecture Technique**
```
Sources → Ingestion → Transform → Analytics → Orchestration
   ↓         ↓          ↓          ↓            ↓
Multiple   Meltano      dbt      DuckDB      Dagster
Formats    Singer     Models    BI Layer    Schedule
```

**📦 Livrables Attendus**
1. **Architecture** complète en local
2. **Ingestion** avec Meltano/Singer
3. **Transformation** dbt + DuckDB
4. **BI layer** avec Metabase/Superset
5. **Documentation** setup et best practices

**🎯 Critères de Réussite**
- Stack complète sur machine 8GB RAM
- Pipeline end-to-end fonctionnel
- Reproductible via Docker Compose

**🛠️ Stack Recommandée**
- **Ingestion** : Meltano
- **Transform** : dbt-duckdb
- **Database** : DuckDB
- **Orchestration** : Dagster
- **BI** : Metabase (léger)
- **Containers** : Docker Compose

---

## 💡 Conseils pour Réussir

### 🎯 Choix du Projet
- **Alignez avec votre objectif** : startup → full-stack, entreprise → spécialisation
- **Commencez petit** : MVP en 2 semaines, itérez ensuite
- **Documentez tout** : choix techniques, trade-offs, apprentissages

### 🚀 Développement
- **Git from day 1** : commits atomiques, branches features
- **Tests** : au minimum sur les fonctions critiques
- **CI/CD** : GitHub Actions (gratuit)
- **Data versioning** : DVC pour les gros fichiers

### 📖 Documentation
- **README complet** : problème, solution, démo GIF
- **Setup guide** : one-click install idéalement
- **Architecture** : diagrammes avec Mermaid
- **Blog post** : votre parcours et learnings

### 🎤 Présentation
- **Business first** : commencez par l'impact
- **Démo live** : préparez une démo qui marche
- **Code walkthrough** : montrez les parties intéressantes
- **Lessons learned** : soyez honnête sur les difficultés

### 🌟 Pour aller plus loin
- **Contribuez** à des projets open source data
- **Participez** aux compétitions Kaggle (top 50%)
- **Bloguez** sur dev.to ou Medium
- **Streamez** votre code sur Twitch/YouTube

---

## 🔗 Ressources Complémentaires

### APIs Gratuites
- [Public APIs](https://github.com/public-apis/public-apis) - Liste massive d'APIs
- [RapidAPI](https://rapidapi.com/hub) - Hub d'APIs avec free tier
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - API de test

### Datasets de Qualité
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Registry of Open Data on AWS](https://registry.opendata.aws/)
- [data.world](https://data.world/) - Communauté datasets

### Outils Modernes
- [DuckDB](https://duckdb.org/) - OLAP dans votre laptop
- [Polars](https://pola.rs/) - DataFrames ultra-rapides
- [Marimo](https://marimo.io/) - Notebooks réactifs
- [Evidence](https://evidence.dev/) - BI as code
- [Great Tables](https://posit-dev.github.io/great-tables/) - Tableaux magnifiques

### Learning Resources
- [DataTalks.Club](https://datatalks.club/) - Communauté et bootcamps gratuits
- [Made With ML](https://madewithml.com/) - MLOps best practices
- [Eugene Yan's Blog](https://eugeneyan.com/) - Applied ML
- [Locally Optimistic](https://locallyoptimistic.com/) - Data leadership

---

**Prêt à démarrer ?** 
1. Choisissez UN projet qui vous motive
2. Créez votre repo GitHub
3. Commencez par un MVP simple
4. Itérez et améliorez
5. Partagez vos progrès !

**Besoin d'aide ?** La communauté data est bienveillante. N'hésitez pas à demander sur Twitter/LinkedIn avec #DataPortfolio

---

*Ce guide est vivant - vos PRs sont les bienvenues pour ajouter de nouveaux datasets/APIs !*
