import requests, bs4

res = requests.get('http://api.open-notify.org/iss-now.json')

res.raise_for_status() #it will only run if the status code != 200 and there is any error 

print(res.json())