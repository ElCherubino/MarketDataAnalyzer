import yfinance as yf
import pandas as pd
import os
import sys

# 1. Dynamic Ticker Logic
# Uses the first argument if provided (e.g., python3 retrieve_data.py TSLA), else defaults to AAPL
ticker = sys.argv[1].upper() if len(sys.argv) > 1 else "AAPL"

print(f"--- Fetching REAL {ticker} Historical Data (5 Years) ---")

data = yf.download(ticker, period="5y", interval="1d")

# Safety check in case of a typo in the ticker
if data.empty:
    print(f"Error: No data found for {ticker}. Please check the symbol.")
    sys.exit(1)

# Clean multi-index columns if present
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

df = pd.DataFrame({
    'timestamp': [int(pd.Timestamp(d).timestamp()) for d in data.index],
    'symbol': ticker,
    'price': data['Close'].values.flatten(),
    'volume': data['Volume'].values.flatten()
})

df = df.dropna()

os.makedirs('data', exist_ok=True)
df.to_csv('data/market_data.csv', header=False, index=False)

# 2. Save both the Mode and the Ticker for the C++ engine and the Plotter
with open('data/session_info.txt', 'w') as f:
    f.write(f"REAL_DATA\n{ticker}")

print(f"Success! {len(df)} lines written for {ticker}.")