#include <iostream>
#include <fstream>
#include <memory>
#include <iomanip>
#include <chrono>
#include <string>
#include "Feed/CsvFeed.hpp"
#include "Analytics/SimpleMovingAverage.hpp"
#include "Analytics/RSI.hpp"

int main() {
    std::string mode = "UNKNOWN";
    std::ifstream sessionFile("../data/session_info.txt");
    if (sessionFile.is_open()) { sessionFile >> mode; sessionFile.close(); }

    auto feed = std::make_unique<CsvFeed>("../data/market_data.csv");
    std::ofstream outFile("../data/results.csv");
    outFile << "timestamp,price,sma20,sma50,rsi" << std::endl;

    SimpleMovingAverage smaFast(20);
    SimpleMovingAverage smaSlow(50);
    RSI rsi(14);

    Tick tick;
    size_t tickCount = 0;
    auto start = std::chrono::high_resolution_clock::now();

    while (feed->getNextTick(tick)) {
        smaFast.addPrice(tick.price);
        smaSlow.addPrice(tick.price);
        rsi.addPrice(tick.price);

        outFile << tick.timestamp << "," << tick.price << ","
                << (smaFast.isReady() ? smaFast.getValue() : 0.0) << ","
                << (smaSlow.isReady() ? smaSlow.getValue() : 0.0) << ","
                << (rsi.isReady() ? rsi.getValue() : 50.0) << "\n";
        tickCount++;
    }

    auto end = std::chrono::high_resolution_clock::now();
    double time = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    double throughput = (tickCount / (time > 0 ? time : 1.0)) * 1000.0;

    std::cout << "\n=== Engine [" << mode << "] ===" << std::endl;
    std::cout << "Ticks: " << tickCount << " | Throughput: " << std::fixed << std::setprecision(0) << throughput << " ticks/s" << std::endl;
    return 0;
}