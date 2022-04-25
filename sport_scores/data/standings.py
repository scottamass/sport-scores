

import requests


def get_standings():
    r=requests.get("http://api.football-data.org/v2/competitions/2021/standings", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"}).json()

    standings=r['standings'][0]['table']


    teams=[]
    for team in standings:
        teams.append(team)   
    return teams     

    





