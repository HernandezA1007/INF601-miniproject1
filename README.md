 INF601 - Advanced Programming in Python
 Antonio Hernandez
 Mini Project 1
 
- [ ] Intro/Welcome to project - explain
- [ ] Quick start/steps - install and requirements
- [ ] Build = execute

# INF601 Mini Project 1

### This project allows the user to receive images of stocks.
The stocks provided are the projects owner example stocks, you will be required to know the stock ticker to receive
a graph of your stock. 

---
## Quick Start

> Before starting, look at requirements.txt to install the necessary packages

`pip install -r requirements.txt`

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