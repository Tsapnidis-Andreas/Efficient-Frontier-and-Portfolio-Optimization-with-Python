import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from scipy.optimize import minimize
from matplotlib import pyplot as plt
import seaborn as sb
import plotly.graph_objects as go
def get_risk_free_rate():
    end_date = datetime.datetime(2024,9,30)
    start_date = datetime.datetime(2019, 9, 30)
    data = yf.download('^IRX', start=start_date, end=end_date)
    average=np.mean(data)
    risk_free_rate = ((1 + average / 100) ** (1 / 12) - 1) * 100
    return(round(risk_free_rate,2))

def get_returns(stock):
    end_date = datetime.datetime(2024, 9, 30)
    start_date = datetime.datetime(2019, 9, 30)
    data = yf.download(stock, start=start_date, end=end_date)
    data = pd.DataFrame(data)
    data = data['Adj Close']
    monthly_data = data.resample('ME').last()
    monthly_data.columns = ['Adj Close']
    monthly_data['returns'] = (monthly_data['Adj Close'] - monthly_data['Adj Close'].shift(1)) / monthly_data[
        'Adj Close'].shift(1)
    monthly_data['returns'] = round(monthly_data['returns'], 4)
    monthly_data = monthly_data.dropna()
    monthly_data.index = range(0, len(monthly_data))
    return (pd.Series(monthly_data['returns']),monthly_data['returns'].mean())

def get_portfolio_return(weights):
    pret=np.dot(weights,avg_ret.T)
    return(pret)

def get_portfolio_risk(weights):
    weights=np.array(weights)
    weights=np.array(weights)
    v=np.sqrt(np.dot(weights,np.dot(cov_matrix,weights.T)))
    return(v)

def get_random_portfolios():
    portfolio_returns = []
    portfolio_volatilities = []

    for i in range(0, 20000):
        weights = np.random.dirichlet(np.ones(len(avg_ret.tolist())))
        portfolio_returns.append(get_portfolio_return(weights))
        portfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))))

    portfolio_returns = np.array(portfolio_returns)*100
    portfolio_volatilities = np.array(portfolio_volatilities)*100

    portfolios = pd.DataFrame({'Return %': portfolio_returns, 'Standard Deviation': portfolio_volatilities})
    portfolios['Sharpe Ratio']=round((portfolios['Return %']-float(risk_free_rate))/portfolios['Standard Deviation'],2)
    print(portfolios)
    return(portfolios)

def get_max(df):
    max_sharpe=df['Sharpe Ratio'].max()
    y=df['Sharpe Ratio'].idxmax()
    x = df.loc[y, 'Standard Deviation']
    y=df.loc[y,'Return %']
    return(y,x,max_sharpe)

def plotting(random_portfolios,optimal_portfolios,stock_data,path,ret_max,std_max):
    figure = plt.figure(figsize=(18, 10))
    plt.style.use('ggplot')
    plt.xlabel('Mοnthly Standard Deviation')
    plt.ylabel('Expected Mοnthly Return %')
    plt.scatter(random_portfolios['Standard Deviation'], random_portfolios['Return %'],c=random_portfolios['Sharpe Ratio'],cmap='gnuplot')
    plt.scatter(optimal_portfolios['Standard Deviation'], optimal_portfolios['Return %'],c=optimal_portfolios['Sharpe Ratio'],cmap='gnuplot')
    cbar = plt.colorbar()
    cbar.ax.set_title('Sharpe Ratio')
    plt.scatter(std_max,ret_max,marker='*',s=350,c='indigo',label='Optimal Portfolio (Highest Sharpe Ratio)')
    plt.title('Efficient Frontier')
    plt.savefig(path + 'Efficient Frontier.png')

    figure1 = plt.figure(figsize=(18, 10))
    dataplot = sb.heatmap(stock_data.corr(numeric_only=True), cmap='Reds', annot=True)
    plt.title('Correlation Heatmap')
    plt.savefig(path + 'Correlation Heatmap.png')

    figure2 = plt.figure(figsize=(18, 10))
    sb.set_theme(style='whitegrid')
    sb.lineplot(data=stock_data, palette='tab10', linewidth=2.5)
    plt.title('Returns')
    plt.savefig(path + 'Stock Returns.png')

def saving(df,name,path):
    writer = pd.ExcelWriter(path + name +'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
    writer.close()

#!!!!!!!!!!!!!!!!!! INITIALIZE VALUES
stocks=['EUROB.AT','ETE.AT','HTO.AT','OPAP.AT','MYTIL.AT','TPEIR.AT','PPC.AT'
        ,'BELA.AT','ALPHA.AT','TENERGY.AT'
    ,'ELPE.AT','GEKTERNA.AT','PRODEA.AT','LAMDA.AT','KARE.AT','AEGN.AT',
        'LAMPS.AT','INKAT.AT','PPA.AT','SAR.AT','ELHA.AT']

path="C:/Users/tsapn/OneDrive/Υπολογιστής/Spare/"
#!!!!!!!!!!!!!!!!!!

global cov_matrix
global avg_ret
risk_free_rate=get_risk_free_rate()
avg_ret=[]
stock_data=pd.DataFrame()
for i in stocks:
    stock_data[i],ret=get_returns(i)
    avg_ret.append(ret)

stock_data=stock_data.dropna()
print(stock_data)
avg_ret=np.array(avg_ret)
cov_matrix=stock_data.cov()
random_portfolios=get_random_portfolios()
optimal_portfolios=pd.DataFrame()
returns=np.linspace(min(avg_ret),max(avg_ret),300)
optimal_portfolios['Return %']=(returns)
optimal_portfolios['Standard Deviation']=np.ones((len(optimal_portfolios),1))
volatility_opt=[]
bounds = [(0, 1) for i in range(len(stocks))]
initial_weights = np.array([1 / len(stocks)] * len(stocks))
constraints=({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1},
             {'type':'eq','fun':lambda weights:get_portfolio_return(weights)-r})
weights_df=pd.DataFrame()
k=0
for r in returns:
    opt=minimize(get_portfolio_risk,initial_weights,method='SLSQP',bounds=bounds,constraints=constraints)
    volatility_opt.append(opt['fun'])
    optimal_weights =opt.x
    optimal_weights=optimal_weights.tolist()

    for i in range(1,len(stocks)+1):
        a=round(optimal_weights[i-1]*100,2)
        a='{:f}'.format(a)
        weights_df.loc[k,i]=a
    k=k+1
optimal_portfolios['Standard Deviation']=volatility_opt
optimal_portfolios = optimal_portfolios*100
optimal_portfolios['Sharpe Ratio']=(optimal_portfolios['Return %']-float(risk_free_rate))/optimal_portfolios['Standard Deviation']
optimal_portfolios=optimal_portfolios.round(2)
ret_max,std_max,sharpe_max=get_max(optimal_portfolios)
results=pd.DataFrame(np.hstack((np.array(optimal_portfolios),np.array(weights_df))))
col_names=['Return %','Standard Deviation','Sharpe Ratio']+stocks
results.columns=col_names
plotting(random_portfolios,optimal_portfolios,stock_data,path,ret_max,std_max)
saving(stock_data,'Stock Returns',path)
saving(results,'Efficient Frontier Portfolios',path)