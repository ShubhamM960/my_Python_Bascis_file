# ====================  PUT REQUEST =======================
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
# ====================  PUT REST RESOURCE =======================
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean


#map the web URLs to pyton fuctions
app = Flask(__name__)

@app.route("/users/<username>/graphs/<graph_id>/<date>", methods=["PUT"])
def put_value(username, graph_id, date ):
    pass
#==================================================================

#========================== PATCH REST RESOURCE  ================================
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(cafe_id):
    pass

@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_coffee_price(**kwargs):
    cafe_id = kwargs["cafe_id"]
    