# script to collect tweets using Tweepy
import tweepy
from tweepy import StreamListener
from arabic import settings
import time
import json
import sys
from arabictweets.models import TwitterText
import pandas as pd
import django.core.exceptions as djangoerr
import schedule

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth)

def tweet_insert(tweet):
    # take a captured tweet and insert it into the database
    try:
       print (tweet['text'])
       atweet = TwitterText(tweet_text=tweet['text'],tweet_datetime=tweet['created_at'], tweet_id=tweet['id_str'],tweet_lang=tweet['lang'],tweet_source=tweet['source'],tweet_user_username=tweet['user']['screen_name'],tweet_user_id=tweet['user']['id_str'],tweet_user_name=tweet['user']['name'] if tweet['user']['name'] is not None else "",tweet_user_location=tweet['user']['location'] if tweet['user']['location'] is not None else "",tweet_user_timezone=tweet['user']['time_zone'] if tweet['user']['time_zone'] else "", tweet_user_lang=tweet['user']['lang'] if tweet['user']['lang'] else "",tweet_coordinates_langitude=tweet['coordinates']['coordinates'][1] if tweet['coordinates'] is not None else "",tweet_coordinates_longitude=tweet['coordinates']['coordinates'][0] if tweet['coordinates'] is not None else "",tweet_place_country=tweet['place']['country'] if tweet['place'] is not None else "", tweet_place_city=tweet['place']['name'] if tweet['place'] is not None else "")
       atweet.save()
    except Exception as e:
        print("Error in inserting tweet. error message:", e)
    return

class TwitterListener(StreamListener):

    def __init__(self, api=None, fprefix = 'streamer'):
        super(StreamListener, self).__init__()
        self.api = api or tweepy.API()
        self.counter = 0
        self.time = time.time()
        return

    def on_data(self, data):
        self.counter += 1
        try:
            tweet = json.loads(data)  # convert twitter stream in json into Python dictionary
            if isinstance(tweet, dict):
                tweet_insert(tweet)
                print("tweets count: {}".format(self.counter))
        except Exception as e:
            print("Error in Twitter listener. Error message:", e)
        
        return

    def on_limit(self, track):
        print(">> limit")
        return

    def on_error(self, status_code):
        print(">>> error: ", str(status_code) + "\n")
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return True
        return

    def on_disconnect(self, notice):
        print (">> disconnecting")
        return False

    def on_timeout(self):
        print(">>> timed out ...\n")
        return False

def run_tweeter_listening():
    try:
        #time.sleep(30)
        listener = TwitterListener(api, "test")
        stream = tweepy.Stream(auth, listener)
        print("Begin Twitter streaming")
        stream.filter(track=['#'], languages=["ar"], is_async=True)
    except:
        print(sys.exc_info())

def stop_tweeter_listening():
    print("stop")

def run():

    try:#schedule.every(settings.tweets_polling_time).seconds.do(stop_tweeter_listening)
        #schedule.every(settings.tweets_polling_time).seconds.do(run_tweeter_listening)
        run_tweeter_listening()
        #while True:
        #    schedule.run_pending()
         #   time.sleep(1)
    except Exception as e:
        print("Error ",e)
