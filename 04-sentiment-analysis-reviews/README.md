# 💬 Analyse Sentiment Avis Produits

> Extraire automatiquement points positifs/négatifs de 500k+ avis clients.

## 📊 Problématique

**Contexte** : L'entreprise reçoit **des milliers d'avis clients** mais n'a pas le temps de les analyser.

**Objectif** : Extraire automatiquement les points positifs/négatifs par produit.

## 🗂️ Dataset

- **Source** : [Amazon Product Reviews - Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- **API** : Reddit API (flux temps réel)
- **Volume** : 568,454 avis + flux Reddit

## 🛠️ Stack

- PRAW (collecteur Reddit)
- scikit-learn (TF-IDF, classification)
- transformers (modèles pré-entraînés)
- Streamlit (dashboard insights)

## 🎯 Livrables

1. Pipeline NLP end-to-end
2. Accuracy > 85% sur sentiment
3. Extraction topics principaux
4. Dashboard actualisé quotidiennement
