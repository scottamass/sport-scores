

import requests
import json


def get_standings():
   with open("json_data.json", "r") as read_file:
    data = json.load(read_file)

    standings=data['standings'][0]['table']


    teams=[]
    for team in standings:
        teams.append(team)   
    return teams     

    






