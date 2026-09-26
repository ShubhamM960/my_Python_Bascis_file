import requests, bs4

res = requests.request('GET','http://api.open-notify.org/iss-now.json')

res.raise_for_status() #it will only run if the status code != 200 and there is any error 

data =res.json() # stores the value in the form of "dictonary"
print(f"iss_position {data['iss_position']}")
print(f"latitude is : {data['iss_position']['latitude']}")
print(f"longitude is : {data['iss_position']['longitude']}")