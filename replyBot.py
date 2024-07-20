import tweepy
import random
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Authentication 
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# API instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Target keywords 
keywords = ['smallbiz', 'shoplocal', 'smbiz'] 

# Message list
messages = [
    "Thanks for the mention! As a designer for SMBs, I can help with a custom site.",  
    "I'd be happy to discuss building an affordable website to highlight your products & services!",
    "Saw your tweet - let's talk about crafting a modern, responsive site designed to boost leads for your biz!"
]

# URL list
urls = [
    "https://www.mybizsites.com/pricing",
    "https://www.mybizsites.com/samples",
    "https://www.mybizsites.com/contact" 
]

# Get random auto reply  
def get_reply():
    message = random.choice(messages)
    url = random.choice(urls)
    
    reply = f"{message} {url}"
    print(reply)
    return reply

# Auto reply function
def auto_reply(tweet):
    reply = get_reply() 
    full_text = f"@{tweet.user.screen_name} {reply}"
    
    api.update_status(full_text, 
                      in_reply_to_status_id=tweet.id, 
                      auto_populate_reply_metadata=True)
