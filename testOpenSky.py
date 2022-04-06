#Data from: The OpenSky Network, https://opensky-network.org
from opensky_api import OpenSkyApi
import json
api = OpenSkyApi()
s = api.get_states()

print(s)
with open('data.txt', 'w', encoding='utf-8') as f: #modified from this StackOverflow on properly storing JSON data: https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
    f.write(str(s))