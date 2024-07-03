import os
import requests
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["AMADEUS_API"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            "grant_type": 'client_credentials',
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

    def get_destination_code(self, city_name):
        code = "TESTING"
        return code