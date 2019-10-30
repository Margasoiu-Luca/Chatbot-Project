#imports
import tweepy as tw
import pandas as pd
import datetime

#api keys and tokens
consumer_key = 'ZffjpjC6IM16Xq8QwQsxwxcx0'
consumer_secret = '0oSlqVbhD18KeJe0ngUHSHTYCIklLe07EgozJcheu4Fksa7PbD'
access_token = '1186363285148459008-p6Q3NpdMF1Nf9k9Dr64AGMKZOzOEUf'
access_token_secret = 'MpLHeLfgcDsMy5mrezgel4M5MZiNADXC1s6Ar2X6H7fhW'

#authorisation and accesing the api
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#searching using the api
hashtag = "#NBA"
date = datetime.date.today()
tweets = tw.Cursor(api.search,q=hashtag,lang="en",since=date).items(5)
for tweet in tweets:
    print(tweet.text)
    users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]   
tweet_text = pd.DataFrame(data=users_locs, 
                    columns=['user', "location"])
