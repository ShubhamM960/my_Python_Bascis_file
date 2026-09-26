import requests, bs4
url = 'https://api.sunrise-sunset.org/json'
parameters = {'lat' : '36.7201600', 'lng' : '-4.4203400', 'date' : '2026-09-23', 'formatted' : '0'}
res = requests.get(url, params = parameters)
print('URL is : ', res.url)
res.raise_for_status()
print(res.json())