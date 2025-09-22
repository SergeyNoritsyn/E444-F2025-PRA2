from flask import Flask
app = Flask(__name__)

@app.route('/') # specifies URL path/endpoint that triggers this function
def index(): # function that runs when the endpoint is accessed
    return '<h1>Hello World!</h1>' # returns HTML content/response