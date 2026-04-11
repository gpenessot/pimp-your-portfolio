# ⚙️ ETL Open Data Gouvernement

> Data warehouse unifié pour centraliser et explorer 50+ datasets publics français.

## 📊 Problématique Business

**Contexte** : Les données publiques sont éparpillées sur des portails hétérogènes et mal formatées.

**Défi** : Ingérer des formats variés (CSV, JSON, XML, APIs) depuis des sources multiples de manière automatisée.

**Objectif** : Créer un **data warehouse unifié** avec portail d'exploration et API pour analyses citoyennes.

---

## 🗂️ Dataset

- **Sources** :
  - [data.gouv.fr API](https://www.data.gouv.fr/api/1/) — base endpoint (`/api/1/`)
  - [INSEE API](https://api.insee.fr/catalogue/)
  - [OpenDataSoft](https://public.opendatasoft.com/api/v2/)
- **Volume** : 100+ datasets publics
- **Formats** : CSV, JSON, XML, APIs REST

---

## 🎯 Critères de Réussite

| Métrique | Objectif |
|----------|----------|
| **Datasets intégrés** | 50+ sources |
| **Fréquence update** | Quotidienne automatique |
| **Qualité données** | Checks automatisés sur chaque ingestion |
| **Documentation API** | 100% endpoints documentés |

---

## 🛠️ Stack

- **ETL** : Python, Airbyte
- **Storage** : DuckDB
- **Qualité** : Great Expectations
- **API** : FastAPI, Strawberry GraphQL
- **Portal** : Datasette

---

## 📦 Structure

```
12-etl-open-data-gouv/
├── pipelines/          # Scripts d'ingestion par source
├── src/                # ETL générique, quality checks
├── api/                # FastAPI + GraphQL
├── catalog/            # Métadonnées datasets
└── data/               # DuckDB storage (non versionné)
```

---

## 💡 Techniques Clés

**Ingestion générique** :
- Détection automatique du format source
- Normalisation des schémas hétérogènes
- Catalogue avec métadonnées automatiques

**Data Quality** :
- Validation schéma à chaque ingestion
- Tests de distribution et complétude
- Alertes sur anomalies

---

## 📚 Ressources

- [data.gouv.fr — Guide API](https://guides.data.gouv.fr/api-de-data.gouv.fr/prise-en-main)
- [Great Expectations Docs](https://docs.greatexpectations.io/)
- [Datasette Docs](https://docs.datasette.io/)
