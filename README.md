# Long-Short-Cryptocurrency-Portfolio-Optimization

As cryptocurrency becomes more adopted in finance, and after reading a report from Bridgewater Associates we became interested in cryptocurrency from a more quantitative finance view. Something that we looked at was building multiple long short strategies and then optimize via efficient frontier to weight the a portfolio of long short strategies.

A trouble that we come across is given the market neutral aspect of the long-short it really comes down to finding the risk premia that arises in these cryptocurrencies. As risk premia is already a challanging topic in the financial world we assume that it is much harder within cryptocurrencies especially given that price discovery can most likely varies more due to market conditions such as countaparty management and or liquidity.

The method within this project randomly picks different cryptocurrency pairs for longs and shorts. Although this is is our initial method we hope to include more time series drive or factor analysis (most likely momentum given the troubles with value) style decisions for finding cryptocurrencies to go long on and then to go short on.

The data that we use if pulled from Yahoo Finance and is daily close data and we start on the day in which all crytpocurrencies have an initial price. Then from there we build out the long-short strategies using 50-50 weights. Once we've built all weights we then use the efficient frontier to optimize over the strategies and find the valid weighting.

Something that we found while examining the efficient frontier is that the risk tends to greatly shadow over the reward. Although the expected value of the portfolio is relatively high (~40%) we standard deviation of the portfolio is much higher, thus decreasing the sharpe. Something that we also found with the efficient frontier is that the difference in risk between the minium variance and maximized sharpe portfolio is very small, or in other words we can maximize sharpe without taking on much more risk (in a marginal sense).

In the future we hope to include more factors such as determining adding factor analysis to determine ideal longs and shorts as well as rebelancing the portfolio. 
