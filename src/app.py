import requests
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def location_page():
    ip = request.environ.get('HTTP_X_FORWARDED_FOR')
    location = requests.get(f"http://ipwhois.app/json/{ip}").json()
    return render_template(
        "index.html",
        longitude=location["longitude"],
        latitude=location["latitude"],
    )
