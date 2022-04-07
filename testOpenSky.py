#Data from: The OpenSky Network, https://opensky-network.org
import requests, json

result = requests.get('http://opensky-network.org/api/states/all')

resultJSON = result.json()
print(resultJSON)

with open('data.json', 'w') as f: #modified from this StackOverflow on properly storing JSON data: https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
    f.write(str(resultJSON))