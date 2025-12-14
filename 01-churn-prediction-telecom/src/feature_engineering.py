"""
Feature Engineering pour la prédiction de churn
"""
import pandas as pd
import numpy as np
from typing import Tuple


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Créé des features custom pour améliorer la prédiction

    Args:
        df: DataFrame avec colonnes brutes

    Returns:
        DataFrame avec features additionnelles
    """
    df = df.copy()

    # 1. Ratio prix/ancienneté (indicateur augmentation)
    df['price_tenure_ratio'] = df['MonthlyCharges'] / (df['tenure'] + 1)

    # 2. Engagement services (nombre de services souscrits)
    service_cols = [
        'PhoneService', 'InternetService', 'OnlineSecurity',
        'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies'
    ]
    df['total_services'] = (df[service_cols] == 'Yes').sum(axis=1)

    # 3. Has internet mais pas de protection
    df['internet_no_protection'] = (
        (df['InternetService'] != 'No') &
        (df['OnlineSecurity'] == 'No') &
        (df['TechSupport'] == 'No')
    ).astype(int)

    # 4. Segmentation ancienneté
    df['tenure_segment'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 60, 100],
        labels=['<1yr', '1-2yr', '2-5yr', '>5yr']
    )

    # 5. Senior avec dependents (segment fragile)
    df['senior_with_dependents'] = (
        (df['SeniorCitizen'] == 1) &
        (df['Dependents'] == 'Yes')
    ).astype(int)

    return df


def preprocess_data(
    df: pd.DataFrame,
    target_col: str = 'Churn'
) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prétraitement complet des données

    Args:
        df: DataFrame brut
        target_col: Nom de la colonne target

    Returns:
        X: Features preprocessed
        y: Target
    """
    df = df.copy()

    # Gestion TotalCharges (parfois string avec espaces)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(0, inplace=True)

    # Encoder target (Yes → 1, No → 0)
    y = (df[target_col] == 'Yes').astype(int)

    # Drop target et customerID
    X = df.drop(columns=[target_col, 'customerID'], errors='ignore')

    # Feature engineering
    X = create_features(X)

    # Encoder variables catégorielles
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

    return X, y
