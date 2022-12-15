# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 1


# import packages
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

# My stock choices are: SPY, NVDA, SBUX, PYPL, WMT | Data used: last 10 days
myTickers = ["SPY", "NVDA", "SBUX", "PYPL", "WMT"]
myData = yf.download(tickers=myTickers, start="2022-08-30", end="2022-09-14")

myPrices = []
# print my choices
print("Stock choices are: SPY | NVDA | SBUX | PYPL | WMT")


# provides the closing price
def stockData(ticker):  # myData
    priceData = []
    for price in myData["Adj Close"]:
        priceData.append(price)  # ticker or price, same result - does not give accurate plot
    return priceData


# create a chart and saves the chart as an image in a folder
def createChart(tickers):
    # check whether charts folder is created, if not make directory
    if not os.path.exists('charts/'):
        os.makedirs('charts/')
    # creates a numpy array
    for ticker in tickers:
        myData = stockData(ticker)  # getStockData
        myPrices = np.array(stockData(ticker))  # myData
        # create matplotlib graph (title, x and y labels)
        plt.plot(myPrices)
        plt.title(ticker)
        plt.xlabel("Day")
        plt.ylabel("Price $")
        plt.tight_layout()
        # save the graph
        plt.savefig('charts/' + ticker + '.png', facecolor='auto', edgecolor='auto', pad_inches=0.25)
        # show the graph
        plt.show()


createChart(myTickers)   # myTickers
print("The images have been created for each stock in the 'charts' folder.")


'''
# provides the closing price
def closingPrice(stock):
    for stock in myTickers:
        price = yf.Ticker(stock)
'''
'''
def closingPrice(stock):
    try:
        ticker = yf.Ticker(stock)
        date = yf.download(tickers=stock, start="2022-08-30", end="2022-09-14")
        return date["Close"][0]
    except Exception as e:
        print("Incorrect stock ticker", e)
'''
'''
myTickers = ["SPY", "NVDA", "SBUX", "PYPL", "WMT"]
myData = closingPrice()

plt.plot(myData)
plt.title(ticker)
plt.xlabel("Day")
plt.ylabel("Price $")
plt.tight_layout()
# save the graph
plt.savefig('charts/' + ticker + '.png', facecolor='auto', edgecolor='auto', pad_inches=0.25)
# show the graph
plt.show()
'''
'''
data = yf.download("SPY", start="2022-08-30", end="2022-09-14")
data = yf.download("NVDA", start="2022-08-30", end="2022-09-14")
data = yf.download("SBUX", start="2022-08-30", end="2022-09-14")
data = yf.download("PYPL", start="2022-08-30", end="2022-09-14")
data = yf.download("WMT", start="2022-08-30", end="2022-09-14")
spyPrices = []
nvdaPrices = []
sbuxPrices = []
pyplPrices = []
wmtPrices = []

for price in data['Adj Close']:
    spyPrices.append(price)

print(spyPrices)
spyarray = np.array(spyPrices)
plt.plot(msftarray)
plt.title('SPY')
plt.xlabel("Day")
plt.ylabel("Price $")
plt.savefig('charts/spy.png')
plt.show()
'''



# Old Graded Code
'''
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
'''
