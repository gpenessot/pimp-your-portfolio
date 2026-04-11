# ⚙️ Modern Data Stack Local

> Stack data moderne complète tournant sur un laptop — les outils du marché sans le cloud.

## 📊 Problématique Business

**Contexte** : Apprendre la data engineering nécessite d'expérimenter avec les outils réels du marché.

**Défi** : Monter une infrastructure complète (ingestion → transformation → serving → orchestration) de manière reproductible.

**Objectif** : **Stack complète fonctionnelle en local** via Docker, reproductible et documentée.

---

## 🗂️ Dataset

- **NYC Taxi** : [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **E-commerce** : [Brazilian Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- **IoT simulé** : Générateur Python
- **Volume** : 10GB+ pour tester les limites de la stack

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Reproductibilité** | `docker compose up` suffit |
| **Pipeline complet** | Source → DWH → Dashboard |
| **Transformations dbt** | Modèles staging + marts |
| **Documentation** | README one-click install |

---

## 🛠️ Stack

- **Orchestration** : Apache Airflow
- **ETL** : Python, pandas
- **Transformation** : dbt
- **Database** : PostgreSQL (data warehouse)
- **BI** : Power BI Desktop ou Tableau Public
- **Containers** : Docker Compose

---

## 📦 Structure

```
15-modern-data-stack-local/
├── dags/               # DAGs Airflow
├── dbt/                # Modèles dbt (staging, marts)
├── ingestion/          # Scripts Python d'ingestion
├── warehouse/          # Schémas PostgreSQL
└── docker-compose.yml  # Stack complète
```

---

## 💡 Techniques Clés

**Infrastructure as code** :
- Docker Compose pour orchestrer Airflow + PostgreSQL
- Variables d'environnement pour la configuration

**Modélisation dbt** :
- Couche staging : nettoyage et typage
- Couche marts : modèles métier agrégés
- Tests dbt sur unicité, non-nullité, relations

**Orchestration** :
- DAGs Airflow pour séquencer ingestion → transformation
- Dépendances explicites entre tâches

---

## 📚 Ressources

- [dbt Docs](https://docs.getdbt.com/)
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
- [NYC TLC Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
