from PIL import Image, ImageDraw
import textwrap
from io import BytesIO
import requests


def tweet_pics(all_tweets)

	tweet_num = 1
	for tweet in all_tweets:

		img = Image.new('RGB', (1280, 720), color = white)
	 	d = ImageDraw.Draw(img)

		wrapped_tweet = textwrap.wrap(tweet.text, width=10)

	    i = 0
	    for line in wrapped_tweet:
		    d.text((320, 200 + i), line.encode('cp1252', 'ignore'), fill = black)
		    i = i + 15

	    if 'media' in tweet.entities:
	        img_url = tweet.entities["media"][0]["media_url"]
	        response = requests.get(img_url)
	        tweet_img = Image.open(BytesIO(response.content))
	        tweet_img.thumbnail((320, 200))
        	img.paste(tweet_image, (0, 0))

	    img_name = "tweet_pic_" + tweet_num + ".png"
	    img.save(img_name)

	    tweetnum = tweetnum + 1



	    
