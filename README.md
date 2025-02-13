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

Data Retrieval: Fetches monthly stock price data from Yahoo Finance for the specified time interval.<br>
It then calculates the monthly returns and stores them in a data frame. This process is repeated for each stock.<br>
Average Monthly Return: Calculates the average monthly return for each stock.<br>
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
Stock Returns Plot: Plots the returns for each stock on the same graph.<br>
Data Export: Exports the stock returns and efficient portfolios as an `.xlsx` file.<br>
Graph Export: Exports all graphs as `.png` files. <br>
# Example-Case Study for the Athes Stock Exchange<br>
Below are the results of running the program for the 25 largest companies in the Greek stock market, by market capitalization.<br>
These companies are the following:<br>

1. Eurobank Ergasias Services and Holdings – EUROB.AT<br>
2. National Bank of Greece – ETE.AT<br>  
3. Hellenic Telecommunications – HTO.AT<br>  
4. OPAP (Organization of Football Prognostics) – OPAP.AT<br> 
5. Mytilineos – MYTIL.AT<br>  
6. Piraeus Financial Holdings – TPEIR.AT<br>  
7. Public Power – PPC.AT<br>  
8. Jumbo – BELA.AT<br>  
9. Alpha Services and Holdings – ALPHA.AT<br>  
10. Titan Cement International – TITC.AT<br>  
11. Athens International Airport – AIA.AT<br>  
12. TERNA ENERGY Industrial Commercial Technical Societe Anonyme – TENERGY.AT<br>  
13. Motor Oil (Hellas) Corinth Refineries – MOHAT.AT<br>  
14. HELLENiQ ENERGY Holdings – ELPE.AT<br>  
15. Gek Terna – GEKTERNA.AT<br>  
16. Prodea Real Estate Investment Company – PRODEA.AT<br>  
17. LAMDA Development – LAMDA.AT<br>  
18. Optima Bank – OPTIMA.AT<br>  
19. Karelia Tobacco – KARE.AT<br>  
20. Aegean Airlines – AEGN.AT<br>  
21. Lampsa Hellenic Hotels – LAMPS.AT<br>  
22. Intrakat – INKAT.AT<br>  
23. Piraeus Port Authority – PPA.AT<br>  
24. Gr. Sarantis – SAR.AT<br>  
25. Elvalhalcor Hellenic Copper and Aluminium Industry – ELHA.AT<br>  

However, due to insufficient data for the following companies:<br>
Titan Cement International<br>
Athens International Airport<br>
Optima Bank<br>
Motor Oil (Hellas) Corinth Refineries<br>
these stocks were excluded. The data covers monthly returns from October 2019 to September 2024 (60 observations).

## Results:

![Efficient Frontier](https://github.com/user-attachments/assets/6a500769-3df6-4784-89f2-00fc50ceb553)

![Correlation Heatmap](https://github.com/user-attachments/assets/35e18df4-290e-41d6-95a5-41fd8db6a658)

![Stock Returns](https://github.com/user-attachments/assets/c6da47a8-e18b-4909-9ce4-baf32b1e7e61)

![Στιγμιότυπο οθόνης 2025-02-12 175350](https://github.com/user-attachments/assets/78c04ddd-0011-4e73-956a-cdb964bdf1f1)


# Disclaimer
This project serves educational purposes only<br>
Under no circumstances should it be used as an investing tool
