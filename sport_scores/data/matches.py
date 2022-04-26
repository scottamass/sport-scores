
import requests
from datetime import date
import json

with open("matches.json", "r") as read_file:
    data = json.load(read_file)

match_data =data['matches']   

def get_match_data():
    with open("matches.json", "r") as read_file:
        data = json.load(read_file)

        match_data =data['matches'] 
        return match_data   
print(get_match_data())


def get_scores():
    
    todays_date = date.today()
    strng= todays_date.strftime('%Y-%m-%d')
    print(strng)
    games =[]
    for match in get_match_data():
        if match['utcDate'][0:10] == strng:
            print(match['id'])
            games.append(match)  
    return games    

def date_scores(matchdate):
    

      
    
    
    games =[]
    for match in get_match_data():
        if match['utcDate'][0:10] == matchdate:
            print(match['id'])
            games.append(match)  
    return games    