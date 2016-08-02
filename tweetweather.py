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
import socket
# Consumer keys and access tokens, used for OAuth
from settings import *

# Create UDP socket to listen for messages from arduino script
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 10000)

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

 
while True:
    data, address = sock.recvfrom(8888)
    
    print data
    
#	if len(tweet_text) <= 140:
#    	api.update_status(status=tweet_text)
#	else:
#    	print "tweet not sent. Too long. 140 chars Max."

