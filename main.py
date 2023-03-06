from flask import Flask, json, render_template, redirect, request, session
import os

app = Flask(__name__)

def write_json(schedule_dictionary):
    with open("schedule.json", "w") as f:
        json.dump(schedule_dictionary, f)

schedule_dictionary = {'Monday':{"hour": 6, "minute": 5}, 'Tuesday':{"hour":6, "minute":5}, 'Wednesday':{"hour":6, "minute":5}, 'Thursday':{"hour":6, "minute":5}, 'Friday':{"hour":6, "minute":5}}


if not os.path.isfile('schedule.json'):
    write_json(schedule_dictionary)

with open("schedule.json", "r") as g:
    data = json.load(g)

schedule_dictionary = data


write_json(schedule_dictionary)



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
    print("test")
    global schedule_dictionary
    if request.method == "POST":
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        schedule_dictionary[request.form.get("day")] = {"hour": hour, "minute": minute}
        write_json(schedule_dictionary)
        return render_template("activatePage.html")

@app.route("/b", methods=["POST", "GET"])
def random2():
    if request.method == "POST":
        schedule = request.form.get("onoroff")
        print(schedule)
        return render_template("submitPage.html")

@app.get('/schedule_data')
def return_schedule_data():
    #read in text file
    #update variable
    global schedule_dictionary
    return {"schedule_dictionary":schedule_dictionary}


    
