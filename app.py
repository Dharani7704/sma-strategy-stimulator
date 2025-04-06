# app.py

import streamlit as st
import matplotlib.pyplot as plt
from fetch_data import fetch_data
from sma_strategy import apply_sma_strategy

st.set_page_config(page_title="SMA Strategy Simulator", layout="wide")
st.title("📊 Simple Moving Average (SMA) Strategy Simulator")

ticker = st.text_input("Enter Stock Ticker (Example: AAPL, TSLA, INFY.NS)", value='AAPL')
short_window = st.slider("Short Window (SMA)", 2, 50, 5)
long_window = st.slider("Long Window (SMA)", 10, 100, 20)

if st.button("Run Strategy"):
    df = fetch_data(ticker)
    
    if not df.empty and 'Date' in df.columns:
        df = apply_sma_strategy(df, short_window, long_window)

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df['Date'], df['Close'], label='Close Price', color='black')
        ax.plot(df['Date'], df['SMA_Short'], label=f'{short_window}-Day SMA', color='blue')
        ax.plot(df['Date'], df['SMA_Long'], label=f'{long_window}-Day SMA', color='red')

        buy = df[df['Signal'] == 1]
        sell = df[df['Signal'] == -1]
        ax.scatter(buy['Date'], buy['Close'], label='Buy', marker='^', color='green')
        ax.scatter(sell['Date'], sell['Close'], label='Sell', marker='v', color='red')

        ax.set_title(f"SMA Strategy for {ticker}")
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("Failed to fetch data. Please check your ticker or internet connection.")
