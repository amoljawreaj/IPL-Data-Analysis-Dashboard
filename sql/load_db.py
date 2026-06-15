import sqlite3
import pandas as pd

conn = sqlite3.connect('data/ipl.db')

matches = pd.read_csv('data/datacleaned/matches_cleaned.csv')
deliveries = pd.read_csv('data/datacleaned/deliveries_final.csv')

matches.to_sql('matches', conn, if_exists='replace', index=False)
deliveries.to_sql('deliveries', conn, if_exists='replace', index=False)

conn.close()
print("Database created successfully!")