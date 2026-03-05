
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Universe!</p>"


@app.route("/customercase")
def customers():
    return "<p>Please reach out to customercase : +91-9644343434!</p>"


app.run()