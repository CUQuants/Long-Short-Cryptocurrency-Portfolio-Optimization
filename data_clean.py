import random
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crypto_prices.csv", index_col = 0)
df = df.dropna(axis = 1, how = "all")
df = df.dropna()

tickers = df.columns.to_list()
random.shuffle(tickers)

j = 0
k = 1
m = 0
n = 0

fig, axes = plt.subplots(4,3, figsize = (30,20))

cumsum_df = pd.DataFrame()
daily_pct_df = pd.DataFrame()

for i in range(int(len(tickers) / 2)):
    
    #grabbing the specific crypto currencies and getting percent change
    port_data = df[[df.columns[j], df.columns[k]]].pct_change().dropna()
    
    #creating the short position
    port_data[df.columns[k]] = -port_data[df.columns[k]]
    
    #renaming columsn to have long and short
    port_data = port_data.rename(columns = {port_data.columns[0]: port_data.columns[0] + "_long", port_data.columns[1]: port_data.columns[1] + "_short"})
    
    #generating 50-50 portfolio of long and short
    port_data["returns"] = (0.5 * port_data[port_data.columns[0]]) + (0.5 * port_data[port_data.columns[1]])
    
    #getitng cumulative returns
    for l in port_data.columns:
        port_data[l + "_cumsum"] = port_data[l].cumsum()
    
    #plotting
    port_data[port_data.columns[3:]].plot(ax = axes[m,n], grid = True)
    
    #iterate the x axis of the matplotlib
    n += 1
    
    #if we reach the end of the x axis then reset
    if n == 3:
        
        #reset
        n = 0
        
        #then go to the next row
        m += 1

    #loop to get the next two sets of cryptocurrency
    j +=2 
    k +=2
    
    cumsum_df[port_data.columns[0] + "_" + port_data.columns[1] + "_cumsum"] = port_data["returns_cumsum"]
    daily_pct_df[port_data.columns[0] + "_" + port_data.columns[1]] = port_data["returns"]

plt.tight_layout()

fig.savefig("cumsum_plots.png")
cumsum_df.to_csv("cumsum.csv")
daily_pct_df.to_csv("returns.csv")