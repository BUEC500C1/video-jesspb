import tweepy
from datetime import datetime, timedelta


class Twitter():

 	auth = tw.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tw.API(auth, wait_on_rate_limit=True)

	def get_tweets(username): 

	        # 200 tweets to be extracted 
	        number_of_tweets=200
	        tweets = api.user_timeline(
	        	screen_name=username,
	        	count=25,
	            exclude_replies=True,
	            include_rts=1) 
	  
	        # Empty Array 
	        user_tweets=[]  

	        curr_date = datetime.now

	        for tweet in timeline:
	                # check if tweet was within the last 24 hours
	                if curr_date - timedelta(hours=24) <= tweet.created_at <= today:
	                    user_tweets.append(tweet)

	            return user_tweets
	  

