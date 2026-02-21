# 📈 Market Data Analyzer & C++ Quant Engine

A high-performance quantitative analysis pipeline that combines the speed of **C++** for computing technical indicators with the flexibility of **Python** for data ingestion and data visualization.

## 🚀 Overview
This project simulates the core component of a quantitative trading system: processing high-frequency tick data (or daily historical data) to compute real-time technical indicators. 

It features two main operational modes:
1. **Real Market Data:** Fetches 5 years of historical data for any stock ticker via the `yfinance` API.
2. **Stress Test (Synthetic):** Generates 30 million ticks using a Geometric Brownian Motion (GBM) model to benchmark the C++ engine's throughput.

## 🧠 System Architecture

The project is split into two distinct pipelines to maximize both performance and usability:

* **Data Ingestion & Visualization (Python):**
  * `retrieve_data.py`: Fetches real-world market data and formats it into a standardized CSV feed.
  * `generate_data_gbm.py`: Generates massive synthetic datasets for C++ performance profiling.
  * `plot_results.py`: Reads the engine's output and generates a comprehensive Matplotlib chart (Price, SMA, RSI).
* **Quantitative Engine (C++):**
  * Reads the feed and processes ticks sequentially.
  * Computes **Simple Moving Averages (SMA 20 & 50)** using optimized Ring Buffers, achieving $O(1)$ time complexity per tick insertion.
  * Computes the **Relative Strength Index (RSI 14)** with efficient running averages.
  * Tracks processing time and outputs total throughput (ticks per second).

## ⚙️ Build & Installation

### 1. Compile the C++ Engine
```bash
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make
cd ..
```

### 2. Set up the Python Environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install numpy pandas matplotlib yfinance
```

## 📊 Usage Instructions

### Scenario A: Real Market Analysis (e.g., TSLA)
```bash
# 1. Fetch real market data (defaults to AAPL if no argument is provided)
python3 retrieve_data.py TSLA

# 2. Run the C++ processing engine
cd build && ./MarketAnalyzer && cd ..

# 3. Generate the analytical visual report
python3 plot_results.py
```

### Scenario B: High-Frequency Stress Test
```bash
# 1. Generate 30M synthetic ticks
python3 generate_data_gbm.py

# 2. Benchmark the C++ engine
cd build && ./MarketAnalyzer && cd ..

# 3. Plot the final segment
python3 plot_results.py
```
---
*Developed by Victor Rigot.*
