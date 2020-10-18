# SentimentTrading
## Project Summary
An algorithmic stock trading program driven by a sentiment analysis of the most popular trading forum in the world, WallStreetBets.

## What It Does
This program compares the performance of our sentiment-driven stock trading algorithm, SentimentStrategy, against the performance of an extremely common stock trading signal, the simple moving average (SMA), across 20 different companies within the S&P500 stock index from 1/1/2020 to the current date. 

## Our Findings

## How It Works
- Simple Moving Average
  - Price average is taken within a given window. Trade calls are generated when two averages cross each other.
- WallStreetBets
  - A subreddit known for its young and brash investors, the perfect example of the traders driving the volatility of the post coronavirus market.
- Firebase/pyrebase
  - Allowed us to store sentiment data to use with backtrader.
- Backtrader
  - A python module that backtests trading strategies against a Yahoo Finance price data.
- Data analysis tools: 
  - Vader sentiment analysis - used to obtain numerical data representing the positive or negative sentiment of each comment.
  - matplotlib - used for plotting graphical representations of stock data.
  - pushshift.io api - used to collect comment data from reddit.
