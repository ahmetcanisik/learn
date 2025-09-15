from flask import Flask, render_template, request

app = Flask(__name__)

lang = "en"

SPORTS = ["Soccer", "Basketball", "Tennis"]


@app.route('/')
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", lang=lang, name=name)


@app.route("/sports")
def sports():
    return render_template("sports.html", sports=SPORTS)