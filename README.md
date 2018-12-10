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
  this file parses the csv file```subway_station.csv'```
  and dumps it to a json file:
    ```
    station_geo_info.json
    ```
    which separates the latitude and longitude value, and removed unnecessary datas.
  
- run ```add_location.py```
    this file combines the following two json files:
    ```
    artistList_MTA_details.json
    ```
    ```
    station_geo_info.json
    ```
- then you got a dataset of MTA art collections with their geographic information.
    

## Data Results
    ```
    MTA_Art_Collection.json
    ```

## Acknowledgments

* MTA ART Data Source: http://web.mta.info/mta/aft/index/
* Subway Station Geo-info Source: https://data.world/new-york-city/subway-stations
* http://www.echartsjs.com/index.html

## Authors

Yiren Wang
Professor: Matthew Miller
