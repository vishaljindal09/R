# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:15:32 2019

@author: vjindal
"""

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='JZRCJ20462KEZ0ED')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('TITAN')

from nsetools import Nse

nse=Nse()


q=nse.get_quote('infy')


q=nse.get_quote('NIFTY 50')



import yfinance as yf
import pandas as pd

data = yf.download(tickers="^NSEI", period="1d", interval="1m")
data.head()

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

trace = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])


trace.layout.xaxis.type = 'category'
trace.layout.xaxis.showgrid= False
trace.layout.yaxis.showgrid= False
trace.update_yaxes(nticks=50)
trace.update_yaxes(tickmode='auto')
#trace.update_xaxes(nticks=78)
trace.update_xaxes(tickformat = '%H:%M')

'%Y-%m-%d'

trace.show()







