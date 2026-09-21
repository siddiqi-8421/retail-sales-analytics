# src/load_to_db.py
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/processed/superstore_clean.csv")
engine = create_engine("sqlite:///data/processed/superstore.db")
df.to_sql("orders", engine, if_exists="replace", index=False)