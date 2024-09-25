'''Monte Carlo Simulation of a Stock Portfolio with Python'''
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf

def get_data(stocks, start, end):
    '''Gathers stock info for closing prices and returns the mean & covariance matrix'''
    all_data = pd.DataFrame()

    for stock in stocks:
        try:
            stock_data = yf.download(stock, start=start, end=end)
            if not stock_data.empty:  # Check if data is returned
                all_data[stock] = stock_data['Close']
            else:
                print(f"Warning: No data returned for {stock}")
        except Exception as output:
            print(f"Error fetching data for {stock}: {output}")

    returns = all_data.pct_change().dropna()
    meanReturns = returns.mean()
    covMatrix = returns.cov()

    return meanReturns, covMatrix

stockList = ['DFEN', 'EURL']

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=500)

meanReturns, covMatrix = get_data(stockList, startDate, endDate)

weights = [0.2, 0.7] # Manual weights
# weights = np.random.random(len(meanReturns)) # Random weights
weights /= np.sum(weights)
# print(weights)

# Monte Carlo Method
# Number of simulations
MC_SIMS = 300
T = 100 #timefram in days

meanM = np.full(shape=(T, len(weights)), fill_value=meanReturns)
meanM = meanM.T
portfolio_sims = np.full(shape=(T, MC_SIMS), fill_value=0.0)

initalPortfolio = 10000

for m in range(0, MC_SIMS):
    #MC loops
    Z = np.random.normal(size = (T, len(weights)))
    L = np.linalg.cholesky(covMatrix)
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:,m] = np.cumprod(np.inner(weights,dailyReturns.T)+ 1)*initalPortfolio

plt.plot(portfolio_sims)
plt.ylabel('Portfolio value ($)')
plt.xlabel('Days')
plt.title('MC simulation of a stock portfolio')
plt.show()
