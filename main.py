from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        userinput = request.form.get("username")
        passinput = request.form.get("password")
        if userinput == "admin" and passinput == "admin":
            #Tablechair!2022Auto
            return render_template("submitPage.html")
    return render_template("index.html")

@app.route("/submitPage", methods=["POST", "GET"])
def submitPage():
    return render_template("activatePage.html")

@app.route("/activatePage", methods=["POST", "GET"])
def activatePage():
    return render_template("submitPage.html")

@app.route("/a", methods=["POST", "GET"])
def random():
    if request.method == "POST":
        day = request.form.get("day")
        minute = request.form.get("minute")
        hour = request.form.get("hour")
        print(day, minute, hour)
        return render_template("activatePage.html")

@app.route("/b", methods=["POST", "GET"])
def random2():
    if request.method == "POST":
        schedule = request.form.get("onoroff")
        print(schedule)
        return render_template("submitPage.html")


    
