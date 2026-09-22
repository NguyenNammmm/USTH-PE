import pandas as pd
from sqlalchemy import text
def read_csv_scores(path): return pd.read_csv(path,na_values=[""])
def read_excel_scores(path): return pd.read_excel(path,sheet_name="Scores",usecols=["id","score"])
def read_database(engine):
    with engine.connect() as connection:
        return pd.read_sql_query(text("SELECT id,score FROM scores ORDER BY id"),connection)
