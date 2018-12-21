from modules import alpha_vantage_api 
from modules import trend 
def main():
    achieve = alpha_vantage_api.requestArchieve("MSFT")
    trend.findTrend(achieve,30)


    today = alpha_vantage_api.requestToday("GOOG")
    
    # for date in data["Time Series (5min)"]:
    #     print(date)
    #     print(data["Time Series (5min)"][date]["1. open"])


if __name__ == '__main__':
    main()