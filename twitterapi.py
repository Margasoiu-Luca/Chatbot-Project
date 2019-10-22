import tweepy as tw
import pandas as pd

consumer_key = 'ZffjpjC6IM16Xq8QwQsxwxcx0'
consumer_secret = '0oSlqVbhD18KeJe0ngUHSHTYCIklLe07EgozJcheu4Fksa7PbD'
access_token = '1186363285148459008-p6Q3NpdMF1Nf9k9Dr64AGMKZOzOEUf'
access_token_secret = 'MpLHeLfgcDsMy5mrezgel4M5MZiNADXC1s6Ar2X6H7fhW'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

hashtag = "#NBA"
date = "2019-10-22"
tweets = tw.Cursor(api.search,q=hashtag,lang="en",since=date).items(5)
for tweet in tweets:
    print(tweet.text)
    