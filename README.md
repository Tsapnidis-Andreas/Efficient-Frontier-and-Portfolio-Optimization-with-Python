# Project Title
## Efficient Frontier and Portfolio Optimization <br>
# Contents
[Info](#Info)<br>
[The Code](#The-Code)<br>
[Example](#Example)<br>
[Disclaimer](#Disclaimer) <br>
# Info
## Programming Languages: 
Python <br>
## Libraries used:
[Pandas](https://pandas.pydata.org/#:~:text=pandas%20is%20a%20fast,%20powerful,%20flexible)<br>
[Numpy](https://numpy.org/)<br>
[Yfinance](https://pypi.org/project/yfinance/)<br>
[Datetime](https://docs.python.org/3/library/datetime.html)<br>
[Scipy](https://scipy.org/)<br>
[Matplotlib](https://matplotlib.org/)<br>
[Seabron](https://seaborn.pydata.org/)<br>
# The Code
Before executing the program, a list containing the stocks for which the efficient frontier will be determined must be initialized, along with the variable `path`,<br>
specifying the folder where the results will be exported.<br>
Additionally, the time interval to be examined must be defined, i.e., the start and end dates of the period.<br>

Once executed, the program performs the following steps:<br>

Data Retrieval: Fetches monthly daily price data from Yahoo Finance for the specified time interval.<br>
It then calculates the cumulative monthly log returns and stores them in a data frame. This process is repeated for each stock.<br>
Average Monthly Return: Calculates the average monthly return for each stock and annualizes it.<br>
Portfolio Simulation: Generates 20,000 random portfolios by assigning random weights to each stock. <br>
It calculates the return, standard deviation, and Sharpe ratio for each portfolio.<br>
The risk-free rate used is the average monthly return of U.S. Treasury bonds for the specified period, retrieved from Yahoo Finance.<br>
Return Interval Creation: Creates an interval from the lowest to the highest average monthly return and divides it into 299 equal intervals, corresponding to 300 values.<br>
Capital Allocation Optimization: For each of these 300 values, it calculates the capital allocation across the stocks that minimizes the portfolio's standard deviation.<br>
Sharpe Ratio Calculation: Computes the Sharpe ratio for each of these 300 portfolios.<br>
The risk-free rate used is the average monthly return of U.S. Treasury bonds for the specified period, retrieved from Yahoo Finance.<br>
Plotting Portfolios: Plots the 20,000 random portfolios and the 300 efficient portfolios on the same graph.<br>
The portfolios are color-coded based on their Sharpe ratio, with a color bar explaining the corresponding value ranges.<br>
Correlation Matrix: Plots the correlation matrix between the stocks.<br>
Cumulative Returns Plot: Plots the cumulative returns for each stock on the same graph.<br>
Exports: Exports all graphs as `.png` files and the efficient frontier portfolios as an ‘.xlsx’ file. <br>
# Example-Case Study for the Athens Stock Exchange<br>
Below are the results of running the program for the 20 largest companies in the Greek stock market, by market capitalization.<br>
Some of them were excluded due to insufficient data.<br>
The data covers monthly returns from January 2021 to December 2025 (60 observations).

## Results:

![Efficient Frontier](https://github.com/user-attachments/assets/1577c55d-d87c-40f6-8a85-909ed6531564)

![Correlation Heatmap](https://github.com/user-attachments/assets/6aa4236c-71d9-45de-8634-a956098baeeb)

![Cumulative Log Returns](https://github.com/user-attachments/assets/4da4cb29-e495-413d-81f2-a577eae4f059)

# Disclaimer
This project serves educational purposes only<br>
Under no circumstances should it be used as an investing tool
