# Python for network programming/web design.

## Set up your environment

So here's a quick rundown on how to use Python Flask; as well as  
a crash course on how to use a virtual environment  

First we need pip, and venv so in your terminal execute:  

> sudo apt-get install python3-pip python3-venv

Once download, navigate to the folder containing your Flask project,  
and execute:

> python3 -m venv ./MyFlaskProject

Upon completion you will find a /bin directory within the project:  
this is a virtual environment; and it's how we package our dependencies  
along with our software packages.

To activate the environment simply:

> source bin/activate


Now, you can use pip to install Python modules, in a single location
separate from the main server-space. We need to download Flask, so:

> pip install flask

----------------------------------------------------------------------

## Create your application

Bare-minimum, flask only needs about 5 lines to get off the ground.

> from flask import Flask  
> app = Flask(__name__)  
> @app.route("/")  
> def hello_world():  
>> return str("Hello, World!")

With these lines saved to a .py file the next step is to alter the shell  
variable $FLASK_APP to point to the file; and then run flask.

> export FLASK_APP=/path/to/FlaskApp.py
> flask run

Note that a naked flask run will ONLY be accessible from the localhost.  
To get the server running publicly you have to alter the flask run command like:

> flask run host='192.168.1.1'

