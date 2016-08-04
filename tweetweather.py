#!/usr/bin/env python2.7

# working from standard yocto build on Edison
# make sure pip is upto date on edison
# sudo pip install --upgrade pip

# download and setup tweepy in root
# pip install tweepy
# (note tweepy at https://github.com/tweepy/tweepy)

# D Wilson June 2016 (original work 2014)


import tweepy
import sys
# Consumer keys and access tokens, used for OAuth
from settings import *

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

    
if len(sys.argv) >= 2:
	tweet_text = sys.argv[1]

else:
	with open("/home/root/climdata.txt", "r") as f:
		tweet_text = f.read()
		print (" Message from Arduino: " + tweet_text)

if len(tweet_text) <= 140:
    api.update_status(status=tweet_text)
else:
    print "tweet not sent. Too long. 140 chars Max."

