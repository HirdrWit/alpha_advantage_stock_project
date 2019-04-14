import json

import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np


def main():
    with open('data.json') as json_file:  
        data = json.load(json_file)
        for p in data['Stocks']:
            print(p['rf_prediction'])
            print("")

            fig = plt.figure()
            ax = plt.axes()

            x = np.linspace(0, 10, 31)
            ax.plot(x, p['rf_prediction'])

if __name__ == '__main__':
    main()