# Bitcoin Sentiment × Hyperliquid Trader Analysis

A production-quality data science and machine learning project exploring the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance on the Hyperliquid decentralized exchange.

---

# Project Overview

This project investigates how market psychology influences trader behavior and profitability in crypto markets.

Key questions explored:

- Do traders perform better during Fear or Greed?
- Does market sentiment influence leverage and position sizing?
- Can profitable contrarian traders be identified?
- Can machine learning predict profitable trades using sentiment data?

The project combines:
- Exploratory Data Analysis (EDA)
- Statistical Testing
- Risk Analytics
- Trader Segmentation
- Machine Learning
- Interactive Dashboarding

---

# Features

## Data Analysis
- Market sentiment distribution analysis
- Profitability analysis across sentiment states
- Trading activity and behavior analysis
- Buy vs Sell behavioral patterns
- Time-series sentiment analysis

## Statistical Analysis
- T-tests for profitability comparison
- ANOVA across sentiment groups
- Correlation analysis
- Volatility analysis

## Risk Analytics
- Sharpe Ratio
- Maximum Drawdown
- PnL volatility by sentiment

## Machine Learning
- Trade profitability prediction
- Model comparison
- ROC analysis
- Feature importance analysis

## Trader Segmentation
- KMeans clustering
- Contrarian trader detection
- Whale vs retail analysis

## Interactive Dashboard
- Streamlit dashboard
- Interactive Plotly visualizations
- Sentiment filters
- Dynamic chart rendering

---

# Folder Structure

```text
btc_sentiment_analysis/
├── data/
│   ├── fear_greed.csv
│   └── hyperliquid_trades.csv
│
├── outputs/
│   ├── 01_sentiment_distribution.png
│   ├── ...
│   └── 16_model_comparison.png
│
├── notebooks/
│   └── analysis.ipynb
│
├── app.py                     # Streamlit dashboard
├── requirements.txt
├── README.md
└── final_merged_dataset.csv
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repo-url>
cd btc_sentiment_analysis
```

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Notebook

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/analysis.ipynb
```

---

# Running the Streamlit Dashboard

Start the dashboard:

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

Default URL:

```text
http://localhost:8501
```

---

# Dataset Information

## 1. Bitcoin Fear & Greed Dataset

Columns:
- timestamp
- value
- classification
- date

Tracks Bitcoin market sentiment from:
- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

---

## 2. Hyperliquid Historical Trader Dataset

Includes:
- account
- coin
- execution price
- trade size
- side
- pnl
- timestamps
- fees
- leverage-related metrics

---

# Visualizations Generated

The project generates 16+ professional visualizations including:

| Chart | Purpose |
|---|---|
| Sentiment Distribution | Market psychology overview |
| Trading Activity | Activity vs sentiment |
| Profitability by Sentiment | PnL comparison |
| Correlation Matrix | Feature relationships |
| Contrarian Scatter | Fear-market winners |
| Trader Segments | Behavioral clustering |
| ML Evaluation | Confusion matrix + ROC |
| Model Comparison | ML benchmark |

All charts are saved automatically inside:

```text
outputs/
```

---

# Machine Learning Pipeline

Models implemented:
- Logistic Regression
- Random Forest
- Gradient Boosting

Features used:
- sentiment score
- trade size
- trading direction
- position metrics
- time-based features

Evaluation metrics:
- Accuracy
- ROC-AUC
- Confusion Matrix
- Feature Importance

---

# Key Findings

- Traders show higher activity during Greed periods
- Extreme Greed correlates with elevated risk-taking
- Fear periods often provide better risk-adjusted opportunities
- Contrarian traders outperform during panic markets
- Sentiment score contributes meaningfully to ML predictions

---

# Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Analysis | pandas, numpy |
| Visualization | matplotlib, seaborn, plotly |
| Machine Learning | scikit-learn |
| Dashboard | Streamlit |

---

# Limitations

- Sentiment data is market-wide, not trader-specific
- Hyperliquid data may not represent the entire crypto ecosystem
- Correlation does not imply causation
- Limited leverage information in some records

---

# Future Improvements

Potential future upgrades:

- Real-time sentiment API integration
- Live trading signal generation
- Deep learning models
- Reinforcement learning strategies
- Multi-exchange analysis
- Deployment to Streamlit Cloud

---

# Author

Developed as a quantitative crypto trading analytics and machine learning project focused on behavioral finance and market sentiment analysis.