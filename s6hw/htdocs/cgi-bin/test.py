import urllib.request
from matplotlib import pyplot as plt

def get_raw_data(ticker, interval='5min'):

    ALPHAVANTAGE_URL = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={apikey}&datatype=csv'.format(ticker=ticker, interval=interval, apikey='IRAS5CPS6HL15I0K'))
    request_handle = urllib.request.urlopen(ALPHAVANTAGE_URL)

    text = request_handle.read()
    text = text.decode('utf-8')

    return text



x = get_raw_data('NFLX', '5min')
hist = []
print(x)
plt.plot(hist)
plt.savefig('test.png')
