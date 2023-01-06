from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submitPage")
def index():
    return render_template("submitPage.html")

@app.route("/activatePage")
def index():
    return render_template("activatePage.html")
