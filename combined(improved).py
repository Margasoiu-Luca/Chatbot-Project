import tweepy as tw
import pandas as pd
import requests
import json
import sqlite3
import os
import datetime
#from googleapiclient.discovery import build



#Check to see if the database files do not exist
if os.path.isfile('userinfo.db') is False:
    #Creates the staff login database 
    userinfo_db = sqlite3.connect('userinfo.db')  #Creates a connection to the database file
    cursor = userinfo_db.cursor()                    #Cursor object is called up using this variable
    cursor.execute('''                   
    CREATE TABLE IF NOT EXISTS logindetails(
    userID INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL);
    ''')                                                #Creates the table if it does not exist in the database    

    cursor.execute('''                   
    CREATE TABLE IF NOT EXISTS extrainfo(
    ID INTEGER PRIMARY KEY,
    twitter TEXT NOT NULL, 
    favteam TEXT NOT NULL,
    favplayer TEXT NOT NULL,
    FOREIGN KEY(ID) REFERENCES logindetails(userID));
    ''')
    
    userinfo_db.commit()                                #Commits the statements, which saves changes made
    userinfo_db.close()                                 #Closes the database  

def start():
    login = 0
    user_info_db = sqlite3.connect('userinfo.db')
    cursor = user_info_db.cursor()
    startup = input("are you a new user?  (y/n): ")
    if startup == 'y':
        newusername = input('Please enter a new username: ')
        newpassword = input('Please enter a new password: ')
        newfirstname = input('Please enter a new first name: ')
        newlastname = input('Please enter a new last name: ')
        TwitterHandle = input('Please enter your Twitter Handle: ')
        FavTeam = input('Please enter your favourite team: ')
        FavPlayer = input('Please enter your favourite player: ')
        if len(newusername) == False or len(newpassword)== False or len(newfirstname)== False or len(newlastname)== False or len(TwitterHandle)== False or len(FavTeam)== False or len(FavPlayer)== False:
            print("Please fill in all boxes. Start Again.")
            start()
        else:
            if newfirstname.isalpha() is False or newlastname.isalpha() is False:    
                print("First Name and Last Name must be characters. Start Again")
                start()
            else:
                #Checks to see if user input matches data in database  
                cursor.execute(('SELECT username FROM logindetails WHERE username=?'),[newusername])
                exists=cursor.fetchone()  
                if exists:
                    print("Username already exists. Start Again.")
                else:
                    cursor.execute('''INSERT INTO logindetails(username,password,firstname,lastname)
                                   VALUES(?,?,?,?)''',[newusername,newpassword,newfirstname,newlastname])
                    cursor.execute('''INSERT INTO extrainfo(twitter,favteam,favplayer)
                                   VALUES(?,?,?)''',[TwitterHandle,FavTeam,FavPlayer])
                    user_info_db.commit()
                    print("New User Created")
                    print("Welcome",newfirstname,newlastname)
                    print("Your favourite team is:",FavTeam)
                    print("Your favourite player is:",FavPlayer)
                    cursor.execute(('SELECT userID FROM logindetails WHERE username=?'),[newusername])
                    log=cursor.fetchone()
                    login = log
                    print("userid",login)
        
                
    elif startup == 'n':
        print("Please Log In!")
        username = input("Username: ")
        password = input("Password: ")
        user_info_db = sqlite3.connect('userinfo.db')
        cursor = user_info_db.cursor()
        cursor.execute(('SELECT * FROM logindetails WHERE username = ? AND password = ?'),[username,password]) 
        verify=cursor.fetchall()
        if verify:
            for i in verify:
                name = (i[3],i[4])
                print("Welcome",name)
                cursor.execute(('SELECT userID FROM logindetails WHERE username=?'),[username])
                log=cursor.fetchone()
                login = log
                print("userid",login)
                
                
                
        else:
            print('Denied')
    else:
        print('That input is not recognised')
        start()
start()

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



consumer_key = 'ZffjpjC6IM16Xq8QwQsxwxcx0'
consumer_secret = '0oSlqVbhD18KeJe0ngUHSHTYCIklLe07EgozJcheu4Fksa7PbD'
access_token = '1186363285148459008-p6Q3NpdMF1Nf9k9Dr64AGMKZOzOEUf'
access_token_secret = 'MpLHeLfgcDsMy5mrezgel4M5MZiNADXC1s6Ar2X6H7fhW'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#from start import Favplayer
team_info = sqlite3.connect('userinfo.db')
cursor = team_info.cursor()
user = input("What is your username? ")
cursor.execute(('SELECT favteam FROM logindetails WHERE username=?'),[user])
check=cursor.fetchone()
#print(check[0])
hashtag = '#' + '{}'.format(check[0])
date = datetime.date.today()
tweets = tw.Cursor(api.search,q=hashtag,lang="en",since=date).items(5)
for tweet in tweets:
    print(tweet.text)
    users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]   
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
answer = input('would you like me to tweet these at you?(y/n) ')
if answer == 'y':
    api.update_status(tweet.text)
    



