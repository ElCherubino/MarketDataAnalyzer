cmake_minimum_required(VERSION 3.10)
project(MarketDataAnalyzer)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(src)

add_executable(MarketAnalyzer src/main.cpp)