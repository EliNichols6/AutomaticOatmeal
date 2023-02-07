from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

schedule_dictionary = {}

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        userinput = request.form.get("username")
        passinput = request.form.get("password")
        print(userinput)
        print(passinput)
        if userinput == "admin" and passinput == "admin":
            print(userinput)
            print(passinput)
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
    global schedule_dictionary
    if request.method == "POST":
        schedule_dictionary["day"] = request.form.get("day")
        schedule_dictionary["minute"] = request.form.get("minute")
        schedule_dictionary["hour"] = request.form.get("hour")
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

@app.get('/schedule_data')
def return_schedule_data():
    global schedule_dictionary
    return {"schedule_dictoinary":schedule_dictionary}


    
