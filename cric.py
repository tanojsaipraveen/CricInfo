from pynotifier import Notification
import requests
import time

oldscore = 0;
baseURL = 'https://cricket-api.vercel.app/cri.php?url='
Enterurl = input("Enter live match URL from Cricbuzz : ")
while True:
    time.sleep(10)
    
    #https://www.cricbuzz.com/live-cricket-scores/38442/rsa-vs-ban-1st-test-bangladesh-tour-of-south-africa-2022
    resp = requests.get(url=baseURL+Enterurl)
    data = resp.json()

    teamone = data['livescore']['teamone']
    teamtwo = data['livescore']['teamtwo']

    title = data['livescore']['title']
    score = data['livescore']['current']
    batsman = data['livescore']['batsman']
    batsman2 = data['livescore']['batsmantwo']
    batsmanruns = data['livescore']['batsmanrun']
    batsman2runs = data['livescore']['batsmantworun']
    recentballs = data['livescore']['recentballs']
    
    if(score != oldscore):
        Notification(
        title=title,
        description=str(score+"\n"+batsman +"   "+ batsmanruns +"\n"+batsman2 +"   "+ batsman2runs+"\n"+recentballs),
        duration=10).send()
    
    oldscore = score
