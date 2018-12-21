import json


def findTrend(data,days):
    avg_open = findAvg('1. open',data)
    print("-----")
    avg_high = findAvg('2. high',data)
    print("-----")
    avg_low = findAvg('3. low',data)
    print("-----")
    avg_close = findAvg('4. close',data)
    print("-----")
    open_to_close('under',data,avg_open,avg_close,days)


def findAvg(value,data):
    timeSeries = getTimeSeries(data)
    total = 0
    count = 0
    for date in data[timeSeries]:
        if(count<365):
            total += float(data[timeSeries][date][value])
            count += 1
    print("Avg " + str(value) +  " : " + str(total/count))
    return total/count

def getTimeSeries(data):
    for key in data.keys():
        timeSeries = key
    return timeSeries

def open_to_close(job,data,avg_open,avg_close,days):
    timeSeries = getTimeSeries(data)
    points = 0
    count = 0
    if(job=='under'):
        for date in data[timeSeries]:
            if(count<days and float(data[timeSeries][date]['1. open']) < avg_open):
                print("open: " +  data[timeSeries][date]['1. open'])
                print("close: " +  data[timeSeries][date]['4. close'])
                val = float(data[timeSeries][date]['4. close']) - float(data[timeSeries][date]['1. open']) 
                if(val<0):
                    points-=1
                if(val>0):
                    points+=1

            count +=1
    print(points)        
    #elif(job=='over'):