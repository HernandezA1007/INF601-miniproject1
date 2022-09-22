# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 1


import yfinance as yf
# SPY, NVDA, SBUX, PYPL, WMT

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")
# print(data)
msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)