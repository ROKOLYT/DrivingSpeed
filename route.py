import requests
import time

class Route():
    def __init__(self):
        self.url = r"https://api.openrouteservice.org"
        self.headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',}
        self.key = "5b3ce3597851110001cf624805101820413d4b81b42f57ee832b8c9c"
        self.directions = directions(self.url, self.key, self.headers)
        
    def distance(self):
        if not self.directions.route:
            raise ValueError
        properties = self.directions.route["features"][0]["properties"]
        segment_0 = properties["segments"][0]
        distance = segment_0["distance"]
        
        return distance

class directions():
    def __init__(self, url, key, headers):
        self.url = url
        self.key = key
        self.headers = headers
        self.geocode = geocode()
        self.route = None
    
    def get(self, origin, destination):
        url = f"{self.url}/v2/directions/driving-car?"
        origin_geocode = self.geocode.get(origin)
        time.sleep(1)
        destination_geocode = self.geocode.get(destination)
        params = {"api_key": self.key, "start": origin_geocode, "end": destination_geocode}
        route = requests.get(url, headers=self.headers, params=params)
        self.route = route.json()
    
class geocode():
    def __init__(self):
        self.url = r"https://geocode.maps.co/search"
        self.key = "664df4c944d4f898209254twk333735"

    def get(self, address):
        params = {"api_key": self.key, "q": address}
        response = requests.get(self.url, params=params)
        
        response = response.json()[0]
        longitude = response["lon"]
        latitude = response["lat"]
        
        return f"{longitude},{latitude}"