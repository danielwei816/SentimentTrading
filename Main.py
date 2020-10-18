import time
import requests
import pyrebase
from datetime import date
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

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

analyser = SentimentIntensityAnalyzer()

tickers = ["MSFT", "AAPL", "AMD", "BA", "AMZN", "DIS", "FB", "NVDA", "MGM", "PPL", "AAL", "ATVI", "NFLX", "INTC", "JPM", "GE", "BAC", "CSCO", "EBAY", "MU"]
num_days = date.today() - date(2020, 1, 1)

for i in range(11, len(tickers), 1):
    print(tickers[i])
    sent_list = [0] * 365
   
    for j in range(num_days.days+7, 7, -1):
        sum = 0
        stock_com = requests.get('https://api.pushshift.io/reddit/search/comment/?q={}&subreddit=wallstreetbets&after={}d&before={}d&size=500'.format(tickers[i], j, j-7))
        stock_com = stock_com.json()
        
        for k in range(len(stock_com['data'])):
            score = analyser.polarity_scores(stock_com['data'][k]['body'])
            # print(score['compound'])
            sum += score['compound']
            
        print(sum)
        print(len(stock_com['data']))
        if(sum != 0):
            avg = sum/len(stock_com['data'])
        else:
            avg = 0
        print(avg)
        sent_list[num_days.days +7 -j] = avg
        time.sleep(1.5)
       
    db.update({tickers[i]: sent_list})
    
    
    

    