-- 1. Top Batsmen by Total Runs
SELECT batter, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

-- 2. Best Strike Rates (min 200 balls)
SELECT batter,
       SUM(batsman_runs) AS runs,
       COUNT(*) AS balls,
       ROUND(SUM(batsman_runs)*100.0/COUNT(*), 2) AS strike_rate
FROM deliveries
GROUP BY batter
HAVING COUNT(*) >= 200
ORDER BY strike_rate DESC
LIMIT 10;

-- 3. Toss Impact
SELECT 
    CASE WHEN toss_winner = winner THEN 'Won' ELSE 'Lost' END AS toss_result,
    COUNT(*) AS matches,
    ROUND(COUNT(*)*100.0/(SELECT COUNT(*) FROM matches), 2) AS percentage
FROM matches
GROUP BY toss_result;

-- 4. Venue Analysis
SELECT venue,
       COUNT(*) AS matches_hosted,
       SUM(CASE WHEN toss_decision='bat' THEN 1 ELSE 0 END) AS bat_first_count
FROM matches
GROUP BY venue
ORDER BY matches_hosted DESC
LIMIT 10;

-- 5. Team Wins
SELECT winner AS team, COUNT(*) AS total_wins
FROM matches
WHERE winner IS NOT NULL
GROUP BY winner
ORDER BY total_wins DESC;

-- 6. Death Overs Analysis
SELECT batting_team,
       ROUND(AVG(batsman_runs), 2) AS avg_death_runs,
       SUM(is_wicket) AS wickets_lost
FROM deliveries
WHERE over >= 15
GROUP BY batting_team
ORDER BY avg_death_runs DESC;