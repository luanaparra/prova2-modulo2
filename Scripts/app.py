from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()