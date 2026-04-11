# ⚙️ Streaming Twitter/X Analytics

> Pipeline temps réel de sentiment analysis sur les tendances Twitter/X.

## 📊 Problématique Business

**Contexte** : Analyser les tendances Twitter nécessite du traitement en flux continu, pas des snapshots.

**Défi** : Ingérer, enrichir et analyser 1000 tweets/minute avec une latence de traitement < 1 seconde.

**Objectif** : Détecter les **trending topics et leur sentiment** en temps réel sur des keywords ciblés.

---

## 🗂️ Dataset

- **Source streaming** : [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api) (gratuit limité)
- **Alternative sans API** : [ntscraper](https://github.com/bocchilorenzo/ntscraper)
- **Volume** : ~1 000 tweets/minute sur keywords configurables
- **Features** : Texte, métriques d'engagement, user info, géolocalisation

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Latence traitement** | < 1s par batch |
| **Détection trending** | Temps réel |
| **Accuracy sentiment** | > 80% |
| **Scalabilité** | Architecture Kafka/Spark extensible |

---

## 🛠️ Stack

- **Streaming** : Apache Kafka, Apache Spark Streaming
- **ML** : scikit-learn, TensorFlow
- **Storage** : PostgreSQL, Redis
- **Viz** : Grafana, Power BI
- **Deploy** : Docker Compose

---

## 📦 Structure

```
13-streaming-twitter-analytics/
├── producer/           # Kafka producer (ingestion tweets)
├── consumer/           # Spark Streaming processing
├── ml/                 # Modèle sentiment
├── storage/            # Schémas PostgreSQL
└── dashboard/          # Config Grafana
```

---

## 💡 Techniques Clés

**Architecture streaming** :
- Producer Kafka pour découpler ingestion et traitement
- Spark Streaming pour processing distribué
- Redis pour cache des résultats récents

**NLP temps réel** :
- Modèle pré-entraîné pour latence minimale
- Sliding window pour détection de tendances

---

## 📚 Ressources

- [Twitter API v2 Docs](https://developer.twitter.com/en/docs/twitter-api)
- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart)
- [Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
