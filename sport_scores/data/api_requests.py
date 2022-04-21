
import requests


def get_scores():
    r=requests.get("http://api.football-data.org/v2/competitions/2021/matches", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"},params={"dateFrom":"2022-04-20","dateTo":"2022-04-20"}).json()
    res=r['matches']
    for match in res:
        hometeam = match['homeTeam']['name']
        awayteam = match['awayTeam']['name']
        homescore = match['score']['fullTime']['homeTeam']
        awayscore = match['score']['fullTime']['awayTeam']
        print("home team " + hometeam +" ")
        print(homescore)
        print("away team " + awayteam +" ")
        print(awayscore)
        print("......")
    return res    
