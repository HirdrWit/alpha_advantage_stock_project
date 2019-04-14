import sklearn
import pandas as pd
from sklearn.datasets import load_files
from sklearn.utils import shuffle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import nltk

def train_twitter_model(data):
    # Import data
    
    twitter_train = shuffle(data)

    # CountVectorizer Words


    twitter_vec = CountVectorizer(
        min_df=2, 
        tokenizer=nltk.word_tokenize
    )  

    twitter_counts = twitter_vec.fit_transform(twitter_train.message)

    # Convert raw frequency counts into TF-IDF values

    tfidf_transformer = TfidfTransformer()

    twitter_tfidf = tfidf_transformer.fit_transform(twitter_counts)

    # Training and testing


    docs_train, docs_test, y_train, y_test = train_test_split(
        twitter_tfidf, twitter_train['rank'], test_size = 0.70, random_state = 1)


    clf = MultinomialNB().fit(docs_train, y_train)

    y_pred = clf.predict(docs_test)

    # print("Train accuracy is %.2f %%" % (clf.score(docs_train, y_train)*100))
    # print("Test accuracy is %.2f %%" % (clf.score(docs_test, y_test)*100))

    return(clf)

def predict_twitter_model(tweets, clf, data):
# import csv
    twitter_train = shuffle(data)
    twitter_vec = CountVectorizer(
        min_df=2, 
        tokenizer=nltk.word_tokenize
    ) 
    tfidf_transformer = TfidfTransformer()
    twitter_counts = twitter_vec.fit_transform(twitter_train.message)
    tfidf_transformer = TfidfTransformer()
    twitter_tfidf = tfidf_transformer.fit_transform(twitter_counts)


    reviews_new_counts = twitter_vec.transform(tweets)
    reviews_new_tfidf = tfidf_transformer.transform(reviews_new_counts)

    # have classifier make a prediction
    pred = clf.predict(reviews_new_tfidf)

    positive = 0
    negative = 0

    # print out results
    for review, category in zip(tweets, pred):
        # print('%r => %s' % (review, category))
        if(category == "negative" ):
            negative+=1

        if(category == "positive" ):
            positive+=1

    # print("postive: " + str(positive))
    # print("negative: " + str(negative))
    return([positive,negative])

def cleanTweets(tweets):
    new = []
    for tweet in tweets:
        if "\\x" in str(tweet):
            x = 1
        else:
            new.append(tweet)
            
    return(new)