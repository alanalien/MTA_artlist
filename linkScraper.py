import requests
from bs4 import BeautifulSoup
import json
# import lxml to use xpath
from lxml import etree
import time

# define function
def getArtistsURL():
    res = requests.get('http://web.mta.info/mta/aft/index/')
    soup = BeautifulSoup(res.content, 'html.parser')

    tables = soup.find_all('table')
    table = tables[0]


    artists = []
    rows = table.find_all('tr')

    for row in rows:
        grids = row.find_all('td')

        for grid in grids:
            # each td has a <h3> as the artist's name and a <p> with an <a> element in
            # get the artist's name, either via find all <h3> or grid.h3 as the h3 in the td ('grid')
            # artistsName = grid.find_all('h3')
            artistsName = grid.h3.text
            # get links from as attributes of <a> nested in the <p>, and use ['href'] to get the link
            pageLink = grid.p.a.attrs['href']
            artistType = grid.p.a.text

            # print(pageLink)

            # now the link is not an entire address
            # dump it to a json file

            artists.append({
                'artistName': artistsName,
                # [2:-1] means append the string without the first two letters and the last one letter
                'url': 'http://web.mta.info/mta/aft' + pageLink[2:],
                'type': artistType
            })

            json.dump(artists, open('artistList_MTA.json', 'w'), ensure_ascii=False, indent=2)


def get_one_artist_detail(url):
    res = requests.get(url)
    html = etree.HTML(res.content)
    # using xpath to find the path to the element we want by id, "//*" means find all children
    station_info = html.xpath('//*[@id="pasingletext"]/p[1]')
    station = station_info[0].text
    title_element = html.xpath('//*[@id="pasingletext"]/p[3]')
    title = title_element[0].text
    # print(station)
    # print(title)

    # return the result to the next function
    return station, title


def getArtistURL_details():
    artistList = json.load(open('artistList_MTA.json'))

    for detail in artistList:
        url = detail['url']

        if detail['type'] == 'Music' or detail['type'] == 'Poster' or detail['type'] == 'Lightbox' or detail['type'] == 'Art Card':
            continue

        try:
            # get the station and title info from the 2nd function
            station, title = get_one_artist_detail(url)
            # add two new item into the dictionary in the list
            detail['station'] = station
            detail['title'] = title
            print('success:' + url)

        except:
            print('error:' + url)

        time.sleep(3)

    json.dump(artistList, open('artistList_MTA_details.json', 'w'), ensure_ascii=False, indent=2)


# this script running starts here
if __name__ == '__main__':
    # call function get URL
    getArtistsURL()
    getArtistURL_details()