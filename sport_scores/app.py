from flask import Flask, render_template
from sport_scores.data.matches import get_scores,date_scores
from datetime import date, timedelta , datetime as dt

from sport_scores.data.standings import get_standings

app = Flask(__name__)
@app.context_processor
def show_year():


    year = date.today().strftime('%Y')
    return dict(year=year)

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
    teams=get_standings()
    return render_template('standings.html', teams=teams) 