from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

TOKEN = os.getenv("API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/player/<tag>")
def player(tag):

    tag = tag.upper().replace("#", "")
    encoded_tag = "%23" + tag

    url = f"https://api.brawlstars.com/v1/players/{encoded_tag}"

    response = requests.get(url, headers=HEADERS)

    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)