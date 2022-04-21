from flask import Flask, render_template
from sport_scores.data.api_requests import get_scores

app = Flask(__name__)

@app.route("/")
def index():
    out=get_scores()
    return render_template('index.html', out=out)