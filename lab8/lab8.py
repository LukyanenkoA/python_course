'''
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen("8.osm")
xml = resp.read().decode("utf8")
soup = BeautifulSoup(xml, "lxml")
cnt = 0
dict ={}
for node in soup.find_all("node"):
    for tag in node("tag"):
        if tag["k"] == "shop" and tag["v"] == "supermarket":
            cnt+=1
print(cnt)
'''
import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type,
                                  elem.id,
                                  elem.version,
                                  elem.visible,
                                  pd.Timestamp(elem.timestamp),
                                  elem.uid,
                                  elem.user,
                                  elem.changeset,
                                  len(elem.tags),
                                  tag.k,
                                  tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")


osmhandler = OSMHandler()
osmhandler.apply_file("8.osm")
df_osm = pd.DataFrame(osmhandler.osm_data)
supermarkets = df_osm[df_osm[10] == 'supermarket']

result = df_osm[(df_osm[9] == 'name') & (df_osm[1].isin(supermarkets[1]))]
print(result)

osmhandler.apply_file("8 - 2.osm")
df_osm = pd.DataFrame(osmhandler.osm_data)
supermarkets = df_osm[df_osm[10] == 'supermarket']

result = df_osm[(df_osm[9] == 'name') & (df_osm[1].isin(supermarkets[1]))]
print(result)