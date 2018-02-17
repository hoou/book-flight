from urllib.parse import urlencode

import requests

from exceptions import *


class Searcher:
    _API_EP_SEARCH_FLIGHTS = 'https://api.skypicker.com/flights'
    _MARKET = 'cz'
    _PARTNER = 'picky'

    def search(self, date, departure_destination, arrival_destination, length_of_stay=0, cheapest=True):
        params = {
            'flyFrom': departure_destination,
            'to': arrival_destination,
            'dateFrom': date,
            'dateTo': date,
            'partner': self._PARTNER,
            'partner_market': self._MARKET,
            'sort': 'price' if cheapest else 'duration',
            'limit': 1
        }
        if length_of_stay > 0:
            params.update({
                'daysInDestinationFrom': length_of_stay,
                'daysInDestinationTo': length_of_stay,
            })

        r = requests.get(self._API_EP_SEARCH_FLIGHTS, urlencode(params))

        if r.status_code == 200:
            if r.json()['data']:
                return r.json()['data'][0]['booking_token']
            else:
                raise FlightNotFoundError
        else:
            raise UnexpectedError
