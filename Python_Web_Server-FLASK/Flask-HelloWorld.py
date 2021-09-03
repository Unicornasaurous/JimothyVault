from flask import Flask

FlaskApp = Flask(__name__)

@FlaskApp.route('/HelloWorld')
def HelloWorld():
    return 'Hello, World!'

@FlaskApp.route('/Hello/<name>')
def HelloIndividual(name):
    return ('Hello, ' + str(name))
