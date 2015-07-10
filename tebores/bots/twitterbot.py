import os
from tweepy import OAuthHandler, API

class TwitterBot(object):
    """Twitter bot"""
    ACCESS_TOKEN = os.environ['TWI_AC_TOKEN']
    ACCESS_SECRET = os.environ['TWI_AC_SECRET']
    CONSUMER_KEY = os.environ['TWI_CO_KEY']
    CONSUMER_SECRET = os.environ['TWI_CO_SECRET']

    def sign_in(self):
        auth = OAuthHandler(TwitterBot.CONSUMER_KEY, TwitterBot.CONSUMER_SECRET)
        auth.set_access_token(TwitterBot.ACCESS_TOKEN, TwitterBot.ACCESS_SECRET)
        self.api = API(auth)

    def tweet(self, text):
        self.api.update_status(text)

    def sign_out(self):
        TwitterBot.CONSUMER_KEY, TwitterBot.CONSUMER_SECRET = (None,) * 2
        TwitterBot.ACCESS_TOKEN, TwitterBot.ACCESS_SECRET = (None,) * 2
        
    
