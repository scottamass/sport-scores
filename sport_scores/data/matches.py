
import requests
from datetime import date
import json



def get_ts():
    with open("matches_ts.json","r") as read_file:
        data=json.load(read_file)

        ts=data['dateLoaded']
        return ts    

 

def get_match_data():
    with open("matches_v2.json", "r") as read_file:
        data = json.load(read_file)

        match_data =data['competitions']
        
        return match_data   



def get_scores():
    
    todays_date = date.today()
    strng= todays_date.strftime('%Y-%m-%d')
    g=get_match_data()
    prem_games =[]
    for m in g['premiership']['matches']:
        prem_games.append(m)
    champ_games =[]
    for m in g['championship']['matches']:
        champ_games.append(m)    
    
    games = {'prem':prem_games ,'champ':champ_games}
    all_games ={'pgames':[],'cgames':[]}
    for match in games['prem']:
        if match['utcDate'][0:10] == strng:
            
            all_games['pgames'].append(match)  
    for match in games['champ']:
        if match['utcDate'][0:10] == strng:
            
            all_games['cgames'].append(match)
    
    
    return all_games    

def date_scores(matchdate):
    

      
    
    g=get_match_data()
    prem_games =[]
    for m in g['premiership']['matches']:
        prem_games.append(m)
    champ_games =[]
    for m in g['championship']['matches']:
        champ_games.append(m)    
    
    games = {'prem':prem_games ,'champ':champ_games}
    all_games ={'pgames':[],'cgames':[]}
    for match in games['prem']:
        if match['utcDate'][0:10] == matchdate:
            
            all_games['pgames'].append(match)  
    for match in games['champ']:
        if match['utcDate'][0:10] == matchdate:
            
            all_games['cgames'].append(match)
    
   
    return all_games    
            
