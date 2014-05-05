# -*- coding: utf-8 -*-

import sys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

class DesktopBot(object):
	"""DesktopBot """
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
	new_tweet_button_div_class = "tweet-button"
	new_tweet_send_button_class = "btn primary-btn tweet-action tweet-btn js-tweet-btn"

	def __init__(self):
		self.firefox = webdriver.Firefox()
		self.firefox.get(DesktopBot.login_url)

	def sign_in(self, username, password):
		try:
			self.firefox.find_element_by_id(DesktopBot.login_input_username).send_keys(username)
			input_pass = self.firefox.find_element_by_id(DesktopBot.login_input_password)
			input_pass.send_keys(password)
			input_pass.submit()
		except NoSuchElementException, e:
			print "Exception %s" % e.args[0]

	def sign_out(self):
		try:
			self.firefox.find_element_by_id(DesktopBot.logout_button_settings).click()
			self.firefox.find_element_by_id(DesktopBot.logout_button).submit()
			self.firefox.quit()
		except NoSuchElementException, e:
			print "Exception %s" % e.args[0]

	def tweet(self, text):
		try:
			'''
			self.firefox.find_element_by_id(DesktopBot.new_tweet_button).click()
			self.firefox.find_element_by_id(DesktopBot.new_tweet_text_box).send_keys(text)
			sleep(10)
			print " Finished waiting"
			self.firefox.find_element_by_id('global-tweet-dialog-dialog').find_element_by_tag_name('button').click()
			#self.firefox.find_element_by_class_name(DesktopBot.new_tweet_send_button_class)[0].click()
			'''
			self.firefox.find_element_by_id('tweet-box-mini-home-profile').send_keys(text)
			self.firefox.find_element_by_id('tweet-box-mini-home-profile').find_element_by_tag_name('button').click()
			
		except NoSuchElementException:
			print "Exception"
