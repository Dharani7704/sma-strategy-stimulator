# fetch_data.py

import yfinance as yf
import pandas as pd

def fetch_data(ticker='AAPL', period='3mo', interval='1d'):
    try:
        df = yf.download(ticker, period=period, interval=interval)
        df.reset_index(inplace=True)
        if 'Date' not in df.columns:
            df.rename(columns={'index': 'Date'}, inplace=True)
        return df
    except Exception as e:
        print("Error fetching data:", e)
        return pd.DataFrame()
