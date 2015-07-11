# -*- coding: utf-8 -*-

import threading
import Queue
from time import sleep
from datetime import datetime
from sys import argv

import config
from bookcrawler import BookCrawler
from bots import DesktopBot, TwitterAPIBot
from files import auth
from dbmanager import DBManager

new_books = Queue.Queue() # Holds a tuple of (BookName-url)
manager = DBManager(config.DB_NAME)

to_mark = [] # Books to mark as tweeted
to_mark_lock = threading.Condition() 

def producer_(time_to_wait):
    """Producer thread, checks the book pages."""
    crawlers = []
    for subcrawler in BookCrawler.__subclasses__():
        print subcrawler.__name__
        crawlers.append(BookCrawler.factory(subcrawler.__name__))
    while True:
        for crawler in crawlers:
            books = crawler.get_books()
            for book in books.keys():
                if is_new_book(book):
                    # url of web page, book name, book url
                    insert_book(crawler.get_url(), books[book], book)
                    print " [ producer ] New book: %s" % (books[book] + \
                                                          " - " + \
                                                          crawler.get_url() + \
                                                          book)
                    new_books.put((books[book], crawler.get_url() + book))
                    with to_mark_lock:
                        while not to_mark:
                            to_mark_lock.wait()
                        mark = to_mark.pop(0)
                        mark_tweeted(mark)
                    # Wait the required time before cheking the next book
                    sleep(time_to_wait)
            sleep(1)


def consumer_():
    """Consumer thread, tweets the book updates."""
    if config.BOT_TYPE == 'DesktopBot':
        bot = DesktopBot()
        bot.sign_in(auth.user, auth.password)
    else:
        bot = TwitterAPIBot()
        bot.sign_in()
    while True:
        book = new_books.get()
        total_len = len(book[0]) + len(book[1]) + 1
        if total_len > 140:
            book[0] = book[0][:-(total_len - 140)]
        bot.tweet(book[0] + " " + book[1])
        print " [ consumer ] Tweet: %s \n\t@%s" % ((book[0] + " " + book[1]),
                                                   datetime.now().time())
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

def main(time_to_wait=60):
    manager.connect()
    consumer = threading.Thread(target=consumer_)
    consumer.setDaemon(True)
    consumer.start()
    producer_(time_to_wait)


if __name__ == '__main__':
    if len(list(argv)) == 1:
        main()
    else:
        main(int(argv[1]))
