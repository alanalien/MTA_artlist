import json
import csv

subway_data = csv.reader(open('subway_station.csv', 'r'))

# create the station information as a dictionary
station_dict = {}
for row in subway_data:

    # skip the first line
    if row[0] == 'NAME':
        continue

    # [POINT (-74.00030814706824 40.73225482650675)]
    # remove the first 7 and last 1 characters and split it with ''
    lat, lon = row[1][7:-1].split(' ')
    station = row[0]
    # dump it into a dictionary
    station_dict[station] = {'lat': lat, 'lon': lon, 'line': row[3]}

    print(station_dict)

    json.dump(station_dict, open('station_geo_info.json', 'w'), indent=2)






# artist_details = json.load(open('artistList_MTA_details.json'))
#
# for artist in artist_details:
#     if "station" in artist:
#         station = artist["station"].replace('Street', 'St').replace('-', ' - ')
#         if station in station_dict:
#             artist.update(station_dict[station])
#
# json.dump(artist_details, open("artist_location.json", 'w'), ensure_ascii=False, indent=2)