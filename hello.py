from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
from datetime import datetime

@app.route('/') # specifies URL path/endpoint that triggers this function
def index(): # function that runs when the endpoint is accessed
    return render_template('index.html') # returns HTML content in a Jinja2 template

@app.route('/user/<name>') # dynamic route with variable component
def user(name):
    # Day suffix logic
    dt = datetime.now()
    day = dt.day
    if 11 <= day <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    
    # Format: Weekday, Month DaySuffix, Year Hour:Minute am/pm
    dt_now = dt.strftime(f"%A, %B {day}{suffix}, %Y %#I:%M %p")
    return render_template('user.html', name=name, now=dt_now, timestamp = dt.timestamp())