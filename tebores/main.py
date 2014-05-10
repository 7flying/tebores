# -*- coding: utf-8 -*-

import threading
import Queue
from time import sleep

from bots import desktopbot
from files import auth
from crawler import bookcrawler
from manager import dbmanager

new_books = Queue.Queue() # Holds a tuple of (BookName-url)
manager = dbmanager.DBManager("tebores_db.sqlite")

to_mark = [] # Books to mark as tweeted
to_mark_lock = threading.Condition() 

def producer_():
	crawlers = []
	crawlers.append(bookcrawler.ITebooksCrawler())
	crawlers.append(bookcrawler.FreeCBCrawler())
	while True:
		for crawler in crawlers:
			books = crawler.get_books()
			for book in books.keys():
				sleep(60)
				if is_new_book(book):
					# url of web page, book name, book url
					insert_book(crawler.get_url(), books[book], book)
					print "New book: %s" % (books[book] + " - " + crawler.get_url() + book)
					new_books.put( (books[book], crawler.get_url() + book))
					with to_mark_lock:
						while not to_mark:
							to_mark_lock.wait()
						mark = to_mark.pop(0)
						mark_tweeted(mark)

			sleep(1)


def consumer_():
	bot = desktopbot.DesktopBot()
	bot.sign_in(auth.user, auth.password)
	while True:
		book = new_books.get()
		bot.tweet(book[0] + " " + book[1])
		print "Tweet: %s" % (book[0] + " " + book[1])
		with to_mark_lock:
			to_mark.append(book[1])
			to_mark_lock.notify()
	
		sleep(1)


def is_new_book(book_url):
	return manager.is_new_book(book_url)

def insert_book(book_web_url, book_name, bool_url):
	manager.insert_book(book_web_url, book_name, bool_url)

def mark_tweeted(book_url):
	manager.mark_tweeted(book_url)


def main():
	manager.connect()
	consumer = threading.Thread(target=consumer_)
	consumer.setDaemon(True)
	consumer.start()
	producer_()


if __name__ == '__main__':
	main()