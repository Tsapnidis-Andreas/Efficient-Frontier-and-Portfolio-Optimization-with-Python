import pandas as pd
import numpy as np
import yfinance as yf
import datetime
from scipy.optimize import minimize
from matplotlib import pyplot as plt
import seaborn as sb
import plotly.graph_objects as go

def get_risk_free_rate():
    end_date = datetime.datetime(2025,12,31)
    start_date = datetime.datetime(2021, 1, 31)
    data = yf.download('^IRX', start=start_date, end=end_date)
    average=np.mean(data)
    print(data)
    risk_free_rate = -np.log(1-(average/100)/12)
    return(round(risk_free_rate,2))

def get_data(stock):
    end_date = datetime.datetime(2024, 9, 30)
    start_date = datetime.datetime(2019, 9, 30)
    data = yf.download(stock, start=start_date, end=end_date,auto_adjust=False)
    data = pd.DataFrame(data)
    print(data)
    return data['Adj Close'].squeeze()
def get_portfolio_return(weights):
    pret=np.dot(weights,m.T)
    return(pret)

def get_portfolio_risk(weights):
    weights=np.array(weights)
    v=np.sqrt(np.dot(weights,np.dot(s,weights.T)))
    return(v)

def get_random_portfolios():
    portfolio_returns = []
    portfolio_volatilities = []

    for i in range(0, 20000):
        weights = np.random.dirichlet(np.ones(len(m.tolist())))
        portfolio_returns.append(get_portfolio_return(weights))
        portfolio_volatilities.append(np.sqrt(np.dot(weights.T, np.dot(s, weights))))

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

def plotting(random_portfolios,optimal_portfolios,rets,path,ret_max,std_max):
    figure = plt.figure(figsize=(18, 10))
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.xlabel('Standard Deviation', fontsize=14)
    plt.ylabel('Expected Return %', fontsize=14)
    sc1 = plt.scatter(
        random_portfolios['Standard Deviation'],
        random_portfolios['Return %'],
        c=random_portfolios['Sharpe Ratio'],
        cmap='viridis',  # excellent on white
        alpha=0.7)
    plt.scatter(
        optimal_portfolios['Standard Deviation'],
        optimal_portfolios['Return %'],
        c=optimal_portfolios['Sharpe Ratio'],
        cmap='viridis')
    cbar = plt.colorbar(sc1)
    cbar.ax.set_title('Sharpe Ratio')
    plt.scatter(
        std_max,
        ret_max,
        marker='*',
        s=400,
        c='red',
        edgecolors='black',
        label='Optimal Portfolio (Highest Sharpe Ratio)')
    plt.title('Efficient Frontier', fontsize=18)
    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig(path + 'Efficient Frontier.png', dpi=300, facecolor='white')

    figure1 = plt.figure(figsize=(18, 10))
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    ax1 = sb.heatmap(rets.corr(numeric_only=True), cmap='Reds', annot=True,
                     annot_kws={"size": 12})

    figure2 = plt.figure(figsize=(18, 10))
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    ax2 = sb.lineplot(data=rets.cumsum(), palette='tab10', linewidth=2.5)
    plt.title('Cumulative Returns', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Cumulative Returns', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(path + 'Cumulative Returns.png', dpi=300, facecolor='white')


def saving(df,name,path):
    writer = pd.ExcelWriter(path + name +'.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, header=True, sheet_name='Sheet1')
    writer.close()

risk_free_rate=get_risk_free_rate()
stocks=['EUROB.AT','ETE.AT','TPEIR.AT','PPC.AT','HTO.AT','OPAP.AT'
        ,'TITC.AT','CENER.AT','MOH.AT','GEKTERNA.AT','VIO.AT','BELA.AT',
    'ELPE.AT','AKTR.AT']

path=""
#!!!!!!!!!!!!!!!!!!


stock_data=pd.DataFrame()
for i in stocks:
    stock_data[i]=get_data(i)

print(stock_data)

noa=len(stock_data.columns)
rets=pd.DataFrame(np.log(stock_data/stock_data.shift(1)))
rets=rets.dropna()
rets=rets.resample('M').sum()
print(rets)

m=rets.mean()*12
std=rets.std()*np.sqrt(12)
s=rets.cov()*12
cr=rets.corr()

random_portfolios=get_random_portfolios()
optimal_portfolios=pd.DataFrame()


returns=np.linspace(max(min(m),0),max(m),300)
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
print(results)
plotting(random_portfolios,optimal_portfolios,rets,path,ret_max,std_max)
saving(results,'Efficient Frontier Portfolios',path)

