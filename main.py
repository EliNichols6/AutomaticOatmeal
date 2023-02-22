from flask import Flask, json, render_template, redirect, request, session

app = Flask(__name__)

def write_text(default_dictionary):
    with open("myfile.json", 'w') as f: 
        for key, value in default_dictionary.items(): 
            f.write('%s:%s\n' % (key, value))

default_dictionary = {'Monday':{"hour": 6, "minute": 5}, 'Tuesday':{"hour":6, "minute":5}, 'Wednesday':{"hour":6, "minute":5}, 'Thursday':{"hour":6, "minute":5}, 'Friday':{"hour":6, "minute":5}}
write_text(default_dictionary)



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
    global updated_dictionary
    if request.method == "POST":
        hour = request.form.get("hour")
        minute = request.form.get("minute")
        default_dictionary[request.form.get("day")] = {"hour": hour, "minute": minute}
        print(minute, hour)
        write_text(default_dictionary)
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
    global default_dictionary
    return {"default_dictionary":default_dictionary}


    
