# ⚙️ Pipeline Crypto Trading

> Pipeline robuste pour collecter et servir les données de 50+ cryptomonnaies en temps réel.

## 📊 Problématique Business

**Contexte** : Analyser les cryptos nécessite des données temps réel multi-sources fiables.

**Défi** : Agréger des flux hétérogènes (prix, volume, social) depuis plusieurs APIs avec une haute disponibilité.

**Objectif** : Pipeline stable collectant **50+ cryptos à la minute** avec historique et serving API.

---

## 🗂️ Dataset

- **Source principale** : [CoinGecko API](https://www.coingecko.com/en/api) (gratuit)
- **Historique** : [Binance API](https://binance-docs.github.io/apidocs/) (gratuit)
- **Volume** : 50 cryptos, données à la minute
- **Features** : Prix, volume, market cap, social metrics

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Disponibilité pipeline** | > 99% uptime |
| **Fréquence collecte** | Toutes les minutes |
| **Retry logic** | Gestion automatique des erreurs API |
| **Latence API serving** | < 200ms |

---

## 🛠️ Stack

- **Orchestration** : Apache Airflow
- **Storage** : PostgreSQL + Parquet
- **Processing** : pandas ou PySpark
- **API** : FastAPI, Docker
- **Cloud** : AWS S3 ou Azure Blob (optionnel)

---

## 📦 Structure

```
11-pipeline-crypto-trading/
├── dags/               # DAGs Airflow
├── src/                # Collecteurs, transformations
├── api/                # FastAPI serving
├── storage/            # Schémas PostgreSQL
└── data/               # Cache local (non versionné)
```

---

## 💡 Techniques Clés

**Orchestration** :
- DAGs Airflow avec retry logic et alertes
- Scheduling granulaire par fréquence de collecte

**Storage** :
- PostgreSQL pour données structurées récentes
- Parquet pour historique longue durée

**Monitoring** :
- Logs Airflow centralisés
- Alertes sur échecs de collecte

---

## 📚 Ressources

- [CoinGecko API Docs](https://www.coingecko.com/en/api/documentation)
- [Binance API Docs](https://binance-docs.github.io/apidocs/)
- [Apache Airflow Docs](https://airflow.apache.org/docs/)
