# -*- coding: utf-8 -*-
from os.path import isfile
import sqlite3 as lite
import sys

class DBManager(object):
	
	conn = None
	
	def __init__(self, name):
		self.name = name
		if not isfile(self.name):
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
				url TEXT NOT NULL UNIQUE,
				tweeted INTEGER NOT NULL DEFAULT 0);"""
			)

			cursor.execute("INSERT INTO Webs (name, url)" +
                           " VALUES ('it-ebooks', 'http://it-ebooks.info')")
			cursor.execute("INSERT INTO Webs (name, url)" +
                           " VALUES ('freecomputerbooks'," +
                           " 'http://freecomputerbooks.com')")

			DBManager.conn.commit()
			self.disconnect()
		else:
			print "Database already created"


	def connect(self):
		if DBManager.conn == None:
			try:
				DBManager.conn = lite.connect(self.name)
			except lite.Error, e:
				print "Exception %s" % e.args[0]

	def disconnect(self):
		if DBManager.conn:
			DBManager.conn.close()
			DBManager.conn = None

	def insert_book(self, book_web_url, book_name, book_url):
		cursor = DBManager.conn.cursor()
		# Get book_web_url id
		cursor.execute("SELECT id FROM Webs WHERE url = ?", (book_web_url,))
		result = cursor.fetchone()
		if result:
			cursor.execute("INSERT INTO Books (idWeb, name, url)" +
                           " VALUES (?, ?, ?);",
                           (result[0], book_name, book_url))
			DBManager.conn.commit()
		

	def is_new_book(self, book_url):
		cursor = DBManager.conn.cursor()
		cursor.execute("SELECT * FROM Books WHERE url = ?", (book_url,))
		result = cursor.fetchone()
		return False if result else True

	def is_tweeted(self, book_url):
		cursor = DBManager.conn.cursor()
		cursor.execute("SELECT tweeted FROM Books WHERE url = ?", (book_url,))
		result = cursor.fetchone()
		return False if result == 0 else True

	def mark_tweeted(self, book_url):
		cursor = DBManager.conn.cursor()
		cursor.execute("UPDATE Books SET tweeted = 1 WHERE url = ?", (book_url,))
		DBManager.conn.commit()
		if self.is_tweeted(book_url):
			print "UPDATE OK\n"
		else:
			print "UPDATE FAIL\n"

