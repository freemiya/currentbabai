# -*- coding: utf-8 -*-
"""
 Install tweepy
"""

"""## Import modules

tweepy for accessing twitter. csv to write down in tabular format.
"""

import tweepy
import csv
import sys
import time

#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""



"""## Function to get Tweets"""

def get_all_tweets(screen_name,recent_tweetid=-1):
  #Twitter only allows access to a users most recent 3240 tweets with this method



  #authorize twitter, initialize tweepy
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  api = tweepy.API(auth)

  #initialize a list to hold all the tweepy Tweets
  alltweets = []

  #make initial request for most recent tweets (200 is the maximum allowed count)
  new_tweets = api.user_timeline(screen_name = screen_name,count=1) # Get latest #'count' tweets

  #save most recent tweets
  alltweets.extend(new_tweets)
  tweet = alltweets[-1] # Store it for recent tweetid and testing purposes

  print("recent tweet id is {}".format(tweet.id))

  print(tweet.id_str, str(tweet.created_at), str(tweet.text),str(tweet.favorite_count),str(tweet.retweet_count), str(len(tweet.entities.get('media',[]))))

  #save the id of the oldest tweet less one
  if  recent_tweetid == -1: recent_tweetid = alltweets[-1].id
  else : pass

  #keep grabbing tweets until there are no tweets left to grab
  while True:
    print ("getting tweets before after".format(recent_tweetid))

    #all subsequent requests use the max_id param to prevent duplicates
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,since_id=recent_tweetid)

    '''
    "since_id"	optional	Returns results with an ID greater than (that is, more recent than) the specified ID. There are limits to the number of Tweets that can be accessed through the API. If the limit of Tweets has occured since the since_id, the since_id will be forced to the oldest ID available.		12345
    "count"	    optional	Specifies the number of Tweets to try and retrieve, up to a maximum of 200 per distinct request. The value of count is best thought of as a limit to the number of Tweets to return because suspended or deleted content is removed after the count has been applied. We include retweets in the count, even if include_rts is not supplied. It is recommended you always send include_rts=1 when using this API method.
    "max_id"	optional	Returns results with an ID less than (that is, older than) or equal to the specified ID.
    '''
    #save most recent tweets
    alltweets.extend(new_tweets)

    #update the id of the oldest tweet less one
    recent_tweetid = alltweets[-1].id

    print ("...%s tweets downloaded so far" % (len(alltweets)))


    outtweets = [[tweet.id_str, str(tweet.created_at), str(tweet.text),str(tweet.favorite_count),str(tweet.retweet_count), str(len(tweet.entities.get('media',[]))) ] for tweet in alltweets]
    tweetmedia = [[tweet.id_str, str(tweet.created_at), str(tweet.text), str(len(tweet.entities.get('media',[]))), tweet.entities['media'][0]['media_url'] if tweet.entities.get('media',-1)!= -1 else "None" ] for tweet in alltweets]
    #write the csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text","# Media"," Media Url"])
        writer.writerows(tweetmedia)

    time.sleep(20)

if __name__ == '__main__':
        #pass in the username of the account you want to download
        get_all_tweets("NammaBESCOM",recent_tweetid=-1)


import pandas as pd

df = pd.read_csv("NammaBESCOM_tweets.csv")
print(df.head())
