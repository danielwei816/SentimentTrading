#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 02:12:55 2020

@author: daniel
"""

import pandas as pd
import numpy as np
import time
import requests
import pyrebase
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas_datareader as pdr
import matplotlib.pyplot as plt

from firebase_auth import *

tickers = ["MSFT", "AAPL", "AMD", "BA", "AMZN", "DIS", "FB", "NVDA", "MGM", "PPL", "AAL", "ATVI", "NFLX", "INTC", "JPM", "GE", "BAC", "CSCO", "EBAY", "MU"]
num_days = date.today() - date(2020, 1, 1)


for i in range(len(tickers)):
    print(tickers[i])
    sent_list = [0] * 365
   
    for j in range(num_days.days+7, 7, -7):
        sum = 0
        stock_com = requests.get('https://api.pushshift.io/reddit/search/comment/?q={}&subreddit=wallstreetbets&after={}d&before={}d&size=500'.format(tickers[i], j, j-7))
        stock_com = stock_com.json()
        
        for k in range(len(stock_com['data'])):
            score = analyser.polarity_scores(stock_com['data'][k]['body'])
            # print(score['compound'])
            sum += score['compound']
            
        print(sum)
        print(len(stock_com['data']))
        avg = sum/len(stock_com['data'])
        print(avg)
        sent_list[num_days.days +7 -j] = avg
        time.sleep(1)
       
    db.update({tickers[i]: sent_list})
    
