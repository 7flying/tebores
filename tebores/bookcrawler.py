# -*- coding: utf-8 -*-

import abc
import re
from bs4 import BeautifulSoup
from requests import get

url_itebooks = 'http://it-ebooks.info'
url_freecomputerbooks = 'http://freecomputerbooks.com'


class BookCrawler(object):
    """Base class of crawlers"""

    def __init__(self, url):
        self.url = url
        self.html = self.get_html(url)

    def get_html(self, web_page):
        return BeautifulSoup(get(web_page).text, 'html.parser')

    def get_url(self):
        return self.url

    @abc.abstractmethod
    def get_books(self):
        """Returns a dict of book url - book name"""

    @staticmethod
    def factory(name):
        if name == 'ITebooksCrawler':
            return ITebooksCrawler()
        elif name == 'FreeCBCrawler':
            return FreeCBCrawler()
        else:
            print "nothing found"


class ITebooksCrawler(BookCrawler):
    """It-ebooks.info page crawler """

    def  __init__(self, url=url_itebooks):
        BookCrawler.__init__(self, url)
        
    def get_books(self):
        soup = self.html
        book_dict = {}

        for table in soup.find_all('table'):
            if 'main' not in table.attrs:
                for link in table.find_all('a'):
                    if re.match('.*/book/[\d]+/', link.get('href')):
                        book_dict[link.get('href')] = link.text
        return book_dict


class FreeCBCrawler(BookCrawler):
    """freecomputerbooks.com crawler"""
    
    def __init__(self, url=url_freecomputerbooks):
        BookCrawler.__init__(self, url)

    def get_books(self):
        soup = self.html
        book_dict =  {}
        for li in soup.find(id='newBooksG').find_all('li'):
            for link in li.find_all('a'):
                if re.match('/.*', link.get('href')):
                    book_dict[link.get('href')] = link.text
        return book_dict
