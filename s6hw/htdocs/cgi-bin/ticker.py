#!/usr/bin/env python

import cgi
import urllib.request
import csv
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
import os

form = cgi.FieldStorage()

print("Content-type:  text/html\n")

print("<HTML><HEAD></HEAD><BODY>")
print("<p>Ticker:  {}</p>".format(form.getvalue("ticker")))
print("<p>Interval:  {}</p>".format(form.getvalue("interval")))
print("</BODY><HTML>")


BASE_DIR = '/Users/pipedriveloaner/Desktop/Py/advpy/s6/s6hw/htdocs'

IMAGES_DIR = os.path.join(BASE_DIR, 'images')
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

STOCK_PRICE_TEMPLATE = os.path.join(TEMPLATES_DIR, 'stock_price_template.html')


def get_raw_data(ticker, interval='5min'):

    ALPHAVANTAGE_URL = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={apikey}&datatype=csv'.format(ticker=ticker, interval=interval, apikey='IRAS5CPS6HL15I0K'))
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
    ##NTS: pull today's date from the last close date instead of this if statement

    dd = dd.strftime('%Y-%m-%d')

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
    stock_template = open(STOCK_PRICE_TEMPLATE)
    return stock_template.read()


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


choice = Stock(ticker = form.getvalue('ticker'), interval = form.getvalue('interval'))

template = get_template_from_file()
completed_template = template.format(obj=choice)

write_chart_to_file(choice.history, choice.ticker)

print(completed_template)

