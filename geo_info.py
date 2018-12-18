import csv
import json
import re
from urllib.parse import urlparse

csv_file = csv.reader(open('subway_station.csv', 'r'))


station_dict = {}
for row in csv_file:
    if row[0] == 'NAME':
        continue
    lont, lat = row[1][7:-1].split(' ')
    station = row[0]
    lines = row[3].split('-')
    for line in lines:
        if line not in station_dict:
            station_dict[line] = {}
        station_dict[line][station] = {'lont': float(lont), 'lat': float(lat)}

replace_table = {
        "Street": "St",
        "Avenue": "Ave",
        "Avenues": "Ave",
        "Highway": "Hwy",
        "Square": "Sq",
        "Road": "Rd",
        "Fifth": "5th",
        "Parkway": "Pkwy",
        "Place": "Pl",
        "Plaza": "Plz",
        "Boulevard": "Blvd",
        "Mount": "Mt",
        "East ": "E ",
        "West ": "W ",
        "-": " - "
    }


def try_update(station, line, artist):
    if line in station_dict:
        if station in station_dict[line]:
            artist.update(station_dict[line][station])
            return True
    return False


def geo_mapping():
    artists = json.load(open('artistList_MTA_details_update.json'))
    for artist in artists:
        url = urlparse(artist["link"])
        line = ''
        for param in url.query.split('&'):
            if param.startswith('line'):
                line = param[5:]

        station = artist["station"]
        for k, v in replace_table.items():
            station = station.replace(k, v)

        rd_station = re.sub(r'(\d+)', r'\1rd', station)
        th_station = re.sub(r'(\d+)', r'\1th', station)
        nd_station = re.sub(r'(\d+)', r'\1nd', station)

        if try_update(station, line, artist):
            pass
        elif try_update(rd_station, line, artist):
            pass
        elif try_update(th_station, line, artist):
            pass
        elif try_update(nd_station, line, artist):
            pass
        elif try_update(station.split('-')[0].strip(), line, artist):
            pass
        else:
            if line in station_dict:
                for k, v in station_dict[line].items():
                    parts = k.split('-')
                    for part in parts:
                        part = part.strip()
                        if station.find(part) >=0 or part.find(station) >=0:
                            artist.update(v)

    json.dump(artists, open("artist_geoinfo.json", 'w'), ensure_ascii=False, indent=2)


if __name__ == '__main__':
    # call function
    geo_mapping()

# this function can't fix all the station names, in csv, there are repeated station names of different lines. So I manipulated the data later, with the line info in the url.