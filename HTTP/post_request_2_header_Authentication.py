import requests
username = "ssm07"
token = "fbwj4727rwf"
url = f"https://pixe.la/v1/users/{username}/graphs"

#token = 'token' value use in the post request with Username
headers = {"X-USER-TOKEN": token}

req_body = {
    "id": "ssmgraph1",
    "name": "Daily Coding",
    "unit": "min",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Kolkata",
    "publishOptionalData": True
}
res = requests.post(url, json=req_body, headers=headers, timeout=15)

print("res status_code:", res.status_code)
print("res text:", res.text)
res.raise_for_status()