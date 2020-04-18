import pandas as pd
import yfinance as yf
import requests

from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Data downloader function


def data_downloader(ticker, period, interval):

    data = yf.download(tickers=ticker, period=period, interval=interval)

    data['Date_new'] = data.index

    data['Date_new'] = pd.to_datetime(data['Date_new'])

    data.reset_index(drop=True, inplace=True)

    data['Date'] = data['Date_new'].dt.strftime('%d.%m.%Y %H:%M:%S')
    data = data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    return data

# Data Read


data_new = data_downloader('^NSEI', "2d", "5m")
data_new = data_new.drop_duplicates(keep=False)
data_new = data_new[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]

# ############################RSI FUNCTION #######################################


def rsi_calculation(rsi_period, data):
    change = data['Close'].diff()
    gain = change.mask(change < 0, 0)
    loss = change.mask(change > 0, 0)
    average_gain = gain.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()
    average_loss = loss.ewm(com=rsi_period - 1, min_periods=rsi_period).mean()
    rs = abs(average_gain / average_loss)
    rsi = 100 - (100 / (1 + rs))
    return rsi

#  #####################################################RSI 9 and 3 calculation on Data#########################


data_new['rsi9'] = rsi_calculation(9, data_new)
data_new['rsi3'] = rsi_calculation(3, data_new)

# Getting rsi value from Data frame
current_rsi = (data_new.iloc[-1:, -2])

rsi_value = (current_rsi[0:, ])

rsi_value = float(rsi_value)


def telegram_bot_send_text(bot_message):
    bot_token = ''
    bot_chat_id = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chat_id \
                + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report(my_message):
    telegram_bot_send_text(my_message)


if (36.0 < rsi_value < 44.0) or (56.0 < rsi_value < 64.0):
    report("#NIFTY BOT Check Nifty 5 min current RSI is "+str(rsi_value))

# END
