# Raw Package
import numpy as np
import pandas as pd
import time
import datetime

#Data Source
import yfinance as yf

import Indicateur as ind 

var = 0

def decision(stock):
    #Interval required 5 minutes
    data = yf.download(tickers=stock, period='1d', interval='1m')
    global var
    #Print data
    #print(data['Close'].tail(30))
    #print (d)

    if(var == -1):
        if(ind.SMA(data,30)> ind.SMA(data,100)):
            return 1 #achat
            var = 1
        else:
            return 0 #rien
    elif (var == 1):
        if(ind.SMA(data,30)< ind.SMA(data,100)):
            return -1 #vente
            var = -1
        else:
            return 0 # rien
    else:
        if(ind.SMA(data,30)< ind.SMA(data,100)):
            var = -1
        elif(ind.SMA(data,30)>ind.SMA(data,100)):
            var = 1

def BotSMA(stock):
    
    temp = decision(stock)
    if (temp == 1):
        print ('buy')
        return 'buy'
    elif(temp == -1):
        print ('sell')
        return 'sell'
    else:
        print ('wait')
        return 'wait'

