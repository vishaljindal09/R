# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:48:29 2019

@author: visha
"""

    import yfinance as yf
    import pandas as pd
    import csv
    
    import os
    from datetime import date
    
    today = date.today()
    
    today_str=str(today)
    
    os.chdir(r"F:\\Algo_trading\\DataBase") 
    
    
    
    ###########Merge old and new###################################
    path = os.path.join(os.getcwd(), today_str)
    os.mkdir(path)
    
    with open('Stock_List.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            ticker=row[2]
            filename=row[1]
            data = yf.download(tickers=ticker, period="1d", interval="5m")
            while data.shape[0] < 74:
                data = yf.download(tickers=ticker, period="1d", interval="5m")
            data['Date'] = data.index
    
            data['Date'] = data['Date'].astype(str).str[:-6]
    
            #data['Date']=data['Date'].astype(str).str[6:]
    
            data['Date']= pd.to_datetime(data['Date'])
    
            data.reset_index(drop=True, inplace=True)
    
            #cols = list(data.columns.values)
    
            data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
            olddata=pd.read_csv(filename+'.csv')
            olddata['Date']= pd.to_datetime(olddata['Date'])
            data_new=pd.concat([olddata,data]).drop_duplicates(subset='Date', keep='first').reset_index(drop=True)
            data_new = data_new[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
            file_current=path+'\\'+filename+'.csv'
            data_new.to_csv(file_current,index=False)
            
        
###################Single Get of all FNO 5 minute 60 days##########################
        
with open('Stock_List.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        ticker=row[2]
        filename=row[1]
        data = yf.download(tickers=ticker, period="60d", interval="5m")
        data['Date'] = data.index

        data['Date'] = data['Date'].astype(str).str[:-6]

        #data['Date']=data['Date'].astype(str).str[6:]

        data['Date']= pd.to_datetime(data['Date'])

        data.reset_index(drop=True, inplace=True)

        #cols = list(data.columns.values)

        data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        file_current=filename+'.csv'
        data.to_csv(file_current,index=False)


##############1 day recurring############
os.chdir(r"F:\\Algo_trading\\DataBase-1D")

path = os.path.join(os.getcwd(), today_str)
os.mkdir(path)

with open('Stock_List-1D.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        ticker=row[2]
        filename=row[1]
        data = yf.download(tickers=ticker, period="7d", interval="1d")
        while data.shape[0] < 1:
            data = yf.download(tickers=ticker, period="7d", interval="1d")
        data['Date'] = data.index


        data['Date']= pd.to_datetime(data['Date'])

        data.reset_index(drop=True, inplace=True)

        #cols = list(data.columns.values)

        data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        olddata=pd.read_csv(filename+'.csv')
        olddata['Date']= pd.to_datetime(olddata['Date'])
        data_new=pd.concat([olddata,data]).drop_duplicates(subset='Date', keep='first').reset_index(drop=True)
        data_new = data_new[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        file_current=path+'\\'+filename+'.csv'
        data_new.to_csv(file_current,index=False)


###################Single Get of all FNO 1D 1000 Days ##########################

  
with open('Stock_List-1D.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        ticker=row[2]
        filename=row[1]
        data = yf.download(tickers=ticker, period="999d", interval="1d")
        data['Date'] = data.index

        #data['Date']=data['Date'].astype(str).str[6:]

        data['Date']= pd.to_datetime(data['Date'])

        data.reset_index(drop=True, inplace=True)

        #cols = list(data.columns.values)

        data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
        file_current=filename+'.csv'
        data.to_csv(file_current,index=False)


#################NINJA##################
        
        
os.chdir(r"F:\\Algo_trading\\Ninja")

path = os.path.join(os.getcwd(), today_str)
os.mkdir(path)
    
with open('Stock_List.csv','rt')as f:
        data = csv.reader(f)
        for row in data:
            ticker=row[2]
            filename=row[1]
            data = yf.download(tickers=ticker, period="1d", interval="1m")
            #while data.shape[0] < 1499:
            #    data = yf.download(tickers=ticker, period="1d", interval="1m")
            data['Date'] = data.index
      
            data['Date']= pd.to_datetime(data['Date'])
    
            data.reset_index(drop=True, inplace=True)
    
            #cols = list(data.columns.values)
    
            data['Date_new'] = data['Date'].dt.strftime('%Y%m%d %H%M%S')

            data = data[['Date_new','Open', 'High', 'Low', 'Close','Volume']]
            data.loc[data['Volume'] ==0, 'Volume'] = 100
            
            file_current=path+'\\'+filename+'.txt'
            data.to_csv(file_current,index=False,sep=';',header=False)
            
        






data=pd.read_csv('NIFTY'+'.csv') 

filename='NSE1d'

data = yf.download(tickers='ADANIENT.NS', period="4d", interval="5m")

data['Date'] = data.index


data['Date']= pd.to_datetime(data['Date'])

data['Date_new'] = data['Date'].dt.strftime('%Y%m%d %H%M%S')

data = data[['Date_new','Open', 'High', 'Low', 'Close','Volume']]

data.loc[data['Volume'] ==0, 'Volume'] = 100


file_current=path+'\\'+filename+'.txt'
data.to_csv('ACC.txt',index=False,sep=';',header=False)




data.to_csv(filename+'.csv')



data.head()


data = yf.download(tickers="IGL.NS", period="60mo", interval="1d")



data.to_csv('NSE1d.csv') 

high=data['High']

max_value=max(high)

low=data['Low']
min_value=min(low)

data['Date'] = data.index


data['Date']= pd.to_datetime(data['Date']) 


data.reset_index(drop=True, inplace=True)

Todays_range=abs(max_value-min_value)

level_618=Todays_range*0.618
level_382=Todays_range*0.382
level_113=Todays_range*1.13
level_1618=Todays_range*1.618
level_1382=Todays_range*1.382




level_above_min_382=round(min_value+level_382,2)
level_above_min_618=round(min_value+level_618,2)
level_above_min_113=round(min_value+level_113,2)
level_above_min_1382=round(min_value+level_1382,2)
level_above_min_1618=round(min_value+level_1618,2)



level_below_max_113=round(max_value-level_113,2)
level_below_max_1382=round(max_value-level_1382,2)
level_below_max_1618=round(max_value-level_1618,2)



#plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

import pandas as pd

trace = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])


trace.layout.xaxis.type = 'category'
trace.layout.xaxis.showgrid= False
trace.layout.yaxis.showgrid= False
#trace.update_yaxes(nticks=50)
trace.update_yaxes(dtick=20)
trace.update_xaxes(showticklabels=False)
trace.update_layout(xaxis_rangeslider_visible=False)
#trace.update_xaxes(nticks=78)

trace.update_layout(
    title='The Nifty Levels',
    yaxis_title='Nifty Spot',
    xaxis_title='Last 3 days 15 min Chart',
    shapes = [dict(
        x0=0, x1=1, y0=level_above_min_382, y1=level_above_min_382, xref='paper',
        line_width=2)],
    annotations=[dict(
        x=0, y=level_above_min_382+5, xref='paper',
        showarrow=False, xanchor='left', text=str(level_above_min_382)+'level')]
)


trace.update_layout(
    title='The Nifty Levels',
    yaxis_title='Nifty Spot',
    xaxis_title='Last 3 days 15 min Chart',
    shapes = [dict(
        x0=0, x1=1, y0=level_above_min_382, y1=level_above_min_382, xref='paper',
        line_width=2)],
    annotations=[dict(
        x=0, y=level_above_min_382+5, xref='paper',
        showarrow=False, xanchor='left', text=str(level_above_min_382)+'level')]
)


trace.update_layout(
    shapes=[
        # Line Vertical
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_382,
            x1=1,
            y1=level_above_min_382,
            xref='paper',
            line=dict(
                color="RoyalBlue",
                width=3
            )
        ),
        # Line Horizontal
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_618,
            x1=1,
            y1=level_above_min_618,
            xref='paper',
            line=dict(
                color="RoyalBlue",
                width=3
            )
        ),
        # Line Diagonal
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_113,
            x1=1,
            y1=level_above_min_113,
            xref='paper',
            line=dict(
                color="RoyalBlue",
                width=3
            )
        ),
    ]
)


trace.update_layout(
    showlegend=False,
    annotations=[
        go.layout.Annotation(
            x=0,
            y=level_above_min_382+5,
            xref='paper',
            text="dict Text",
            showarrow=False, 
            xanchor='left'
        )
    ]
    
)














trace.write_html('check.html', auto_open=True)


import urllib.request
import threading
 
def run_check():
    threading.Timer(5.0, run_check).start()
    urllib.request.urlopen("http://domain.tld?parameter=value&parameter2=value").read()
    print("HTTP Request sent.")
 
run_check()


import requests

def telegram_bot_sendtext(bot_message):

    bot_token = '916925173:AAG-CuT8gB78nT9_NjpwHQpUss9A4ZYEJP8'
    bot_chatID = '-399094458'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



test = telegram_bot_sendtext("This is done!!")
print(test)



