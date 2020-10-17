import pandas as pdimport numpy as npimport pandas_datareader as pdrimport matplotlib.pyplot as pltimport jsonimport tweepyfrom tweepy.streaming import StreamListenerfrom tweepy import OAuthHandlerfrom tweepy import Stream# import twitter keys and tokensfrom config import *data_amd = pdr.get_data_yahoo('AMD', '1-Feb-20')data_amd.head()data_amd['2_SMA'] = data_amd['Close'].rolling(window=2).mean()data_amd['5_SMA'] = data_amd['Close'].rolling(window=5).mean()data_amd = data_amd[data_amd['5_SMA'].notna()]# SMA trade callsTrade_Buy=[]Trade_Sell=[]for i in range(len(data_amd)-1):    if ((data_amd['2_SMA'].values[i] < data_amd['5_SMA'].values[i]) & (data_amd['2_SMA'].values[i+1] > data_amd['5_SMA'].values[i+1])):        print("Trade Call for {row} is Buy.".format(row=data_amd.index[i].date()))        Trade_Buy.append(i)    elif ((data_amd['2_SMA'].values[i] > data_amd['5_SMA'].values[i]) & (data_amd['2_SMA'].values[i+1] < data_amd['5_SMA'].values[i+1])):        print("Trade Call for {row} is Sell.".format(row=data_amd.index[i].date()))        Trade_Sell.append(i)plt.figure(figsize=(20, 10),dpi=80)plt.plot(data_amd.index, data_amd['Close'])plt.plot(data_amd.index, data_amd['2_SMA'],'-^', markevery=Trade_Buy, ms=15, color='green')plt.plot(data_amd.index, data_amd['5_SMA'],'-v', markevery=Trade_Sell, ms=15, color='red')plt.xlabel('Date',fontsize=14)plt.ylabel('Price in Dollars', fontsize = 14)plt.xticks(rotation='60',fontsize=12)plt.yticks(fontsize=12)plt.title('Trade Calls - Moving Averages Crossover', fontsize = 16)plt.legend(['Close','2_SMA','5_SMA'])plt.grid()plt.show() class TweetStreamListener(StreamListener):    numAnalyzed = 0    numPositive = 0    numNeutral = 0    numNegative = 0    # on success    def on_data(self, data):        # decode json        print(data)        #df = pd.DataFrame(data[0])        return True    # on failure    def on_error(self, status):        print(status)# create instance of the tweepy tweet stream listenerlistener = TweetStreamListener()# set twitter keys/tokensauth = OAuthHandler(consumer_key, consumer_secret)auth.set_access_token(access_token, access_token_secret)# instantiate apiapi = tweepy.API(auth)# create instance of the tweepy streamstream = Stream(auth, listener)# search twitter by useruser = api.get_user('realDonaldTrump')stream.filter(follow=[str(user.id)])