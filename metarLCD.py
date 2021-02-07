#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
import lcddriver
import time

display = lcddriver.lcd()

# Initialize the conditions dictionary
condDict = {}

def getMetEntry(metar, entry):
        if metar.find(entry) == None:
                return "-"
        return metar.find(entry).text

# Read the airports file to retrieve list of airports and use as order for LEDs
with open("/home/pi/metar/METARMap/airportsLCD") as f:
        airports = f.readlines()
        airports = [x.strip() for x in airports]
        
# Retrieve METAR from aviationweather.gov data server
# Details about parameters can be found here: https://www.aviationweather.gov/dataserver/example?datatype=metar
url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=5&mostRecentForEachStation=true&stationString=" + ",".join([item for item in airports if item != "NULL"])

# Download the latest METARs
req = urllib.request.Request(url)
content = urllib.request.urlopen(req).read()
#print(content)
root = ET.fromstring(content)

# Retrieve airport conditions
for metar in root.iter('METAR'):
        stationId = getMetEntry(metar,'station_id')
        flightCategory =getMetEntry(metar,'flight_category')
        temp = getMetEntry(metar,'temp_c')
        windDir = getMetEntry(metar,'wind_dir_degrees')
        windSpd = getMetEntry(metar,'wind_speed_kt')
        windGst = getMetEntry(metar,'wind_gust_kt')
        vis = getMetEntry(metar,'visibility_statute_mi')
        condDict[stationId] = {'flightCategory':flightCategory, 'temp':temp, 'windDir':windDir, 'windSpd':windSpd, 'windGst':windGst, 'vis':vis}

while True:
        for (i,stationId) in enumerate(airports):
                display.lcd_clear()
                display.lcd_display_string(stationId + " - " + condDict[stationId]['flightCategory'], 1)
                if condDict[stationId]['windSpd'] == str(0):
                        display.lcd_display_string("Wind calm",2)
                else:
                        display.lcd_display_string("Wind " + condDict[stationId]['windDir'] + " @ " + condDict[stationId]['windSpd'] + " kts", 2)
                time.sleep(5)
                display.lcd_clear()
                display.lcd_display_string(stationId + " - " + condDict[stationId]['flightCategory'], 1)
                display.lcd_display_string("Vis. " + condDict[stationId]['vis'] + " miles",2)
                time.sleep(5)
                display.lcd_clear()
                display.lcd_display_string(stationId + " - " + condDict[stationId]['flightCategory'], 1)
                display.lcd_display_string("Temp. " + condDict[stationId]['temp'] + "C",2)
                time.sleep(5)
