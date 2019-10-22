import requests
import json




header = {
    "Ocp-Apim-Subscription-Key": "20f359230eb94a8c8b607aaf1e91e990"
}

# x=requests.request("GET","https://api.sportsdata.io/v3/nba/stats/json/AllStars/2019",headers=header)
# print(x.content)

Sentence = input("Hello! Please input what you want to know about the current basketball season")

if (Sentence.lower()=="what season is this?"):
    temp=requests.request("GET","https://api.sportsdata.io/v3/nba/stats/json/CurrentSeason",headers=header).content
    temp=json.loads(temp)
    print("The current season is the "+str(temp["Season"])+" season, which started in "+str(temp["StartYear"])+" and will span the "+str(temp["Description"])+" time span")
elif(Sentence.lower()=="i want to get some information about a player"):
    playerId=input("Please type the id of the player you want to get information about")
    temp=requests.request("GET","https://api.sportsdata.io/v3/nba/scores/json/Player/"+str(playerId),headers=header).content
    print(temp)
elif(Sentence.lower()=="is there any game now?"):
    temp=requests.request("GET","https://api.sportsdata.io/v3/nba/scores/json/AreAnyGamesInProgress",headers=header).content
    temp=json.loads(temp)
    if(temp==False):
        print("No, there is no game being played right now in the nba")
    else:
        print("Yes, there is a game being played right now in the nba!")