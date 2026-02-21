#pragma once
#include <vector>
#include <iostream>

class SimpleMovingAverage {
private:
    std::vector<double> window; // Ring Buffer
    double sum;                 // Sum
    size_t headIndex;           // Writing pointer
    size_t period;              // N
    size_t count;               // Number of seen elements

public:
    SimpleMovingAverage(size_t periodN)
            : period(periodN), sum(0.0), headIndex(0), count(0) {
        window.resize(period, 0.0);
    }

    void addPrice(double price) {
        sum -= window[headIndex];
        sum += price;

        window[headIndex] = price;

        headIndex = (headIndex + 1) % period;

        if (count < period) {
            count++;
        }
    }

    double getValue() const {
        return (count == 0) ? 0.0 : sum / count;
    }

    bool isReady() const {
        return count >= period;
    }
};