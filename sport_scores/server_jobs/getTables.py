import requests
import json

r=requests.get("http://api.football-data.org/v2/competitions/2021/standings", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"}).json()

with open('standings.json', 'w') as outfile:
    json.dump(r, outfile)
