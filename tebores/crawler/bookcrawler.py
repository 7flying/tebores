# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from requests import get

url_itebooks = 'http://it-ebooks.info/'
url_freecomputerbooks = 'http://freecomputerbooks.com/'


class BookCrawler(object):

	def __init__(self, url):
		self.url = url
		self.html = self.get_html(url)

	def get_html(self, web_page):
		return BeautifulSoup(get(web_page).text)

	def get_url(self):
		return self.url


class ITebooksCrawler(BookCrawler):
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

def main():
	
	cb = FreeCBCrawler()
	print cb.get_books()
	print "-" * 10
	itb = ITebooksCrawler()
	print itb.get_books()
	
	
	
	


if __name__ == '__main__':
	main()