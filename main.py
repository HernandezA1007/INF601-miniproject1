# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# My stock choices are: SPY, NVDA, SBUX, PYPL, WMT, Ex: MSFT
# Run > Receive PNG image > Save image file in another folder
# terminal is not syncing with virtual environment - not running

#myTickers = yf.Tickers('spy nvda sbux pypl wmt')

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")  # Ex
#myData = yf.download("SPY NVDA SBUX PYPL WMT", start="2022-08-30", end="2022-09-14",  auto_adjust = True,)

msftPrices = []  # Ex
#spyPrices = []
#nvdaPrices = []
#sbuxPrices = []
#pyplPrices = []
#wmtPrices = []
#myPrices = []  # all ticker data?


for price in data['Adj Close']:
    msftPrices.append(price)

# Open, Close, calender, and dividends
#myTickers.tickers.NVDA.calendar  # shows next event
#myData.dividends  # shows all dividends?


print(msftPrices)

# Create a NumPy array
msftarray = np.array(msftPrices)
print(msftarray)
# Create matplotlib graph
plt.plot(msftarray)

# Save the graph
plt.savefig('charts/msft.png')
#plt.savefig('Charts/myData.png', facecolor='auto', edgecolor='auto', pad_inches=0.25)

# Show the graph

plt.show()  # Traceback error
