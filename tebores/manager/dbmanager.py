# -*- coding: utf-8 -*-
from os.path import isfile
import sqlite3 as lite
import sys
"""
conn = None

try:
	conn = lite.connect('tebores_test.db')
	cur = conn.cursor()
	cur.execute('CREATE TABLE Webs (id INT, name TEXT, url TEXT)')
	cur.execute("INSERT INTO Webs VALUES (1, 'it-ebooks', 'http://it-ebooks.info/')")
	cur.execute("INSERT INTO Webs VALUES (2, 'freecomputerbooks', 'http://freecomputerbooks.com/')")
	conn.commit()
	conn.close()
except lite.Error, e:
	print "Some error %s" % e.args[0]
finally:
	if conn:
		conn.close()

"""
class DBManager(object):
	
	conn = None
	dbname = 'tebores_test.db'
	
	def __init__(self):
		if not isfile(DBManager.dbname):
			self.connect()
			cursor = DBManager.conn.cursor()
			cursor.execute(
				"""CREATE TABLE Webs (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				 name TEXT NOT NULL,
				 url TEXT NOT NULL UNIQUE);"""
			)
			cursor.execute(
				"""CREATE TABLE Books (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				idWeb INTEGER NOT NULL REFERENCES Webs (id) ON DELETE CASCADE,
				name TEXT NOT NULL,
				url TEXT NOT NULL UNIQUE);"""
			)

			#cursor.execute("INSERT INTO Webs (name, url) VALUES ('it-ebooks', 'http://it-ebooks.info/')")
			#cursor.execute("INSERT INTO Webs (name, url) VALUES ('freecomputerbooks', 'http://freecomputerbooks.com/')")

			DBManager.conn.commit()
			self.disconnect()
		else:
			print "Database already created"


	def connect(self):
		if DBManager.conn == None:
			try:
				DBManager.conn = lite.connect(DBManager.dbname)
			except lite.Error, e:
				print "Exception %s" % e.args[0]

	def disconnect(self):
		if DBManager.conn:
			DBManager.conn.close()

	def insert_book(self, book_web_url, book_name, book_url):
		cursor = DBManager.conn.cursor()
		# Get book_web_url id
		cursor.execute("SELECT id FROM Webs WHERE url = ?;", (book_web_url,))
		result = cursor.fetchone()
		if result:
			cursor.execute("INSERT INTO Books (idWeb, name, url) VALUES (?, ?, ?);", (result, book_name, book_url))
			DBManager.conn.commit()
			print "book inserted"
		else:
			print "not fetched"


if __name__ == '__main__':
	manager = DBManager()
	manager.connect()
	manager.insert_book("http://it-ebooks.info/", "some book name", "some book url")
	manager.disconnect()
