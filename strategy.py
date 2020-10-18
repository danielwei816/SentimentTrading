#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:56:50 2020

@author: daniel
"""

from firebase_auth import db
from datetime import datetime
import backtrader as bt

class SentimentStrategy(bt.Strategy):
    
    def __init__(self):
        self.counter = 0

    def next(self):
        if sentimentData[self.counter] > 0.1: # buy if sentiment is > 0.1
            self.buy()
        elif sentimentData[self.counter] < -0.1: # close position if sentiment is < -0.1
            self.close();
        self.counter += 1


class SmaCrossBenchmark(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=2,  # period for the fast moving average
        pslow=5   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


tickers = ["MSFT", "AAPL", "AMD", "BA", "AMZN", "DIS", "FB", "NVDA", "MGM", "PPL", "AAL", "ATVI", "NFLX", "INTC", "JPM", "GE", "BAC", "CSCO", "EBAY", "MU"]

sentimentWins = 0
sentimentProfit = 0
smaProfit = 0
for ticker in tickers:
    cerebroStrategy = bt.Cerebro()  # create a "Cerebro" engine instance
    cerebroBenchmark = bt.Cerebro()
    
    # Pull stock data from Yahoo Finance
    data = bt.feeds.YahooFinanceData(dataname=ticker,
                                      fromdate=datetime(2020, 1, 1),
                                      todate=datetime(2020, 10, 17))
    
    # Add the data feed to each strategy
    cerebroStrategy.adddata(data)  
    cerebroBenchmark.adddata(data)
    
    # Set our desired cash start
    cerebroStrategy.broker.setcash(100000.0)
    cerebroBenchmark.broker.setcash(100000.0)
    
    print("---"  + ticker + "---")
    print("Sentiment:")
    # Print out the starting conditions for Strategy
    print('Starting Portfolio Value: %.2f' % cerebroStrategy.broker.getvalue())
    
    cerebroStrategy.addstrategy(SentimentStrategy)  # Add the trading strategy
    sentimentData = db.child(ticker).get().val()
    cerebroStrategy.run()  # run it all
    
    # Print out the final result for Strategy
    print('Final Portfolio Value: %.2f' % cerebroStrategy.broker.getvalue())
    
    print("SMA:")
    # Print out the starting conditions for Benchmark
    print('Starting Portfolio Value: %.2f' % cerebroBenchmark.broker.getvalue())
    
    cerebroBenchmark.addstrategy(SmaCrossBenchmark)  # Add the trading strategy
    cerebroBenchmark.run()  # run it all
    
    # Print out the final result for Benchmark
    print('Final Portfolio Value: %.2f' % cerebroBenchmark.broker.getvalue())
    
    # Evaluate results
    sentimentProfit += cerebroStrategy.broker.getvalue() - 100000
    smaProfit += cerebroBenchmark.broker.getvalue() - 100000
    if cerebroStrategy.broker.getvalue() > cerebroBenchmark.broker.getvalue():
        sentimentWins += 1
    print("SENTIMENT WINS" if cerebroStrategy.broker.getvalue() > cerebroBenchmark.broker.getvalue() else "SMA WINS")
    
print("Sentiment won: " + str(sentimentWins) + "/20")
print("Sentiment profit: " + str(sentimentProfit))
print("SMA profit: " + str(smaProfit))
