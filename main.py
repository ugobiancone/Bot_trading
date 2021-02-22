import Bot
import datetime
import time
import Bankroll
import yfinance as yf

bank = Bankroll.bankroll(1000)
Achat = 0
dt = datetime.datetime.now().time()
other_time = datetime.time.fromisoformat('21:00')
while (dt < other_time):
    test = Bot.BotSMA('AAPL')
    if(test == 'buy'):
        data = yf.download(tickers=stock, period='1d', interval='1m')
        d2 = data['Close'].tail(1).to_numpy()
        Achat = d2[0]
        bank.buy()
        print('buy')
        print(bank.get_bank())
    elif(test =='sell'):
        data = yf.download(tickers=stock, period='1d', interval='1m')
        d2 = data['Close'].tail(1).to_numpy()
        vente = (d2[0]/Achat)*100
        bank.sell(vente)
        print('sell')
        print(bank.get_bank())

    time.sleep(60)
    dt = datetime.datetime.now().time()

if(dt>=other_time):
    data = yf.download(tickers=stock, period='1d', interval='1m')
    d2 = data['Close'].tail(1).to_numpy()
    vente = (d2[0]/Achat)*100
    bank.sell(vente)
    print(bank.get_bank())

    

