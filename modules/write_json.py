import json

def write(data,stock_symb,stock_name,month,rf_predict,accuracy,open_,close_,high_,low_,volatile_,average_,positive,negative): 
    data['Stocks'].append({  
        'stock_symb': stock_symb,
        'stock_name': stock_name,
        'date_label': month,
        'rf_prediction': rf_predict.tolist(),
        'accuracy': accuracy,
        'open': open_[0],
        'close': close_[0],
        'high': high_[0],
        'low': low_[0],
        'volatility': volatile_,
        'average': average_,
        'positive': positive,
        'negative': negative
    })

    with open('data7.json', 'w+') as outfile:  
        json.dump(data, outfile)