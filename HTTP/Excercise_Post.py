import requests

url = "https://app.100daysofpython.dev/v1/nutrition/natural/excerice"

payload = {
    "query": "ran 3 miles and cycled for 30 minutes"
}

headers = {
    "Content-Type": "application/json",
    # Add auth headers if your API requires them:
    "x-app-id": "YOUR_APP_ID",
    "x-api-key": "YOUR_API_KEY",
}

response = requests.post(url, json=payload, headers=headers, timeout=30)

print("Status:", response.status_code)
print("Response:", response.text)

# If response is JSON:
print('final response is', response.json()) 