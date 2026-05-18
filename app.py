import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Crypto Sentiment Dashboard",
    layout="wide"
)

st.title("Crypto Sentiment Trading Dashboard")

# Load dataset
df = pd.read_csv("final_merged_dataset.csv")

# Sidebar filter
sentiment = st.selectbox(
    "Select Sentiment",
    sorted(df['sentiment'].dropna().unique())
)

# Filtered dataframe
filtered = df[
    df['sentiment'] == sentiment
]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Trades",
    len(filtered)
)

col2.metric(
    "Average PnL",
    f"{filtered['closed_pnl'].mean():.2f}"
)

col3.metric(
    "Average Trade Size",
    f"{filtered['size_usd'].mean():.2f}"
)

# Scatter Plot
fig = px.scatter(
    filtered.sample(min(3000, len(filtered))),
    x='size_usd',
    y='closed_pnl',
    color='side',
    hover_data=['coin'],
    title='Trade Performance by Market Sentiment'
)

# ── Analysis Charts Section ────────────────────────────────────────────────
from PIL import Image
from pathlib import Path

st.header("Analysis Visualizations")

OUTPUT_DIR = Path("outputs")

chart_explanations = {
    "01_sentiment_distribution.png":
        "Shows the distribution of market sentiment states. "
        "Helps identify whether the market spent more time in Fear or Greed conditions.",

    "02_sentiment_timeline.png":
        "Displays how market sentiment changed over time. "
        "Useful for observing sentiment cycles and volatility periods.",

    "03_trading_activity.png":
        "Illustrates trading activity across different sentiment conditions. "
        "Higher activity during Greed may indicate increased market participation.",

    "04_buy_sell_distribution.png":
        "Compares BUY vs SELL behavior across sentiment states. "
        "Helps identify whether traders become more aggressive during Greed.",

    "05_profitability_by_sentiment.png":
        "Shows average profitability under different market sentiments. "
        "Useful for detecting favorable trading environments.",

    "06_pnl_boxplot_violin.png":
        "Displays the distribution of profit and loss values. "
        "Highlights volatility, outliers, and risk differences.",

    "07_trade_size_by_sentiment.png":
        "Analyzes how trade sizes vary under different sentiment conditions. "
        "Can reveal increased risk-taking during Greed.",

    "08_timeseries_pnl_sentiment.png":
        "Tracks profitability over time alongside sentiment trends. "
        "Useful for identifying periods of strong or weak trader performance.",

    "09_correlation_matrix.png":
        "Shows relationships between numeric trading variables. "
        "Helps identify factors strongly associated with profitability.",

    "10_winrate_heatmap.png":
        "Displays win rates across different sentiment categories. "
        "Useful for understanding trading consistency.",

    "11_coin_sentiment_heatmap.png":
        "Shows how different coins perform under varying sentiment conditions.",

    "12_contrarian_scatter.png":
        "Highlights traders who perform well during Fear conditions. "
        "Useful for identifying contrarian strategies.",

    "13_trader_segments.png":
        "Visualizes trader clusters based on behavior and profitability. "
        "Helps identify whales, aggressive traders, and consistent performers.",

    "14_segment_sentiment_heatmap.png":
        "Shows how different trader segments behave under various sentiment conditions.",

    "15_ml_evaluation.png":
        "Displays machine learning evaluation metrics including confusion matrix, ROC curves, and feature importance.",

    "16_model_comparison.png":
        "Compares machine learning models based on predictive performance metrics."
}

# Display all charts
for chart_file in sorted(OUTPUT_DIR.glob("*.png")):

    st.subheader(chart_file.stem.replace("_", " ").title())

    image = Image.open(chart_file)

    st.image(
        image,
        width='stretch'
    )

    explanation = chart_explanations.get(
        chart_file.name,
        "Visualization generated from trading analysis."
    )

    st.markdown(f"**Explanation:** {explanation}")

    st.divider()

fig.update_layout(
    template='plotly_dark',
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ── Optional Trade Preview ────────────────────────────────────────────────
with st.expander("View Sample Trade Data"):

    preview_cols = [
        'coin',
        'side',
        'size_usd',
        'closed_pnl',
        'sentiment',
        'timestamp_ist'
    ]

    st.dataframe(
        filtered[preview_cols].head(20),
        width='stretch'
    )