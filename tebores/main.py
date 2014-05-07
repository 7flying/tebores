# -*- coding: utf-8 -*-

import threading
import Queue
from time import sleep

from bots import desktopbot
from files import auth
from crawler import bookcrawler
from manager import dbmanager

new_books = Queue.Queue()
manager = dbmanager.DBManager()
ttl = 0

def producer_():
	crawlers = []
	crawlers.append(bookcrawler.ITebooksCrawler())
	crawlers.append(bookcrawler.FreeCBCrawler())
	while True:
		for crawler in crawlers:
			books = crawler.get_books()
			for book in books.keys():
				if is_new_book(book):
					# url of web page, book name, book url
					manager.insert_book(crawler.get_url(), books[book], book)
					new_books.put(books[book])
			sleep(60)


def consumer_():
	bot = bots.DesktopBot()
	bot.sign_in(auth.user, auth.password)
	while True:
		book = new_books.get()
		bot.tweet("New book: " + book)
		sleep(5)

def is_new_book(book_url):
	return manager.is_new_book(book_url)

def main():
	typo = True
	while  typo:
		try:
			ttl = int(raw_input('Time to live > '))
			typo = False
		except ValueError:
			typo = True

	manager.connect()
	consumer = threading.Thread(target=consumer_)
	consumer.setDaemon(True)
	consumer.start()
	producer = threading.Thread(target=producer_)
	producer.setDaemon(True)
	producer.start()


if __name__ == '__main__':
	main()