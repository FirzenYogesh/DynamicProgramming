cmake_minimum_required(VERSION 3.8)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

set(SOURCE_FILES 01KnapSack.cpp BinomialCoefficient.cpp CoinChangeMinCoins.cpp)
add_executable(01KnapSack 01KnapSack.cpp)
add_executable(BinomialCoefficient BinomialCoefficient.cpp)
add_executable(CoinChangeMinCoins CoinChangeMinCoins.cpp)