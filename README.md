 - INF601 - Advanced Programming in Python
 - Antonio Hernandez
 - Mini Project 1


# INF601 Mini Project 1

### This mini project allows the user to receive images of stocks with their closing prices.
The stocks provided are the projects owner example stocks over a 10 day period as an example, you will be required 
to know the stock ticker to receive a graph of your stock and change the time period to your desired period. The
images are saved as a png in the 'charts' folder.

---
## Quick Start

> Before starting, look at requirements.txt to install the necessary packages

`pip install -r requirements.txt`
> You can change the given tickers to your desired stocks in line...<> 
`<line>`

> You can change the time period to your choice by year-month-day
`<line>`


An example to startup the project can be taken below:
```python
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

data = yf.download("MSFT", start="2022-08-30", end="2022-09-14")

msftPrices = []

for price in data['Adj Close']:
    msftPrices.append(price)
    
print(msftPrices)

msftarray = np.array(msftPrices)

plt.plot(msftarray)

plt.savefig('charts/msft.png')

plt.show()

```

## Example of result/output
image...