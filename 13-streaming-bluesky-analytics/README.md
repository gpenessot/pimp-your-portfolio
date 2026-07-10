# ⚙️ Streaming Bluesky Analytics

> Pipeline temps réel de sentiment analysis sur les tendances Bluesky.

## 📊 Problématique Business

**Contexte** : Analyser les tendances sociales nécessite du traitement en flux continu, pas des snapshots.

**Défi** : Ingérer, enrichir et analyser des centaines d'événements/seconde avec une latence de traitement < 1 seconde.

**Objectif** : Détecter les **trending topics et leur sentiment** en temps réel sur des keywords ciblés.

---

## 🗂️ Dataset

- **Source streaming** : [Bluesky Jetstream](https://docs.bsky.app/docs/advanced-guides/firehose) — WebSocket public, sans authentification requise
- **Volume** : ~300-500 événements/seconde sur le firehose complet, filtrable par keywords
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
13-streaming-bluesky-analytics/
├── producer/           # Kafka producer (ingestion Jetstream)
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

- [Bluesky Jetstream Docs](https://docs.bsky.app/docs/advanced-guides/firehose)
- [Apache Kafka Quickstart](https://kafka.apache.org/quickstart)
- [Spark Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
