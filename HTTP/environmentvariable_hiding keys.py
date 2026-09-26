import requests, bs4
import os
url = 'https://api.sunrise-sunset.org/json'
parameters = {
    'lat' : '36.7201600', 
    'lng' : '-4.4203400', 
    'date' : '2026-09-23', 
    'apikey' : os.environ.get("API_KEY")
    }
res = requests.get(url, params = parameters)
res.raise_for_status()
print(res.json())



#============================  TERMINAL  =========================
# >>> export API_KEY = wfwfwfwlf854784894efjgw
#Click Enter - now this value will be save in the environment, use it in the code as " os.environ.get("API_KEY") ""