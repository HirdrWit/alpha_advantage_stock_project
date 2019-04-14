from modules import alpha_vantage_api 
from modules import trend 
from modules import clean_json 
from modules import stock_ml
from modules import write_json
from modules import twitter_sentiment
from modules import get_tweets
import pandas as pd
import csv


def main():
    json_data = {}  
    json_data['Stocks'] = [] 

    #Train Twitter Model 
    twitter_train = pd.read_csv("training_data.csv")
    clf = twitter_sentiment.train_twitter_model(twitter_train)

    # #begin for loop
    with open("test.csv", 'r', encoding='utf8') as csvFile:
        
        reader = csv.reader(csvFile)
        for row in reader:
            stock_symb = row[0]
            stock_name = row[1].split(" ")[0]
            archive = alpha_vantage_api.requestArchieve(stock_symb)
            if(len(archive)>0):
                print(stock_symb)
                date_ = clean_json.getDate(archive)

                open_ = clean_json.getOpening(archive)
                low_ = clean_json.getLow(archive)
                high_ = clean_json.getHigh(archive)
                close_ = clean_json.getClosing(archive)

                data = stock_ml.joinData(date_,open_,low_,high_,close_)

                volatile_ = trend.getVolatile(close_) #last year
                average_ = trend.getAvgerage(close_)  #last year

                features = stock_ml.getFeatures(data)
                labels = stock_ml.getLabels(data)

                # # Random Forest
                rf_prediction = stock_ml.randomForest(features, labels)
                rf_month = rf_prediction[0]
                rf_month_predict = rf_prediction[1]
                rf_accuracy = rf_prediction[2]


                # Get Twitter Data
                tweets = get_tweets.loadTweets(stock_name)
                tweets = twitter_sentiment.cleanTweets(tweets)
                if(len(tweets) > 0):
                    twitter_predictions = twitter_sentiment.predict_twitter_model(tweets, clf, twitter_train)
                    positive = twitter_predictions[0]
                    negative = twitter_predictions[1]
                else:
                    positive = 0
                    negative = 0


                # Data for JSON
                write_json.write(json_data,stock_symb,stock_name,rf_month,rf_month_predict,rf_accuracy,open_,close_,high_,low_,volatile_,average_,positive,negative)

if __name__ == '__main__':
    main()