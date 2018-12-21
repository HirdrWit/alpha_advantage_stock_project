import requests
import json
import settings
settings.init() 

def requestArchieve(stock):
    r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&interval=5min&outputsize=full&symbol={stock}&apikey={settings.apikey}')
    return r.json()

def requestToday(stock):
    r = requests.get(f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock}&interval=5min&apikey={settings.apikey}')
    return r.json()        
    