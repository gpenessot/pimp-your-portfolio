# ⚙️ Data Quality Platform

> Plateforme de monitoring automatisé pour éliminer les erreurs de qualité données.

## 📊 Problématique Business

**Contexte** : Les équipes data passent **40% de leur temps** à débugger des problèmes de qualité de données.

**Défi** : Détecter proactivement les anomalies (schéma, distribution, dérive ML) avant qu'elles n'impactent la production.

**Objectif** : Réduire de **50% le temps de debugging** avec monitoring centralisé et alertes automatiques.

---

## 🗂️ Dataset

- **Sources** : Vos propres projets data (réutilisation des autres projets du repo)
- **Simulation** : Générateur Python de datasets avec anomalies injectées
- **Volume** : Multi-sources, multi-formats
- **Types de tests** : Schéma, distribution, règles métier, dérive ML

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Détection anomalies** | > 95% |
| **Réduction debugging** | - 50% temps |
| **Couverture tests** | 100% pipelines critiques |
| **Adoption équipe** | Self-service sans dev |

---

## 🛠️ Stack

- **Profiling** : ydata-profiling
- **Testing** : Great Expectations, Soda
- **Drift detection** : Evidently AI
- **Orchestration** : Prefect
- **Monitoring** : Metabase

---

## 📦 Structure

```
14-data-quality-platform/
├── profiling/          # Auto-profiling nouveaux datasets
├── expectations/       # Suites Great Expectations
├── drift/              # Détection dérive ML (Evidently)
├── orchestration/      # Flows Prefect
└── dashboard/          # Config Metabase
```

---

## 💡 Techniques Clés

**Profiling automatique** :
- Rapport statistique à chaque nouvelle ingestion
- Détection automatique des types et distributions

**Tests déclaratifs** :
- Expectations sur schéma, nulls, ranges, unicité
- Intégration CI/CD pour bloquer les pipelines défaillants

**Drift detection** :
- Comparaison distributions train vs serving
- Alertes sur dérive de features critiques

---

## 📚 Ressources

- [Great Expectations Docs](https://docs.greatexpectations.io/)
- [Evidently AI Docs](https://docs.evidentlyai.com/)
- [ydata-profiling](https://docs.profiling.ydata.ai/)
