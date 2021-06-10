from flask import  render_template, Flask
from flask.globals import request
from flask.json import jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient, collection

app = Flask("MY_HEALTH_APP")
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/"
mongo = PyMongo(app)
client = MongoClient("mongodb://127.0.0.1:27017/")

collection = client.yserdb.u_collection

get_data = lambda x : request.args.get(x)

@app.route("/form.html")
def form():
    return render_template("form.html")

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/doctors.html")
def doctor():
    return render_template("doctors.html")

@app.route('/patientdata', methods=["GET"])
def patient_data():    
    db = {
        "fname": get_data("fname"),
        "lname": get_data("lname"),
        "Phone": get_data("Phone"), 
        "Email": get_data("Email"),
        "Health": get_data("Health")
    }

    collection.insert_one(db)
    return render_template("app_s.html")

@app.route('/subscribtion', methods=["GET"])
def subscription():
    msg = request.args.get("Message")
    db = {
        "Message": msg
    }
    collection.insert_one(db)
    return render_template("sub_success.html")


app.run(port=5555, debug=True)

    




