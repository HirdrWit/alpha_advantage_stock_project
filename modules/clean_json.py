import json

def getDate(json_data):
    date = []
    for i in json_data["Time Series (Daily)"]:
        date.append(i)
    return date

def getOpening(json_data):
    opening = []
    for i in json_data["Time Series (Daily)"]:
        opening.append(float(json_data["Time Series (Daily)"][i]["1. open"]))
    return opening

def getClosing(json_data):
    closing = []
    for i in json_data["Time Series (Daily)"]:
        closing.append(float(json_data["Time Series (Daily)"][i]["4. close"]))
    return closing

def getHigh(json_data):
    high = []
    for i in json_data["Time Series (Daily)"]:
        high.append(float(json_data["Time Series (Daily)"][i]["2. high"]))
    return high

def getLow(json_data):
    low = []
    for i in json_data["Time Series (Daily)"]:
        low.append(float(json_data["Time Series (Daily)"][i]["3. low"]))
    return low