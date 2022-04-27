import requests
import json
from datetime import datetime

r=requests.get("http://api.football-data.org/v2/competitions/2021/matches", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"}).json()
prem=r
#with open('matches_prem.json', 'w') as outfile:
#    json.dump(r, outfile)

r=requests.get("http://api.football-data.org/v2/competitions/2016/matches", headers={"X-Auth-Token":"769b4f8fdad94b5a9441ab475cdd1a8d"}).json()
#with open('matches_champ.json', 'w') as outfile:
#    json.dump(r, outfile)
championship=r
data= {'competitions': {"premiership":prem, "championship":championship }}
with open('matches_v2.json', 'w') as outfile:
       json.dump(data, outfile)
date=datetime.now()
date_srt=date.isoformat()
print(date_srt)
ts={"dateLoaded":date_srt}
with open('matches_ts.json', 'w') as outfile:
    json.dump(ts, outfile)    