import time

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def helloWorld():
    return "Hello, cross-origin-world!"


@app.route("/time")
def get_current_time():
    return jsonify({"time": time.time()})
