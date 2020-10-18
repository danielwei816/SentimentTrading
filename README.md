# SentimentTrading
## Project Summary
An algorithmic stock trading program driven by a sentiment analysis of the most popular trading forum in the world, WallStreetBets.

## What It Does
This program compares the performance of our sentiment-driven stock trading algorithm, SentimentStrategy, against the performance of an extremely common stock trading signal, the simple moving average (SMA), across 20 different companies within the S&P500 stock index from 1/1/2020 to the current date. 

## How It Works
- Simple Moving Average
  - Price average is taken within a given window. Trade calls are generated when two averages cross each other.
- WallStreetBets
  - A subreddit known for its young and brash investors, the perfect example of the traders driving the volatility of the post coronavirus market.
- Firebase/pyrebase
  - Allowed us to store sentiment data to use with backtrader.
    - https://github.com/thisbejim/Pyrebase
- Backtrader
  - A python module that backtests trading strategies against a Yahoo Finance price data.
    - https://github.com/mementum/backtrader
- Data analysis tools: 
  - Vader sentiment analysis - used to obtain numerical data representing the positive or negative sentiment of each comment.
    - https://github.com/cjhutto/vaderSentiment
  - matplotlib - used for plotting graphical representations of stock data.
    - https://github.com/matplotlib/matplotlib
  - pushshift.io api - used to collect comment data from reddit.
    - https://github.com/pushshift/api

## Our Findings
```
---MSFT---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 101662.76
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99975.16
SENTIMENT WINS
---AAPL---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100262.65
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100000.48
SENTIMENT WINS
---AMD---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100211.36
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100014.60
SENTIMENT WINS
---BA---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99909.20
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99974.24
SMA WINS
---AMZN---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 134819.77
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100288.55
SENTIMENT WINS
---DIS---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99923.99
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99993.63
SMA WINS
---FB---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 102272.17
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100017.78
SENTIMENT WINS
---NVDA---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 109068.96
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100053.90
SENTIMENT WINS
---MGM---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100108.19
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99995.70
SENTIMENT WINS
---PPL---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99991.81
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99998.16
SMA WINS
---AAL---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99990.84
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99988.57
SENTIMENT WINS
---ATVI---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100465.89
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100006.03
SENTIMENT WINS
---NFLX---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 105256.63
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100095.39
SENTIMENT WINS
---INTC---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100045.10
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99988.86
SENTIMENT WINS
---JPM---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99833.46
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99978.02
SMA WINS
---GE---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99937.86
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99996.77
SMA WINS
---BAC---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99909.08
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99994.66
SMA WINS
---CSCO---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99955.01
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99990.58
SMA WINS
---EBAY---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100573.02
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100020.63
SENTIMENT WINS
---MU---
Sentiment:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 100069.45
SMA:
Starting Portfolio Value: 100000.00
Final Portfolio Value: 99978.92
SENTIMENT WINS
Sentiment won: 13/20
Sentiment profit: 54267.2
SMA profit: 350.629999999961
```
