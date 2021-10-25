#/bin/python3
from os import read
from flask import Flask, render_template, request, flash
from random import *


readings = [# More answers; Better formatting.
  "No.",
  "Definitely not!",
  "Yes!",
  "Nope!",
  "Ask another time.",
  "Yessir!",
  "Outlook Good.",
  "Maybe?",
  "Can't say...",
  "Not certain."
]

def reader(): return choice(readings)# One-Liner; make it so.
EightBall = Flask(__name__); EightBall.secret_key = "ramen"# Related;

@EightBalll.route("/", methods=["POST", "GET"])
def index():

    if request.method == 'POST':
        if request.form.get('submitbutton') == 'Shake The EightBall':
            flash(reader());
            return render_template(
                'index.html'
            )

    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__': EightBall.run(
    # List-Notation for ease of config.
    host="localhost",
    port=8080,
    debug=True
)