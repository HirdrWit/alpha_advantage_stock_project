import statistics

def getAvgerage(data):
    temp = []
    for i in range(0,364):
        temp.append(data[i])

    return(round(statistics.mean(temp), 2))

def getVolatile(data):
    temp = []
    for i in range(0,364):
        temp.append(data[i])

    return(round(statistics.stdev(temp), 2))