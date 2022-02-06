import pandas as pd
import yfinance as yf

tickers = pd.read_excel("crypto_tickers.xlsx")
tickers = tickers[tickers.columns[0]].to_list()

df = yf.download(tickers)['Close']
df.to_csv("crypto_prices.csv")