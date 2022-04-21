
import requests
from datetime import date


def get_scores():
    todays_date = date.today()
    
    r=requests.get("http://api.football-data.org/v2/competitions/2021/matches", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"},params={"dateFrom":todays_date,"dateTo":todays_date}).json()
    res=r['matches']
    
    return res 
       
def date_scores(date):
    r=requests.get("http://api.football-data.org/v2/competitions/2021/matches", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"},params={"dateFrom":date,"dateTo":date}).json()
    res=r['matches']
    return res