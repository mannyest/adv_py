import urllib.request
import csv
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np


def get_raw_data(ticker, interval='5min'):

    ALPHAVANTAGE_URL = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={apikey}&datatype=csv'.format(ticker=ticker, interval=interval, apikey='UEL5RBEY1Z3J6GY0'))
    request_handle = urllib.request.urlopen(ALPHAVANTAGE_URL)

    text = request_handle.read()
    text = text.decode('utf-8')

    return text


def select_latest_data(text):

    wfh = open('ticker.csv', 'w')
    wfh.write(text)
    wfh.close()

    csv_file = open('ticker.csv')
    text = csv.reader(csv_file)
    next(text)

    ##NTS: use splitlines() on text file instead of writing to .csv and opening

    l_date, l_close, l_volume = [], [], []

    if dt.date.today().weekday() == 5:
        dd = dt.date.today() - dt.timedelta(days = 1)
    elif dt.date.today().weekday() == 6:
        dd = dt.date.today() - dt.timedelta(days = 2)
    else:
        dd = dt.date.today()

    dd = dd.strftime('%Y-%m-%d')

    ##NTS: pull today's date from the last close date instead of this if statement

    for row in text:
        date = row[0][:10]
        close = row[-2]
        volume = row[-1]
        if date == dd:
            l_date.append(date)
            l_close.append(close)
            l_volume.append(volume)

    return l_date[0], l_close[0], l_volume[0], l_close


def write_chart_to_file(history, ticker):
    '''uses matplotlib to create a graph of history and ticker'''
    history = list(reversed(history))
    plt.plot(history)
    plt.savefig('{}_chart.png'.format(ticker))

def get_template_from_file():
    '''loads html stockprice template'''
    STOCK_PRICE_TEMPLATE = open('stock_price_template.html')
    return STOCK_PRICE_TEMPLATE.read()


def write_completed_page_to_file(ticker, text):
    '''writes an html file with the ticker data'''
    ticker_name = '{}.html'.format(ticker)
    file = open(ticker_name, 'w')
    file.write(text)
    file.close()

class Stock:
    """creates object based on the daily stock data available """
    def __init__(self, ticker, interval='5min'):
        text = get_raw_data(ticker, interval)
        date, last_close, last_volume, close_history = select_latest_data(text)
        self.ticker = ticker
        self.date = date
        self.current_price = last_close
        self.volume = last_volume
        self.last_updated = str(dt.datetime.now())[:19]
        self.history = close_history


NFLX = Stock('NFLX', interval = '60min')

template = get_template_from_file()

completed_template = template.format(obj=NFLX)

write_filename = NFLX.ticker + '.html'

write_completed_page_to_file(write_filename, completed_template)

write_chart_to_file(NFLX.history, NFLX.ticker)
