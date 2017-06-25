import json
import pandas as pd
import xlsxwriter
import xml.etree.ElementTree as ET
import urllib.request, urllib
from xml.dom import minidom

week = ['Sunday',
		'Monday',
		'Tuesday',
		'Wednesday', 
        'Thursday',  
        'Friday', 
        'Saturday']

url_str = 'http://api.sfpark.org/sfpark/rest/availabilityservice?TYPE=OFF&radius=10&pricing=yes'
xml_str = urllib.request.urlopen(url_str).read()
xml_doc = minidom.parseString(xml_str)

garage_id_ = 1
rate_id_ = 1

new_garage = {
	'id':[],
	'name':[],
	'lat':[],
	'lon':[],
	'num_spots':[],
	'sun_start':[],
	'sun_end':[],
	'mon_start':[],
	'mon_end':[],
	'tues_start':[],
	'tues_end':[],
	'wed_start':[],
	'wed_end':[],
	'thur_start':[],
	'thur_end':[],
	'fri_start':[],
	'fri_end':[],
	'sat_start':[],
	'sat_end':[],
	'visible':[]
}

garage_rates = {
	'id':[],
	'fk_garage_id':[],
	'start_hour':[],
	'end_hour':[],
	'price':[],
	'qualifier':[],
	'visible':[]
}

avl = xml_doc.getElementsByTagName('AVL')

for el in avl:
	name = el.getElementsByTagName("NAME")[0].firstChild.nodeValue
	if el.getElementsByTagName("OPER").length > 0:
		oper = el.getElementsByTagName("OPER")[0].firstChild.nodeValue
	else:
		oper = 0
	[lon, lat] = el.getElementsByTagName("LOC")[0].firstChild.nodeValue.split(",")
	hours = [['Closed', 'Closed']]*7
	#Manage hours of operation
	for ops in el.getElementsByTagName("OPS"):
		#Start Day
		from_ = ops.getElementsByTagName("FROM")[0].firstChild.nodeValue
		if from_ != '7 Days/Wk':
			#End Day
			if ops.getElementsByTagName("TO").length > 0:
				to_ = ops.getElementsByTagName("TO")[0].firstChild.nodeValue
			else:
				to_ = 0

			#Start Time
			beg_ = ops.getElementsByTagName("BEG")[0].firstChild.nodeValue
			#End Time
			if ops.getElementsByTagName("END").length > 0:
				end_ = ops.getElementsByTagName("END")[0].firstChild.nodeValue
				i = week.index(from_)
				hours[i] = [beg_, end_]
				if to_:
					for j in range(i, week.index(to_) + 1):
						hours[j] = [beg_, end_]
			else:
				hours = [beg_, beg_]
		else:
			#Start Time
			beg_ = ops.getElementsByTagName("BEG")[0].firstChild.nodeValue
			#End Time
			if ops.getElementsByTagName("END").length > 0:
				end_ = ops.getElementsByTagName("END")[0].firstChild.nodeValue
				hours = [[beg_, end_]]*7
			else:
				hours = [['12:00 AM', '12:00 AM']]*7

	#Info
	new_garage['id'].append(garage_id_)
	new_garage['name'].append(name)
	new_garage['lat'].append(lat)
	new_garage['lon'].append(lon)
	new_garage['num_spots'].append(oper)
	#Hours
	new_garage['sun_start'].append(hours[0][0])
	new_garage['sun_end'].append(hours[0][1])
	new_garage['mon_start'].append(hours[1][0])
	new_garage['mon_end'].append(hours[1][1])
	new_garage['tues_start'].append(hours[2][0])
	new_garage['tues_end'].append(hours[2][1])
	new_garage['wed_start'].append(hours[3][0])
	new_garage['wed_end'].append(hours[3][1])
	new_garage['thur_start'].append(hours[4][0])
	new_garage['thur_end'].append(hours[4][1])
	new_garage['fri_start'].append(hours[5][0])
	new_garage['fri_end'].append(hours[5][1])
	new_garage['sat_start'].append(hours[6][0])
	new_garage['sat_end'].append(hours[6][1])

	new_garage['visible'].append(1)
	

	rs = el.getElementsByTagName("RS")
	for ent in rs:
		if ent.getElementsByTagName("DESC").length == 0:
			beg_ = ent.getElementsByTagName("BEG")[0].firstChild.nodeValue
			end_ = ent.getElementsByTagName("END")[0].firstChild.nodeValue
			rate_ = ent.getElementsByTagName("RATE")[0].firstChild.nodeValue
			qualifier_ = ent.getElementsByTagName("RQ")[0].firstChild.nodeValue
		else:
			pass

		garage_rates['id'].append(rate_id_)
		garage_rates['fk_garage_id'].append(garage_id_)
		garage_rates['start_hour'].append(beg_)
		garage_rates['end_hour'].append(end_)
		garage_rates['price'].append(rate_)
		garage_rates['qualifier'].append(qualifier_)
		garage_rates['visible'].append(1)

		rate_id_ = rate_id_ + 1

	garage_id_ = garage_id_ + 1

	
df = pd.DataFrame(new_garage)

writer = pd.ExcelWriter('garages.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'garages')

writer.save()

df = pd.DataFrame(garage_rates)

writer = pd.ExcelWriter('garage_rates.xlsx', engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'rates')

writer.save