import xml.etree.ElementTree as ET
import urllib.request, urllib
from xml.dom import minidom
import threading
import mysql.connector

db = mysql.connector.connect(host = "localhost",
					 user = "root",
					 passwd = "",
					 db = "parking_pad"
					)

cur = db.cursor()

def collect():
	threading.Timer(600, collect).start()
	url_str = 'http://api.sfpark.org/sfpark/rest/availabilityservice?TYPE=OFF&radius=10'
	xml_str = urllib.request.urlopen(url_str).read()
	xml_doc = minidom.parseString(xml_str)


	avl = xml_doc.getElementsByTagName('AVL')

	for el in avl:
		name_ = el.getElementsByTagName("NAME")[0].firstChild.nodeValue
		temp_query = 'SELECT id FROM carage WHERE name = "' + name_ + '"'
		cur.execute(temp_query)
		for thing in cur:
			garage_id = int(thing[0])
		if el.getElementsByTagName("OCC").length > 0:
			avail = int(el.getElementsByTagName("OCC")[0].firstChild.nodeValue)
		else:
			avail = 0
		add_entry = ("INSERT INTO availability "
					 "(garage_id, availability, datetime, visible) "
					 "VALUES (%d, %d, %s, %d)")
		data = (garage_id, avail, 'NOW()', 1)
		print(add_entry % data)
		cur.execute(add_entry % data)
	db.commit()
collect()