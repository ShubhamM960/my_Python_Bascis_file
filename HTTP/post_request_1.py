import os
import requests
url = "https://pixe.la/v1/users"
body = {
    "token": "fbwj4727rwf",
    "username": "ssm07",  
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThisIsThanksCode",
}
res = requests.post(url, json=body, timeout=15)
print(f"body: {res.text}")   # important: shows exact Pixela error reason
res.raise_for_status()
data = res.json()
print(data)