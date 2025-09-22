from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
from datetime import datetime, timezone
from flask_moment import Moment
moment = Moment(app)


@app.route('/') # specifies URL path/endpoint that triggers this function
def index(): # function that runs when the endpoint is accessed
    return render_template('index.html') # returns HTML content in a Jinja2 template

@app.route('/user/<name>') # dynamic route with variable component
def user(name):
    return render_template('user.html', name=name, current_time=datetime.now(timezone.utc))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500