import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import os

# 1. Read Mode and Ticker from session metadata
mode = "Unknown"
ticker = "UNKNOWN_ASSET"
if os.path.exists('data/session_info.txt'):
    with open('data/session_info.txt', 'r') as f:
        lines = f.readlines()
        if len(lines) > 0: mode = lines[0].strip()
        if len(lines) > 1: ticker = lines[1].strip()

df = pd.read_csv('data/results.csv')
df['date'] = pd.to_datetime(df['timestamp'], unit='s')
total_ticks = len(df)
total_span_days = (df['date'].max() - df['date'].min()).days

# MODIFICATION ICI : [2.5, 1.5, 0.8] donne plus de hauteur à la fenêtre du milieu
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12),
                                    gridspec_kw={'height_ratios': [2.5, 1.8, 0.8], 'hspace': 0.4})

# --- TOP: OVERVIEW ---
skip = max(1, total_ticks // 2000)
df_over = df.iloc[::skip]

ax1.plot(df_over['date'], df_over['price'], color='black', linewidth=1)
ax1.set_title(f"{ticker} Market Overview [{mode}] - Span: {total_span_days} days", pad=20, fontweight='bold')

if total_span_days > 500:
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
else:
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax1.grid(True, alpha=0.2)
ax1.set_ylabel("Price ($)")
ax1.tick_params(labelbottom=True)

# --- MIDDLE: ZOOM (More spacious now) ---
ZOOM_AMOUNT = 200
df_z = df.tail(ZOOM_AMOUNT).copy()
df_z.replace(0, np.nan, inplace=True)

ax2.plot(df_z['date'], df_z['price'], color='black', label="Price", linewidth=1)
ax2.plot(df_z['date'], df_z['sma20'], color='blue', label="SMA 20", linewidth=0.8, linestyle='--')
ax2.plot(df_z['date'], df_z['sma50'], color='orange', label="SMA 50", linewidth=0.8, linestyle='--')
ax2.set_title(f"Indicators Zoom (Last {ZOOM_AMOUNT} ticks)", fontsize=10)
ax2.legend(loc='upper left', fontsize='small')
ax2.grid(True, alpha=0.3)
ax2.set_ylabel("Price ($)")
ax2.tick_params(labelbottom=False)

# --- BOTTOM: RSI ---
ax3.plot(df_z['date'], df_z['rsi'], color='purple', linewidth=1)
ax3.axhline(70, color='red', linestyle=':', alpha=0.5)
ax3.axhline(30, color='green', linestyle=':', alpha=0.5)
ax3.set_ylim(0, 100)
ax3.set_ylabel("RSI")
ax3.set_title("RSI Momentum", fontsize=10)
ax3.tick_params(labelbottom=False)

plt.savefig('analysis_report.png', bbox_inches='tight')
print(f"Report generated for {ticker}: analysis_report.png")
plt.show()