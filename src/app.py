from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/")
def location_page():
    print(request.__dict__)
    return jsonify(f"{request.__dict__}")
