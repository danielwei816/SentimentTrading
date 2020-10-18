import pandas as pd
import numpy as np
import time
import requests
import pyrebase
from datetime import date
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


import pandas_datareader as pdr
import matplotlib.pyplot as plt

# firebase configuration keys
firebase_config = {
  "apiKey": "AIzaSyCmmznsEI68l0AVICMuB5Gm3rRDifJt-xE",
  "authDomain": "sentimenttrading-f5ae7.firebaseapp.com",
  "databaseURL": "https://sentimenttrading-f5ae7.firebaseio.com/",
  "storageBucket": "sentimenttrading-f5ae7.appspot.com",
  "serviceAccount": "firebase_keys.json"
}

# initialize firebase
firebase = pyrebase.initialize_app(firebase_config)

# Get a reference to the auth service
auth = firebase.auth()

# Get a reference to the database service
db = firebase.database()

data_amd = pdr.get_data_yahoo('AMD', '1-Jan-20')
data_amd.head()

data_amd['2_SMA'] = data_amd['Close'].rolling(window=2).mean()
data_amd['5_SMA'] = data_amd['Close'].rolling(window=5).mean()

data_amd = data_amd[data_amd['5_SMA'].notna()]

# SMA trade calls
Trade_Buy=[]
Trade_Sell=[]
for i in range(len(data_amd)-1):
    if ((data_amd['2_SMA'].values[i] < data_amd['5_SMA'].values[i]) & (data_amd['2_SMA'].values[i+1] > data_amd['5_SMA'].values[i+1])):
        print("Trade Call for {row} is Buy.".format(row=data_amd.index[i].date()))
        Trade_Buy.append(i)
    elif ((data_amd['2_SMA'].values[i] > data_amd['5_SMA'].values[i]) & (data_amd['2_SMA'].values[i+1] < data_amd['5_SMA'].values[i+1])):
        print("Trade Call for {row} is Sell.".format(row=data_amd.index[i].date()))
        Trade_Sell.append(i)

plt.figure(figsize=(20, 10),dpi=80)
plt.plot(data_amd.index, data_amd['Close'])
plt.plot(data_amd.index, data_amd['2_SMA'],'-^', markevery=Trade_Buy, ms=15, color='green')
plt.plot(data_amd.index, data_amd['5_SMA'],'-v', markevery=Trade_Sell, ms=15, color='red')
plt.xlabel('Date',fontsize=14)
plt.ylabel('Price in Dollars', fontsize = 14)
plt.xticks(rotation='60',fontsize=12)
plt.yticks(fontsize=12)
plt.title('Trade Calls - Moving Averages Crossover', fontsize = 16)
plt.legend(['Close','2_SMA','5_SMA'])
plt.grid()
plt.show() 

analyser = SentimentIntensityAnalyzer()


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
    
    
    

    