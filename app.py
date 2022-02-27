from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/general")
def gen_details():
    return render_template("gen details.html")


@app.route("/student")
def student():
    return render_template("student.html")


@app.route("/teacher")
def teacher():
    return render_template("teacher.html")


@app.route("/question")
def question():
    return render_template("questions.html")


@app.route("/report")
def report():
    return render_template("report.html")


@app.route("/mcq")
def mcq():
    return render_template("mcq.html")


if __name__ == "__main__":
    app.run(debug=True)
