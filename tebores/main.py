# -*- coding: utf-8 -*-

from bots import desktopbot
from files import auth


def main():
	bot = desktopbot.DesktopBot()
	bot.sign_in(auth.user, auth.password)
	print "\n We are in"
	bot.tweet("Hello world!")
	#bot.sign_out()
	#print " We are out"

if __name__ == '__main__':
	main()