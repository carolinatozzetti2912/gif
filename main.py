import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

GIPHY_API_KEY = os.getenv("KGTQVKdhFMubeQiLOT9Jkw38cnvkMcB2")
GIPHY_API_URL = "https://api.giphy.com/v1/gifs/search"

@app.route("/", methods=["GET", "POST"])
def index():
    gifs = []
    if request.method == "POST":
        query = request.form["query"]
        response = requests.get(
            GIPHY_API_URL,
            params={"api_key":"KGTQVKdhFMubeQiLOT9Jkw38cnvkMcB2", "q": query, "limit": 5},
        )
        gifs = response.json().get("data", [])
    return render_template("index.html", gifs=gifs)

if __name__ == "__main__":
    app.run(debug=True)
