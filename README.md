# Parking-Pal
Application Predicting Parking trends in SF

garage.py
Stores data from SF Park api for garages in San Francisco.
Libraries Used:
  mysql, json, pandas, urllib, xml  

garagerecords.py
Collects live data on parking availability in garages.
Libraries Used:
  xml, urllib, mysql, threading

visualization.py
Applies support vector machine analysis to records to try and predict parking availability in the near future
Libraries Used:
  numpy, matplotlib, sklearn, xml
