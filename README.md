# MTA Art Collection 

This is a python practice for Pratt Institute's Course Info-664 Program for Cultural Heritage

### Prerequisites

the code run with python 3.7

### Usage

- run ```linkScraper.py```
  this file scrapes http://web.mta.info/mta/aft/index/
  and dumps the json file:
    ```
    artistList_MTA.json
    ```
    including artists' names and the url for further information;
    
    it then scrapes the detail pages and dumps another json file:
    ```
    artistList_MTA_details.json
    ```
    added further information to the former one, including the artwork's located station name, and its title
  
- run ```parse_station.py```
  this file parses the csv file```subway_station.csv```
  and dumps it to a json file:
    ```
    station_geo_info.json
    ```
    which separates the latitude and longitude value, and removed unnecessary datas.
    
- i copied ```artistList_MTA_details.json``` to ```artistList_MTA_details_update.json``` in case of unexpected overwrite.
  
- run ```geo_info.py```
  this file parses the file```subway_station.csv```and
    1. trying to replace the unmatching strings of abbreviate addresses
    2. combine the longitude and latitude to ```artistList_MTA_details_update.json```
  and dumps
    ```
    artist_geoinfo.json
    ```
- Note that the file ```artist_geoinfo.json``` is not a clean data
    there are many values that i can't change using Python, so I manually checked the data and added the file
    ```
    artist_geoinfo_manipulate.json
    ```
- run ```geo2arts.py```
    this file removes the items in ```artist_geoinfo_manipulate.json``` without a geo info, and added a key in the format of (lont|lat) to each item. it dumps:
    ```
    final_addgeo2arts.json
    ```
- then you got a dataset of MTA art collections with their geographic information.

## Visualization
- JavaScript library Leaflet.js has been used to mapping the data ```final_addgeo2arts.json```
- The map was provided by Mapbox.com
- File 

## Data Results
    ```
    final_addgeo2arts.json
    ```

## Acknowledgments

* MTA ART Data Source: http://web.mta.info/mta/aft/index/
* Subway Station Geo-info Source: https://data.world/new-york-city/subway-stations
* Mapping Tool: https://leafletjs.com/
* Map Provider: https://www.mapbox.com/

## Authors

Yiren Wang
Professor: Matthew Miller
