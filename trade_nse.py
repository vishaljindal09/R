# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 19:48:29 2019

@author: visha
"""

import yfinance as yf
import pandas as pd
from datetime import date

##########NIFTY#######

data = yf.download(tickers="^NSEI", period="2d", interval="15m")

#data.head()

data['Date'] = data.index

data['Date'] = data['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data['Date']= pd.to_datetime(data['Date'])

data.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

#data['Date']= pd.to_datetime(data['Date']) 

#data = yf.download(tickers="BPCL.NS", period="60d", interval="5m")


today = date.today()

today_str=str(today)

today=pd.to_datetime(today)

mask = (data['Date'] < today)

#When running on same day market hour

#data_ready=(data.loc[mask])

data_ready=data


#data.to_csv('BPCL.csv') 

high=data_ready['High']

max_value=max(high)

low=data_ready['Low']
min_value=min(low)

Todays_range=abs(max_value-min_value)

level_382=Todays_range*0.382
level_618=Todays_range*0.618
level_113=Todays_range*1.13
level_1618=Todays_range*1.618
level_1382=Todays_range*1.382


min_value=round(min_value,2)
max_value=round(max_value,2)

level_above_min_382=round(min_value+level_382,2)
level_above_min_618=round(min_value+level_618,2)
level_above_min_113=round(min_value+level_113,2)
level_above_min_1382=round(min_value+level_1382,2)
level_above_min_1618=round(min_value+level_1618,2)



level_below_max_113=round(max_value-level_113,2)
level_below_max_1382=round(max_value-level_1382,2)
level_below_max_1618=round(max_value-level_1618,2)


data_5 = yf.download(tickers="^NSEI", period="5d", interval="15m")


data_5['Date'] = data_5.index

data_5['Date'] = data_5['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data_5['Date']= pd.to_datetime(data_5['Date'])

data_5.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data_5 = data_5[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]


#plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

import pandas as pd

trace = go.Figure(data=[go.Candlestick(x=data_5['Date'],
                open=data_5['Open'],
                high=data_5['High'],
                low=data_5['Low'],
                close=data_5['Close'])])

#data['Date'].strptime('%m-%d %H:%M:%S')

trace.layout.xaxis.type = 'category'
trace.layout.xaxis.showgrid= False
trace.layout.yaxis.showgrid= False
#trace.update_yaxes(nticks=50)
trace.update_yaxes(dtick=20)
trace.update_xaxes(showticklabels=False)
trace.update_layout(xaxis_rangeslider_visible=False)
#trace.update_xaxes(nticks=78)
#trace.update_xaxes(tickformat="%H~%M~%S.%2f")

trace.update_layout(
    yaxis_title='Nifty Spot',
    xaxis_title='Last 5 days 15 min Chart'
)


trace.update_layout(
    title=go.layout.Title(
        text="The Nifty Levels for "+today_str,
        xref="paper",
        x=.5
    )
)



# =============================================================================
# trace.update_layout(
#     title='The Nifty Levels',
#     yxis_title='Nifty Spot',
#     xaxis_title='Last 3 days 15 min Chart',
#     shapes = [dict(
#         x0=0, x1=1, y0=level_above_min_382, y1=level_above_min_382, xref='paper',
#         line_width=2)],
#     annotations=[dict(
#         x=0, y=level_above_min_382+5, xref='paper',
#         showarrow=False, xanchor='left', text=str(level_above_min_382)+'level')]
# )
# =============================================================================


trace.update_layout(
    shapes=[
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=min_value,
            x1=1,
            y1=min_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=max_value,
            x1=1,
            y1=max_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal .382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_382,
            x1=1,
            y1=level_above_min_382,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal .618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_618,
            x1=1,
            y1=level_above_min_618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_113,
            x1=1,
            y1=level_above_min_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1382,
            x1=1,
            y1=level_above_min_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1618,
            x1=1,
            y1=level_above_min_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal below 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_113,
            x1=1,
            y1=level_below_max_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal below 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1382,
            x1=1,
            y1=level_below_max_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal below 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1618,
            x1=1,
            y1=level_below_max_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
    ]
)


trace.update_layout(
    showlegend=False,
    annotations=[
        #Base Level
        go.layout.Annotation(
            x=0,
            y=min_value-9,
            xref='paper',
            text="Level 0-"+str(min_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #Base Level
        go.layout.Annotation(
            x=0,
            y=max_value+9,
            xref='paper',
            text="Level 1 -"+str(max_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_382
        go.layout.Annotation(
            x=0,
            y=level_above_min_382+9,
            xref='paper',
            text="Level .382 -"+str(level_above_min_382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_618
        go.layout.Annotation(
            x=0,
            y=level_above_min_618+9,
            xref='paper',
            text="Level .618 -"+str(level_above_min_618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_113
        go.layout.Annotation(
            x=0,
            y=level_above_min_113+9,
            xref='paper',
            text="Level 1.13 -"+str(level_above_min_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1382
        go.layout.Annotation(
            x=0,
            y=level_above_min_1382+9,
            xref='paper',
            text="Level 1.382 -"+str(level_above_min_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_116
        go.layout.Annotation(
            x=0,
            y=level_above_min_1618+9,
            xref='paper',
            text="Level 1.618 -"+str(level_above_min_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_113
        go.layout.Annotation(
            x=0,
            y=level_below_max_113-9,
            xref='paper',
            text="Level 1.13 -"+str(level_below_max_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_1382
        go.layout.Annotation(
            x=0,
            y=level_below_max_1382-9,
            xref='paper',
            text="Level 1.382 -"+str(level_below_max_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1618
        go.layout.Annotation(
            x=0,
            y=level_below_max_1618-9,
            xref='paper',
            text="Level 1.618 -"+str(level_below_max_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        
    ]
    
)













trace.write_html('NIFTY.html', auto_open=True)




###################BANKNIFTY#############

dataBNF = yf.download(tickers="^NSEBANK", period="2d", interval="15m")

#data.head()

dataBNF['Date'] = dataBNF.index

dataBNF['Date'] = dataBNF['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

dataBNF['Date']= pd.to_datetime(dataBNF['Date'])

dataBNF.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

dataBNF = dataBNF[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

#data['Date']= pd.to_datetime(data['Date']) 

#data = yf.download(tickers="BPCL.NS", period="60d", interval="5m")


today = date.today()

today_str=str(today)

today=pd.to_datetime(today)

mask = (dataBNF['Date'] < today)

#Current day market hrs

#dataBNF_ready=(dataBNF.loc[mask])

dataBNF_ready=dataBNF

#data.to_csv('BPCL.csv') 

high=dataBNF_ready['High']

max_value=max(high)

low=dataBNF_ready['Low']
min_value=min(low)

Todays_range=abs(max_value-min_value)

level_382=Todays_range*0.382
level_618=Todays_range*0.618
level_113=Todays_range*1.13
level_1618=Todays_range*1.618
level_1382=Todays_range*1.382


min_value=round(min_value,2)
max_value=round(max_value,2)

level_above_min_382=round(min_value+level_382,2)
level_above_min_618=round(min_value+level_618,2)
level_above_min_113=round(min_value+level_113,2)
level_above_min_1382=round(min_value+level_1382,2)
level_above_min_1618=round(min_value+level_1618,2)



level_below_max_113=round(max_value-level_113,2)
level_below_max_1382=round(max_value-level_1382,2)
level_below_max_1618=round(max_value-level_1618,2)


data_BNF_5 = yf.download(tickers="^NSEBANK", period="5d", interval="15m")


data_BNF_5['Date'] = data_BNF_5.index

data_BNF_5['Date'] = data_BNF_5['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data_BNF_5['Date']= pd.to_datetime(data_BNF_5['Date'])

data_BNF_5.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data_BNF_5 = data_BNF_5[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]


#plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

import pandas as pd

trace = go.Figure(data=[go.Candlestick(x=data_BNF_5['Date'],
                open=data_BNF_5['Open'],
                high=data_BNF_5['High'],
                low=data_BNF_5['Low'],
                close=data_BNF_5['Close'])])

#data['Date'].strptime('%m-%d %H:%M:%S')

trace.layout.xaxis.type = 'category'
trace.layout.xaxis.showgrid= False
trace.layout.yaxis.showgrid= False
#trace.update_yaxes(nticks=50)
trace.update_yaxes(dtick=20)
trace.update_xaxes(showticklabels=False)
trace.update_layout(xaxis_rangeslider_visible=False)
#trace.update_xaxes(nticks=78)
#trace.update_xaxes(tickformat="%H~%M~%S.%2f")

trace.update_layout(
    yaxis_title='BANK Nifty Spot',
    xaxis_title='Last 5 days 15 min Chart'
)


trace.update_layout(
    title=go.layout.Title(
        text="The BANK Nifty Levels for "+today_str,
        xref="paper",
        x=.5
    )
)



# =============================================================================
# trace.update_layout(
#     title='The Nifty Levels',
#     yxis_title='Nifty Spot',
#     xaxis_title='Last 3 days 15 min Chart',
#     shapes = [dict(
#         x0=0, x1=1, y0=level_above_min_382, y1=level_above_min_382, xref='paper',
#         line_width=2)],
#     annotations=[dict(
#         x=0, y=level_above_min_382+5, xref='paper',
#         showarrow=False, xanchor='left', text=str(level_above_min_382)+'level')]
# )
# =============================================================================


trace.update_layout(
    shapes=[
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=min_value,
            x1=1,
            y1=min_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=max_value,
            x1=1,
            y1=max_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal .382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_382,
            x1=1,
            y1=level_above_min_382,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal .618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_618,
            x1=1,
            y1=level_above_min_618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_113,
            x1=1,
            y1=level_above_min_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1382,
            x1=1,
            y1=level_above_min_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1618,
            x1=1,
            y1=level_above_min_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal below 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_113,
            x1=1,
            y1=level_below_max_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal below 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1382,
            x1=1,
            y1=level_below_max_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal below 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1618,
            x1=1,
            y1=level_below_max_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
    ]
)


trace.update_layout(
    showlegend=False,
    annotations=[
        #Base Level
        go.layout.Annotation(
            x=0,
            y=min_value-27,
            xref='paper',
            text="Level 0-"+str(min_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #Base Level
        go.layout.Annotation(
            x=0,
            y=max_value+27,
            xref='paper',
            text="Level 1 -"+str(max_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_382
        go.layout.Annotation(
            x=0,
            y=level_above_min_382+27,
            xref='paper',
            text="Level .382 -"+str(level_above_min_382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_618
        go.layout.Annotation(
            x=0,
            y=level_above_min_618+27,
            xref='paper',
            text="Level .618 -"+str(level_above_min_618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_113
        go.layout.Annotation(
            x=0,
            y=level_above_min_113+27,
            xref='paper',
            text="Level 1.13 -"+str(level_above_min_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1382
        go.layout.Annotation(
            x=0,
            y=level_above_min_1382+27,
            xref='paper',
            text="Level 1.382 -"+str(level_above_min_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_116
        go.layout.Annotation(
            x=0,
            y=level_above_min_1618+27,
            xref='paper',
            text="Level 1.618 -"+str(level_above_min_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_113
        go.layout.Annotation(
            x=0,
            y=level_below_max_113-27,
            xref='paper',
            text="Level 1.13 -"+str(level_below_max_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_1382
        go.layout.Annotation(
            x=0,
            y=level_below_max_1382-27,
            xref='paper',
            text="Level 1.382 -"+str(level_below_max_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1618
        go.layout.Annotation(
            x=0,
            y=level_below_max_1618-27,
            xref='paper',
            text="Level 1.618 -"+str(level_below_max_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        
    ]
    
)














trace.write_html('BANKNIFTY.html', auto_open=True)



#############Nifty 30 Min candle#######


data = yf.download(tickers="^NSEI", period="3d", interval="30m")

#data.head()

data['Date'] = data.index

data['Date'] = data['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data['Date']= pd.to_datetime(data['Date'])

data.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

#data['Date']= pd.to_datetime(data['Date']) 

#data = yf.download(tickers="BPCL.NS", period="60d", interval="5m")


today = date.today()

today_str=str(today)

today=pd.to_datetime(today)

mask = (data['Date'] < today)
data_ready=(data.loc[mask])


#data.to_csv('BPCL.csv') 

high=data_ready['High']

max_value=max(high)

low=data_ready['Low']
min_value=min(low)

Todays_range=abs(max_value-min_value)

level_382=Todays_range*0.382
level_618=Todays_range*0.618
level_113=Todays_range*1.13
level_1618=Todays_range*1.618
level_1382=Todays_range*1.382


min_value=round(min_value,2)
max_value=round(max_value,2)

level_above_min_382=round(min_value+level_382,2)
level_above_min_618=round(min_value+level_618,2)
level_above_min_113=round(min_value+level_113,2)
level_above_min_1382=round(min_value+level_1382,2)
level_above_min_1618=round(min_value+level_1618,2)



level_below_max_113=round(max_value-level_113,2)
level_below_max_1382=round(max_value-level_1382,2)
level_below_max_1618=round(max_value-level_1618,2)


data_5 = yf.download(tickers="^NSEI", period="5d", interval="30m")


data_5['Date'] = data_5.index

data_5['Date'] = data_5['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data_5['Date']= pd.to_datetime(data_5['Date'])

data_5.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data_5 = data_5[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]


#plotly.offline.init_notebook_mode()
import plotly.graph_objs as go

import pandas as pd

trace = go.Figure(data=[go.Candlestick(x=data_5['Date'],
                open=data_5['Open'],
                high=data_5['High'],
                low=data_5['Low'],
                close=data_5['Close'])])

#data['Date'].strptime('%m-%d %H:%M:%S')

trace.layout.xaxis.type = 'category'
trace.layout.xaxis.showgrid= False
trace.layout.yaxis.showgrid= False
#trace.update_yaxes(nticks=50)
trace.update_yaxes(dtick=20)
trace.update_xaxes(showticklabels=False)
trace.update_layout(xaxis_rangeslider_visible=False)
#trace.update_xaxes(nticks=78)
#trace.update_xaxes(tickformat="%H~%M~%S.%2f")

trace.update_layout(
    yaxis_title='Nifty Spot',
    xaxis_title='Last 5 days 30 min Chart'
)


trace.update_layout(
    title=go.layout.Title(
        text="The Nifty Levels for "+today_str,
        xref="paper",
        x=.5
    )
)



# =============================================================================
# trace.update_layout(
#     title='The Nifty Levels',
#     yxis_title='Nifty Spot',
#     xaxis_title='Last 3 days 15 min Chart',
#     shapes = [dict(
#         x0=0, x1=1, y0=level_above_min_382, y1=level_above_min_382, xref='paper',
#         line_width=2)],
#     annotations=[dict(
#         x=0, y=level_above_min_382+5, xref='paper',
#         showarrow=False, xanchor='left', text=str(level_above_min_382)+'level')]
# )
# =============================================================================


trace.update_layout(
    shapes=[
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=min_value,
            x1=1,
            y1=min_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Base
        go.layout.Shape(
            type="line",
            x0=0,
            y0=max_value,
            x1=1,
            y1=max_value,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal .382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_382,
            x1=1,
            y1=level_above_min_382,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal .618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_618,
            x1=1,
            y1=level_above_min_618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_113,
            x1=1,
            y1=level_above_min_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1382,
            x1=1,
            y1=level_above_min_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_above_min_1618,
            x1=1,
            y1=level_above_min_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
        # Line Horizontal below 1.13
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_113,
            x1=1,
            y1=level_below_max_113,
            xref='paper',
            line=dict(
                color="Red",
                width=3
            )
        ),
        # Line Horizontal below 1.382
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1382,
            x1=1,
            y1=level_below_max_1382,
            xref='paper',
            line=dict(
                color="Green",
                width=3
            )
        ),
        # Line Horizontal below 1.618
        go.layout.Shape(
            type="line",
            x0=0,
            y0=level_below_max_1618,
            x1=1,
            y1=level_below_max_1618,
            xref='paper',
            line=dict(
                color="Black",
                width=3
            )
        ),
    ]
)


trace.update_layout(
    showlegend=False,
    annotations=[
        #Base Level
        go.layout.Annotation(
            x=0,
            y=min_value-9,
            xref='paper',
            text="Level 0-"+str(min_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #Base Level
        go.layout.Annotation(
            x=0,
            y=max_value+9,
            xref='paper',
            text="Level 1 -"+str(max_value),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_382
        go.layout.Annotation(
            x=0,
            y=level_above_min_382+9,
            xref='paper',
            text="Level .382 -"+str(level_above_min_382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_618
        go.layout.Annotation(
            x=0,
            y=level_above_min_618+9,
            xref='paper',
            text="Level .618 -"+str(level_above_min_618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_113
        go.layout.Annotation(
            x=0,
            y=level_above_min_113+9,
            xref='paper',
            text="Level 1.13 -"+str(level_above_min_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1382
        go.layout.Annotation(
            x=0,
            y=level_above_min_1382+9,
            xref='paper',
            text="Level 1.382 -"+str(level_above_min_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_116
        go.layout.Annotation(
            x=0,
            y=level_above_min_1618+9,
            xref='paper',
            text="Level 1.618 -"+str(level_above_min_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_113
        go.layout.Annotation(
            x=0,
            y=level_below_max_113-9,
            xref='paper',
            text="Level 1.13 -"+str(level_below_max_113),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #below_max_1382
        go.layout.Annotation(
            x=0,
            y=level_below_max_1382-9,
            xref='paper',
            text="Level 1.382 -"+str(level_below_max_1382),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        #level_above_min_1618
        go.layout.Annotation(
            x=0,
            y=level_below_max_1618-9,
            xref='paper',
            text="Level 1.618 -"+str(level_below_max_1618),
            showarrow=False, 
            xanchor='left',
            xshift=1107
        ),
        
    ]
    
)













trace.write_html('NIFTY_30.html', auto_open=True)






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




#########################

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:44:59 2019

@author: vjindal
"""

import yfinance as yf
import pandas as pd
import os
#from datetime import date

def main():
    
    print("Current Working Directory " , os.getcwd())
    
    
    try:
        # Change the current working Directory    
        os.chdir("C:\\Users\\vjindal\\Resources\\Personal\\Trade")
        print("Directory changed")
    except OSError:
        print("Can't change the Current Working Directory")        
 
    print("Current Working Directory " , os.getcwd())
    
    # Check if New path exists
    if os.path.exists("/home/varun/temp") :
        # Change the current working Directory    
        os.chdir("/home/varun/temp")
    else:
        print("Can't change the Current Working Directory")    
 
        
    
    print("Current Working Directory " , os.getcwd())
    
if __name__ == '__main__':
    main()


ticker="^NSEI"

##########NIFTY#######

data = yf.download(tickers="^NSEI", period="2d", interval="1m")

#data.head()

data['Date'] = data.index

data['Date'] = data['Date'].astype(str).str[:-6]

#data['Date']=data['Date'].astype(str).str[6:]

data['Date']= pd.to_datetime(data['Date'])

data.reset_index(drop=True, inplace=True)

#cols = list(data.columns.values)

data = data[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]



data_new = yf.download(tickers=ticker, period="2d", interval="1m")


data_new['Date'] = data_new.index

data_new['Date'] = data_new['Date'].astype(str).str[:-6]

#data_new['Date']=data_new['Date'].astype(str).str[6:]

data_new['Date']= pd.to_datetime(data_new['Date'])

data_new.reset_index(drop=True, inplace=True)

#cols = list(data_new.columns.values)

data_new = data_new[['Date','Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]


olddf=pd.concat([data,data_new]).drop_duplicates().reset_index(drop=True)




