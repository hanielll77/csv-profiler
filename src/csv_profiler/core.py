from __future__ import annotations
import pandas as pd
from pathlib import Path

def profile_csv(path: str | Path) -> pd.DataFrame:
    """Read a CSV file and return a profiling summary (statistics + missing values)."""
  
    df = pd.read_csv(path)
    desc = df.describe(include="all").transpose()
    desc["missing"] = df.isna().sum()
    return desc

def clean_csv(path: str | Path, drop_duplicates: bool = True) -> pd.DataFrame:
    """Read a CSV, drop empty rows and optionally duplicates, then return cleaned data."""
  
    df = pd.read_csv(path)
    df = df.dropna(how="all")
    if drop_duplicates:
        df = df.drop_duplicates()
    return df
