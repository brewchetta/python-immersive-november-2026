# this is the file that controls our connection to the API

import requests

class APIConnector:

    url = "https://de1.api.radio-browser.info/json/stations/search?"
    limit = 5
    attempts = 0

    def __init__(self, station_type=None, countrycode=None):
        self.station_type = station_type
        self.countrycode = countrycode

        self.connect()

    def connect(self):
        self.attempts += 1
        search_params = [ f"limit={self.limit}" ]

        if self.station_type:
            search_params.append(f"type={self.station_type}")
        if self.countrycode:
            search_params.append(f"countrycode={self.countrycode}")

        completed_url = self.url + "&".join(search_params)
        print(completed_url)

        try:
            self.response = requests.get(completed_url)
            return self.response
        except:
            self.response = None
            print("Something went wrong...")
        
    def retry(self):
        return self.connect()