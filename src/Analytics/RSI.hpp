#pragma once
#include <iostream>
#include <cmath>

class RSI {
private:
    size_t period;
    double avgGain;
    double avgLoss;
    double lastPrice;
    size_t count;
    bool isInitialized;

public:
    RSI(size_t periodN)
            : period(periodN), avgGain(0.0), avgLoss(0.0),
              lastPrice(0.0), count(0), isInitialized(false) {}

    void addPrice(double currentPrice) {
        if (count == 0) {
            lastPrice = currentPrice;
            count++;
            return;
        }

        double change = currentPrice - lastPrice;
        double currentGain = (change > 0) ? change : 0.0;
        double currentLoss = (change < 0) ? -change : 0.0;

        if (count <= period) {
            avgGain += currentGain;
            avgLoss += currentLoss;
            if (count == period) {
                avgGain /= period;
                avgLoss /= period;
                isInitialized = true;
            }
        }
        else {
            avgGain = ((avgGain * (period - 1)) + currentGain) / period;
            avgLoss = ((avgLoss * (period - 1)) + currentLoss) / period;
        }

        lastPrice = currentPrice;
        count++;
    }

    double getValue() const {
        if (!isInitialized || avgLoss == 0) {
            return 100.0;
        }
        double rs = avgGain / avgLoss;
        return 100.0 - (100.0 / (1.0 + rs));
    }

    bool isReady() const {
        return isInitialized;
    }
};