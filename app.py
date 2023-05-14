"""Module flask used for creating a web server"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    """Index route for the web app"""
    return '<h1>Hello WSB! Greetings from Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
