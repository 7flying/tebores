# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

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