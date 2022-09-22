# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 1


import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# My stock choices are: SPY, NVDA, SBUX, PYPL, WMT, EX: MSFT
# Run > Receive PNG image > Save image file in another folder

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")

msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)

print(msftPrices)

# Create a NumPy array
msftarray = np.array(msftPrices)

# Create matplotlib graph
plt.plot(msftarray)

# Save the graph
plt.savefig('charts/msft.png')

# Show the graph
plt.show()  # Traceback error
