# Parking Pal

We developed three separate applications for Parking-Pal:


## 1. Parking Data collection (Python Web clawler) and API to retrive those data
### garagerecords.py
Web clawler that collects live data about parking garage availability.
Libraries Used:
  xml, urllib, mysql, threading
<p align="center"><img width="90%" vspace="20" src="https://drive.google.com/file/d/0B4pwCE5pbSmUTDF4VHB4NmNoNWM/view?usp=sharing"></p>

### Parking Pal Data API 
[Parking Pal API](http://104.154.229.56/api.php/availability) - Data collected from garagerecords.py can be access from this api
<p align="center"><img width="90%" vspace="20" src="https://drive.google.com/file/d/0B4pwCE5pbSmUWmhwelNRSmttM28/view?usp=sharing"></p>

They are currently running in our Google Cloud server.


## 2. Parking availability prediction:
Application Predicting Parking trends in San Francisco
### Installation
garage.py
Stores data from SF Park api for garages in San Francisco.
Libraries Used:
  mysql, json, pandas, urllib, xml  

visualization.py
Applies support vector machine analysis to records to try and predict parking availability in the near future
Libraries Used:
  numpy, matplotlib, sklearn, xml

<p align="center"><img width="90%" vspace="20" src="https://drive.google.com/open?id=0B4pwCE5pbSmURldURmMzR2dhNDA"></p>


## 3. Parking Pal Client-side application (Android)
The description of this application is located in this respository: 
[!A|Parking Pal](https://cldup.com/dTxpPi9lDf.thumb.png)](https://github.com/wingardtw/Parking-Pal/tree/master/Parking_Radar(Android))



### License
----
MIT
**Free Software, Feel free to use it!**
