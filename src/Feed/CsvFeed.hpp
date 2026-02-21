#pragma once
#include "../Interfaces/IMarketDataSource.hpp"
#include <fstream>
#include <sstream>
#include <iostream>
#include <exception>

class CsvFeed : public IMarketDataSource {
private:
    std::ifstream file;

public:
    CsvFeed(const std::string& path) {
        file.open(path);
        if (!file.is_open()) {
            std::cerr << "Error: Could not open file " << path << std::endl;
        }
    }

    ~CsvFeed() {
        if (file.is_open()) file.close();
    }

    bool getNextTick(Tick& tick) override {
        std::string line;

        while (std::getline(file, line)) {
            if (line.empty()) {
                continue;
            }

            std::stringstream ss(line);
            std::string segment;

            try {
                std::getline(ss, segment, ',');
                tick.timestamp = std::stoll(segment);

                std::getline(ss, tick.symbol, ',');

                std::getline(ss, segment, ',');
                tick.price = std::stod(segment);

                std::getline(ss, segment, ',');
                tick.volume = std::stoi(segment);

                if (tick.timestamp > 1000000000) {
                    return true;
                }
            } catch (const std::exception& e) {
                continue;
            }
        }
        return false;
    }
};