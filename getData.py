#Brazenly copied from https://pypi.org/project/FlightRadarAPI/

from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()

airline_icao = "DAL"
flights = fr_api.get_flights(airline = airline_icao)
airline_icao = "UAL"
flights.append(fr_api.get_flights(airline = airline_icao))
airline_icao = "AAL"
flights = fr_api.get_flights(airline = airline_icao)
airline_icao = "NKS"
flights.append(fr_api.get_flights(airline = airline_icao))

print(flights)