import tweepy
from textblob import textblob
consumer_key='yV5Ko8K2reU2jEBfT3hFw5RUU'
consumer_secret='rR2AKzz8L1xoMSjXrIEC2Ocj7BiBVKp5pGTO4OdoGOSyq9ZUbG'
access_token='931882347087065088-M6Pcy2iFnX6vTTREkKX45comCsXGJc2'
access_token_secret='D4haUjTzQDXe00YjOnslYx2fwBmNNJw42U4iVBLDrNb6G'
auth=tweepy.OAuthHandler(consumer_key,connsumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
public_tweets=api.search('Elon Musk')
for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis)