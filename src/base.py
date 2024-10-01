import requests
from urllib import parse

class BaseClient():
    def __init__(self):
        self.base_url = "https://api.sleeper.app"
        self.base_uri = '/'
        self.version = 'v1'
        self.headers = {"Content-Type": "application/json"}


    def get(self, uri: str, params = None):
        full_url = parse.urljoin(
            self.base_url, f"/{self.version}/{self.base_uri}{uri}"
        )

        print(f"Requesting: {full_url}")

        response = requests.get(full_url, params=params, headers=self.headers)
        return response.json()


