# ====================  PUT  =======================
import requests
from datetime import datetime
username = "ssm07"
graph_id = "ssmgraph1"
token = "fbwj4727rwf"
date = datetime.now().strftime("%Y%m%d")  # e.g. 20260924
url = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}/{date}"
headers = {"X-USER-TOKEN": token}
req_body = {
    "quantity": "45.5"   # Pixela expects string
}
res = requests.put(url, json=req_body, headers=headers, timeout=15)
print("res status_code:", res.status_code)
print("res text:", res.text)
res.raise_for_status()




#===================  DELETE =========================

import requests
username = "ssm07"
graph_id =  "ssmgraph1"
token = "fbwj4727rwf"
url = f"https://pixe.la//v1/users//{username}/graphs/{graph_id}>/<yyyyMMdd>"

#token = 'token' value use in the post request with Username
headers = {"X-USER-TOKEN": token}

res = requests.delete(url, headers=headers, timeout=15)

print("res status_code:", res.status_code)
print("res text:", res.text)

res.raise_for_status()