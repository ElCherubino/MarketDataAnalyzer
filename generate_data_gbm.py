import numpy as np
import pandas as pd
import os

TOTAL_TICKS = 30_000_000
S0 = 150.0
mu = 0.0000001
sigma = 0.0001
dt = 1

print(f"Generating {TOTAL_TICKS} ticks (Stress Test)...")

returns = np.random.normal(loc=(mu - 0.5 * sigma**2) * dt,
                           scale=sigma * np.sqrt(dt),
                           size=TOTAL_TICKS)
price_path = S0 * np.exp(np.cumsum(returns))

df = pd.DataFrame({
    'timestamp': np.arange(1700000000, 1700000000 + TOTAL_TICKS),
    'symbol': 'AAPL_STRESS',
    'price': np.round(price_path, 2),
    'volume': np.random.randint(10, 1000, size=TOTAL_TICKS)
})

os.makedirs('data', exist_ok=True)
df.to_csv('data/market_data.csv', header=False, index=False)

# Update session info to include the synthetic ticker name
with open('data/session_info.txt', 'w') as f:
    f.write("STRESS_TEST\nSYNTHETIC_GBM")

print("CSV of 30M lines generated.")