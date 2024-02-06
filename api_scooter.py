import json
import requests
from constant import Constants


class ScooterApi:

    def __init__(self):
        self.headers = Constants.def_headers

    def post(self, url, input_data):
        response = requests.post(url=url, headers=self.headers, data=json.dumps(input_data))
        return response

    def get(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response

    def put(self, url):
        response = requests.put(url=url, headers=self.headers)
        return response
