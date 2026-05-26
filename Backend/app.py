from flask import Flask,request,jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["authentication_frmp"]
users = db["users"]
users.insert_one({"username":"Veda","password":"1234"})

@app.route("/")
def home():
    user_list = list(users.find())
    print("Hello")
    for doc in user_list:
        doc["_id"] = str(doc["_id"])
    return jsonify(user_list)
if __name__=="__main__":
    app.run(debug=True)
