import sqlite3
import pandas as pd

# Wczytanie danych z plików CSV
stations_data = pd.read_csv("clean_stations.csv")
measure_data = pd.read_csv("clean_measure.csv")

print(stations_data)
print(measure_data)

# Utworzenie połączenia z bazą danych
conn = sqlite3.connect("database.db")

# Zapisanie danych do bazy danych jako tabele
stations_data.to_sql("stations", conn, if_exists="replace", index=False)
measure_data.to_sql("measurements", conn, if_exists="replace", index=False)

# Zapytanie SQL do wyświetlenia pierwszych 5 wierszy tabeli "stations"
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)
