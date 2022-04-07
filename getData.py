"""Data fetching script. Written by Roo Case, using documentation from AviationStack."""
"""Fetching script taken from AviationStack's code samples for API requests"""
import requests, json

params = {
  'access_key': 'ab16a35958c85b847d791be015b60d84'
}



api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()


with open('data.json', 'w') as f: #modified from this StackOverflow on properly storing JSON data: https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file
    f.write(str(api_response))

for flight in api_response['results']:
    if (flight['live']['is_ground'] is False):
        print(u'%s flight %s from %s (%s) to %s (%s) is in the air.' % (
            flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata']))
