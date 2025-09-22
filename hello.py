from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/') # specifies URL path/endpoint that triggers this function
def index(): # function that runs when the endpoint is accessed
    return render_template('index.html') # returns HTML content in a Jinja2 template

@app.route('/user/<name>') # dynamic route with variable component
def user(name):
    return render_template('user.html', name=name)