#Client 
#===========
import requests

payload = {
    "username": "johndoe",
    "email": "john@example.com"
}
paramaters = {"v" : "34"}
res = requests.request("POST", "https://httpbin.org/post" , json = payload, params = paramaters)
#res = requests.request("POST", "https://httpbin.org/post" , data = payload)

print(res.status_code)
print(res.json())

res.raise_for_status()




#====================================
# from the cleint side when we use a "POST" request and content using  "json" / "data" argument in HTTP Request 
# At the server side read this by using "request" of package : 'flask' as below :
#########if content has sent using paramater "data" : request.form.get('key1') , request.form['key2'],  request.form.get('key3') 
#########if content has sent using paramater "json" : request.get_json().get('key1')

########## to accesss the value of the paramaters  : request.args.get("param_name")

# Server : 
# ============
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/path", methods = ["POST"])
def my_post_req():
    name = request.get_json().get('username')
    emailId = request.get_json().get('email')
    
    return jsonify(message = {"Successfully received the data"}), 201