from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def location_page():
    return f"{request.environ.get('X-Forwarded-For')}"
