#pragma once
#include "../Types.hpp"


class IMarketDataSource {
public:
    virtual ~IMarketDataSource() = default;

    virtual bool getNextTick(Tick& tick) = 0;
};