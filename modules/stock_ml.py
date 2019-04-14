import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

def randomForest(features,labels):

    labels = np.array(labels)
    features = np.array(features)

    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    rf.fit(train_features, train_labels)

    predictions = rf.predict(test_features)
    
    month_features = getNextMonth(features[0])

    errors = abs(predictions - test_labels)
    # print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / test_labels)
    accuracy = 100 - np.mean(mape)

    month_prediction = rf.predict(month_features)
    return([month_features,month_prediction,round(accuracy, 2)])

def linearRegression(features,labels):

    labels = np.array(labels)
    features = np.array(features)
    labels = labels.astype(float)
    features = features.astype(float)

    features = preprocessing.scale(features)

    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.20)
    
    lr = LinearRegression()
    lr.fit(train_features, train_labels)

    predictions = lr.predict(test_features)
    
    month_features = getNextMonth(features[0])

    errors = abs(predictions - test_labels)
    # print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / test_labels)
    accuracy = 100 - np.mean(mape)

    month_prediction = lr.predict(month_features)
    return([month_features,month_prediction,round(accuracy, 2)])




#helper, would be better if it was its own module. 
def joinData(date,open_,low,high,close):
    year = []
    month = []
    day = []

    for i in date:
        d = i.split("-")
        year.append(d[0])
        month.append(d[1])
        day.append(d[2])

    data = []

    for i in range(0,len(year)):
        data.append([year[i],month[i],day[i],close[i],open_[i],high[i],low[i]])
    return(data)
        
def getFeatures(data):
    new = []
    for i in data:
        new.append([i[0],i[1],i[2]])
    return(new)

def getLinearFeatures(data):
    new = []
    for i in data:
        new.append([i[0],i[1],i[2],i[4],i[5],i[6]])
    return(new)

def getLabels(data):
    new = []
    for i in data:
        new.append(i[3])
    return(new)

def getNextMonth(date): #Fix actual dates
    new_month = []
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    for i in range(0,30):
        if(day<=30):
            day = day + 1
            new_month.append([year, month, day])
        if(day>30):
            day = 1
            if(month == 12):
                month = 1
                year = year + 1
            else:
                month = month + 1
            new_month.append([year, month, day])
    return(new_month)
        


