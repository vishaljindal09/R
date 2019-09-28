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







