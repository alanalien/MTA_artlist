import json
artists = json.load(open('artist_geoinfo_manipulate.json'))


# 列表解析：only use the items with geo info
artists = [t for t in artists if "lont" in t]

# lont - lat change place
addgeo2arts = {}
for art in artists:
    key = "{}|{}".format(art['lont'], art['lat'])
    if key not in addgeo2arts:
        addgeo2arts[key] = []
    addgeo2arts[key].append(art)

json.dump(addgeo2arts, open("final_addgeo2arts.json", 'w'), ensure_ascii=False, indent=2)
