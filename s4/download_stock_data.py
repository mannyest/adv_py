import urllib.request

# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=15min&outputsize=full&apikey={}'.format('TSLA', 'UEL5RBEY1Z3J6GY0')

# request_handle = urllib.request.urlopen(url)
# text = request_handle.read()

# text = text.decode('utf-8')

# print(text)


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=15min&outputsize=full&apikey={apikey}'.format(apikey = 'UEL5RBEY1Z3J6GY0', ticker ='TSLA')

request_handle = urllib.request.urlopen(url)
text = request_handle.read()

text = text.decode('utf-8')

print(text)
