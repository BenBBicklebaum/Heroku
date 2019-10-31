#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
import sys
import openweathermapy.core as owm
import os
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")



# In[5]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# Create a function that gets the weather in London and Tweets it
def WeatherTweet(tweet):

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    settings = {"units": "imperial", "appid": weather_api_key}
    # Perform the API call to get the weather
    washington = owm.get_current(city, **settings)
    washingtonweather = washington["main"]["temp"]
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    currenttime = datetime.datetime.now().strftime("%I:%M %p")
    api.update_status(f"The weather in DC RIGHT NOW is {washingtonweather}F timestamp: {currenttime}")

    # Print success message
    print("This was successful")


# In[ ]:


# Set timer to run every 1 hour
# Create a loop that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    WeatherTweet(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(3600)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1


# In[34]:





# In[ ]:




