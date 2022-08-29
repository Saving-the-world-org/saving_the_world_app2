import pandas as pd
import numpy as np
from pathlib import Path
from sqlalchemy import inspect, create_engine
connection_string = 'sqlite:///./src/data/stw_data.db'
engine = create_engine(connection_string)
insp = inspect(engine)

def init_data():
    cities_df = pd.read_csv(Path("./src/data/cities.csv"))
    donations_df = pd.read_csv(Path("./src/data/donations.csv"))
    organizations_df = pd.read_csv(Path("./src/data/organizations.csv"))
    recipients_df = pd.read_csv(Path("./src/data/recipients.csv"))
    cities_df.to_sql('CITIES', engine, index=False, if_exists='replace')
    donations_df.to_sql('DONATIONS', engine, index=False, if_exists='replace')
    organizations_df.to_sql('ORGANIZATIONS', engine, index=False, if_exists='replace')
    recipients_df.to_sql('RECIPIENTS', engine, index=False, if_exists='replace')

def get_data(query):
    df = pd.read_sql_query(query, con=engine)
    return df