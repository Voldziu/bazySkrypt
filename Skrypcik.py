import csv
import random
from faker import Faker
import psycopg2
from sqlalchemy import create_engine, Table, MetaData, select
from Generators import *
fake = Faker()

# Konfiguracja połączenia z bazą danych PostgreSQL
db_url = "postgresql://postgres:admin@localhost:5432/WaszaKlasa"  # Ustaw poprawne dane połączenia
engine = create_engine(db_url)
metadata = MetaData()
metadata.reflect(bind=engine)
# Test połączenia
with engine.connect() as connection:
    print("Połączono z bazą danych!")

accounts = metadata.tables["accounts"]
types = metadata.tables["types"]
profiles = metadata.tables["profiles"]


# Wstawienie danych do tabeli departments i pobranie wygenerowanych ID
with engine.connect() as conn:
    conn.execute(types.insert(), generate_types(5))
    conn.execute(types.insert(), generate_profiles(1000))
    conn.commit()