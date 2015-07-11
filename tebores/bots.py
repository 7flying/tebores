# -*- coding: utf-8 -*-

import os
from time import sleep
from tweepy import OAuthHandler, API
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class DesktopBot(object):
	"""Bot to operate in Twitter using selenium. """
	# Url for login
	login_url = "https://twitter.com/"
	# Inputs to sign in
	login_input_username = "signin-email"
	login_input_password = "signin-password"
	# Buttons to sign out
	logout_button_settings = "user-dropdown-toggle"
	logout_button = "signout-form"
	# Tweeting
	new_tweet_button = "global-new-tweet-button"
	new_tweet_text_box = "tweet-box-global"
    
	def __init__(self):
		self.firefox = webdriver.Firefox()
		self.firefox.get(DesktopBot.login_url)
		
	def sign_in(self, username, password):
		try:
			self.firefox.find_element_by_id(DesktopBot.login_input_username)\
              .send_keys(username)
			input_pass = self.firefox.find_element_by_id(
                DesktopBot.login_input_password)
			input_pass.send_keys(password)
			input_pass.submit()
		except NoSuchElementException, e:
			print "Exception %s" % e.args[0]

	def sign_out(self):
		try:
			self.firefox.find_element_by_id(DesktopBot.logout_button_settings)\
              .click()
			self.firefox.find_element_by_id(DesktopBot.logout_button).submit()
			self.firefox.quit()
		except NoSuchElementException, e:
			print "Exception %s" % e.args[0]

	def tweet(self, text):
		self.firefox.find_element_by_id(DesktopBot.new_tweet_button).click()
		self.firefox.find_element_by_id(DesktopBot.new_tweet_text_box)\
          .send_keys(text)
		self.firefox.find_element_by_id(DesktopBot.new_tweet_text_box)\
          .send_keys(Keys.CONTROL, Keys.RETURN)
		sleep(1)
        

class TwitterAPIBot(object):
    """Bot to operate in Twitter using the API"""
    ACCESS_TOKEN = os.environ['TWI_AC_TOKEN']
    ACCESS_SECRET = os.environ['TWI_AC_SECRET']
    CONSUMER_KEY = os.environ['TWI_CO_KEY']
    CONSUMER_SECRET = os.environ['TWI_CO_SECRET']

    def sign_in(self):
        auth = OAuthHandler(TwitterAPIBot.CONSUMER_KEY,
                            TwitterAPIBot.CONSUMER_SECRET)
        auth.set_access_token(TwitterAPIBot.ACCESS_TOKEN,
                              TwitterAPIBot.ACCESS_SECRET)
        self.api = API(auth)

    def tweet(self, text):
        print "[ bot ] Tweeting:", text
        #self.api.update_status(status=text)

    def sign_out(self):
        TwitterAPIBot.CONSUMER_KEY, TwitterAPIBot.CONSUMER_SECRET = (None,) * 2
        TwitterAPIBot.ACCESS_TOKEN, TwitterAPIBot.ACCESS_SECRET = (None,) * 2
        
    
