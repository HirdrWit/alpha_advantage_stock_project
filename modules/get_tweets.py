import twitter
import json

def loadTweets(stock):
    stocks = stock.lower()
    api = twitter.Api(consumer_key='e5Es2lqqUdagHlof03gAJzF8u',
    consumer_secret='qbkclMGlhPcA31DS6OtUlPB00iKU87zHOyBTbANRgCcUSzYjAA',
    access_token_key='894498050-lmd7WnOe0fPZChENzwLuVmSKe27VQ1a5uXEWVLUB',
    access_token_secret='OMDPLwsiPrqfImWw8ofINMXQ7XEARi8hFoBZm3BSS22Jf')

    # search = api.GetSearch(stock, geocode=[37.781157, -122.398720, "1mi"] ,count=100) # Replace happy with your search
    search = api.GetSearch(stock, count=100) 
    tweets = []

    for tweet in search:
        tweet = str(tweet.text)
        tweets.append(tweet.encode("utf-8"))

    return(tweets)