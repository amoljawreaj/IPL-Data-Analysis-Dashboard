# 🏏 IPL Data Analysis Dashboard

An end-to-end data analytics project analyzing 15+ seasons of IPL (2008–2024) match and ball-by-ball data to uncover insights on team performance, player consistency, toss impact, and venue trends — built using Python, SQL, and an interactive Plotly Dash dashboard.

## 📌 Business Problem

A new IPL franchise's management wants data-driven insights to:
- Identify which players to target in auctions based on consistency and strike rate
- Understand how toss decisions and venues impact match outcomes
- Benchmark team performance across seasons to find areas of improvement

This project analyzes historical IPL data to answer these questions and presents findings through an interactive dashboard.

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Languages | Python, SQL |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Plotly, Dash |
| Database | SQLite |
| Visualization | Plotly Dash, Power BI (planned), Excel |
| Version Control | Git, GitHub |

## 📂 Project Structure

```
IPL-Data-Analysis-Dashboard/
│
├── data/
│   ├── dataraw/          # Original Kaggle CSVs (matches.csv, deliveries.csv)
│   ├── datacleaned/       # Cleaned datasets after preprocessing
│   ├── dataprocessed/     # Aggregated KPI tables for dashboard/BI tools
│   └── ipl.db              # SQLite database used for SQL analysis
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb     # Missing values, name standardization, feature engineering
│   ├── 02_eda.ipynb               # Exploratory analysis & visualizations
│   └── 03_kpi_analysis.ipynb      # KPI computation & export
│
├── sql/
│   ├── analysis_queries.sql       # Core analysis queries
│   ├── load_db.py                 # Loads cleaned CSVs into SQLite
│   └── test_queries.py            # Runs and prints query results
│
├── dashboard/
│   └── app.py                     # Interactive Plotly Dash dashboard
│
├── visuals/                       # Exported chart images (PNG)
│
├── requirements.txt
└── README.md
```

## 🔄 Workflow

```
Raw CSV (Kaggle)
   → Data Cleaning & Feature Engineering (Pandas)
   → Cleaned CSVs → SQLite Database
   → SQL Analysis (top batsmen, toss impact, venue trends, death overs)
   → EDA & KPI Computation (Python)
   → Aggregated tables exported
   → Interactive Dashboard (Plotly Dash)
```

## 🧹 Data Cleaning & Preprocessing

- Standardized inconsistent team names across seasons (e.g., Delhi Daredevils → Delhi Capitals)
- Removed abandoned matches with no result
- Engineered new features: `is_boundary`, `is_wicket`, and match `phase` (Powerplay / Middle / Death)
- Converted date fields and derived `season` from match date

## 📊 Key KPIs Computed

| KPI | Description |
|---|---|
| Win Percentage | Wins / Total matches played, per team |
| Top Batsmen | Total runs scored across all seasons |
| Strike Rate | Runs per 100 balls (min. 200 balls faced) |
| Powerplay Average | Average runs scored in overs 1–6 |
| Boundary Percentage | % of balls faced resulting in a boundary |
| Player Consistency | Standard deviation of runs per innings (min. 20 innings) |

## 🔍 SQL Analysis

Six core SQL queries were written against a SQLite database (`data/ipl.db`) covering:
- Top batsmen by total runs
- Best strike rates (qualified players)
- Toss impact on match outcome
- Venue-wise match and scoring trends
- Team-wise win totals
- Death-overs (15–20) scoring and wicket analysis

Full queries available in [`sql/analysis_queries.sql`](sql/analysis_queries.sql).

## 📈 Dashboard

An interactive dashboard was built using Plotly Dash, featuring:
- KPI cards (Total Matches, Total Runs, Total Sixes, Total Fours)
- Team filter dropdown
- Win percentage by team
- Top 10 batsmen and strike rate leaderboards
- Toss impact visualization
- Season-wise run trend
- Venue analysis
- Team vs. match-phase performance heatmap

Run locally:
```bash
cd dashboard
python app.py
```
Then open `http://127.0.0.1:8050` in your browser.

## 💡 Key Insights

- Toss winners go on to win the match roughly **51%** of the time, suggesting a slight but real advantage rather than a dominant factor
- Powerplay scoring patterns vary meaningfully by team, indicating differing opening strategies
- A small group of top batsmen account for a disproportionate share of total runs scored across all seasons
- Death-overs performance (economy and strike rate) is a key differentiator between consistently successful and inconsistent teams

## ▶️ How to Run This Project

```bash
# 1. Clone the repository
git clone https://github.com/amoljawreaj/IPL-Data-Analysis-Dashboard.git
cd IPL-Data-Analysis-Dashboard

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run notebooks in order (via Jupyter or VS Code)
notebooks/01_data_cleaning.ipynb
notebooks/02_eda.ipynb
notebooks/03_kpi_analysis.ipynb

# 5. (Optional) Load data into SQLite and run SQL queries
python sql/load_db.py
python sql/test_queries.py

# 6. Launch the interactive dashboard
cd dashboard
python app.py
```

## 📁 Dataset Source

IPL Complete Dataset (2008–2024) — match-level (`matches.csv`) and ball-by-ball (`deliveries.csv`) data sourced from Kaggle.

## 🚀 Future Improvements

- Build a predictive model for win probability based on first-innings score
- Add a player auction value prediction model
- Integrate Power BI dashboard as an alternative visualization layer
- Automate data refresh via API for current-season data

## 👤 Author

**Amol Jawre**
B.Tech Information Technology (3rd Year)
[GitHub](https://github.com/amoljawreaj) · 

---
*This project was built as a self-driven learning exercise to practice end-to-end data analytics: cleaning, SQL, KPI design, and dashboarding.*
