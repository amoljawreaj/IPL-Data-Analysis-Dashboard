import sqlite3
import pandas as pd

conn = sqlite3.connect('data/ipl.db')

# Top 10 batsmen
print("=== TOP 10 BATSMEN ===")
query1 = """
SELECT batter, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10
"""
print(pd.read_sql_query(query1, conn))

# Team wins
print("\n=== TEAM WINS ===")
query2 = """
SELECT winner AS team, COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC
"""
print(pd.read_sql_query(query2, conn))

# Toss impact
print("\n=== TOSS IMPACT ===")
query3 = """
SELECT 
    CASE WHEN toss_winner = winner 
    THEN 'Toss Winner Won' 
    ELSE 'Toss Winner Lost' END AS result,
    COUNT(*) AS matches
FROM matches
GROUP BY result
"""
print(pd.read_sql_query(query3, conn))

# Best strike rates
print("\n=== BEST STRIKE RATES (min 200 balls) ===")
query4 = """
SELECT batter,
       SUM(batsman_runs) AS runs,
       COUNT(*) AS balls,
       ROUND(SUM(batsman_runs)*100.0/COUNT(*), 2) AS strike_rate
FROM deliveries
GROUP BY batter
HAVING COUNT(*) >= 200
ORDER BY strike_rate DESC
LIMIT 10
"""
print(pd.read_sql_query(query4, conn))

# Top venues
print("\n=== TOP VENUES ===")
query5 = """
SELECT venue, COUNT(*) AS matches_hosted
FROM matches
GROUP BY venue
ORDER BY matches_hosted DESC
LIMIT 10
"""
print(pd.read_sql_query(query5, conn))

# Death overs analysis
print("\n=== DEATH OVERS ANALYSIS ===")
query6 = """
SELECT batting_team,
       ROUND(AVG(batsman_runs), 2) AS avg_death_runs,
       SUM(is_wicket) AS wickets_lost
FROM deliveries
WHERE over >= 15
GROUP BY batting_team
ORDER BY avg_death_runs DESC
"""
print(pd.read_sql_query(query6, conn))

conn.close()
print("\nAll queries executed successfully!")