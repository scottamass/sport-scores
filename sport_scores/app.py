from flask import Flask, render_template
from sport_scores.data.api_requests import get_scores,date_scores
from datetime import date, timedelta , datetime as dt

app = Flask(__name__)

@app.route("/")
def index():
    todays_date = date.today()
    tomorrow= todays_date + timedelta(days=1)
    yesterday= todays_date - timedelta(days=1)
    out=get_scores()
    return render_template('index.html', matches=out, day=todays_date, tomorrow=tomorrow, yesterday=yesterday )

@app.route("/date/<date>")
def selectday(date):
    out=date_scores(date)
    date_str=date
    date_obj = dt.strptime(date_str, '%Y-%m-%d')
    tomorrow= date_obj.date() + timedelta(days=1)
    yesterday= date_obj.date() - timedelta(days=1)

    return render_template('index.html', matches=out,day=date, tomorrow=tomorrow, yesterday=yesterday)    


@app.route("/standings")
def standings():
    return 