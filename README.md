--- Activate virtual environments ---
source venv/bin/activate
pip install numpy pandas matplotlib

--- Generate data ---
python3 generate_data_gbm.py
// OR Retrieve real data (AAPL by default)
python3 retrieve_data.py
// OR retrieve a specific data
python3 retrieve_data.py TSLA

--- Compile project ---
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make

--- Executing the binary ---
./MarketAnalyzer

--- Plot the results from data/results.csv ---
cd ..
python3 plot_results.py