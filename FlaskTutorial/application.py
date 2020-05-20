from flask import Flask, render_template, request
import datetime

# export FLASK_APP= app_file_name.py 
# export FLASK_ENV=development
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST","GET"])
def hello():
    if request.method == "GET":
        return "Please"
    else:
        name = request.form.get("name")
        return render_template("hello.html", name=name)