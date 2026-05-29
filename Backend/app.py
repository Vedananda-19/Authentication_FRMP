from flask import Flask,request,jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["authentication_frmp"]
users = db["users"]
users.insert_one({"username":"Veda","password":"1234"})

@app.route("/api/login",methods=["GET","POST"])
def login():
    return jsonify("successful")
if __name__=="__main__":
    app.run(debug=True)
