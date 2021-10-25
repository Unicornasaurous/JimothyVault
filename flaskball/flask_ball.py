#/bin/python3
from os import read
from flask import Flask, render_template, request, flash
from random import *

readings = ["No", "Definitely not", "Yes!", "Nope!", "Ask another time.", "Yessir"]

def reader(): return choice(readings)
EightBall = Flask(__name__); EightBall.secret_key = "ramen"

@EightBalll.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        if request.form.get('submitbutton') == 'Shake The EightBall':
            flash(reader())
            return render_template('index.html')
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    EightBall.run(host="localhost", port=8080, debug=True)