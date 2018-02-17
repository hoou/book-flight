import requests
from exceptions import *


class Booker:
    _API_EP_BOOKING = 'http://128.199.48.38:8080/booking'
    _MARKET = 'cz'
    _CURRENCY = 'CZK'

    _TESTING_PASSENGER = {
        'firstName': 'test',
        'lastName': 'test',
        'title': 'Mr',
        'birthday': '1990-04-13',
        'documentID': '',
        'email': 'email.address@gmail.com'
    }

    def book(self, token, bags=0):
        body_params = {
            'bags': bags,
            'booking_token': token,
            'currency': self._CURRENCY,
            'passengers': [
                self._TESTING_PASSENGER
            ]
        }

        r = requests.post(self._API_EP_BOOKING, json=body_params)

        if r.status_code == 200:
            if r.json()['status'] == 'confirmed':
                return r.json()['pnr']
            else:
                raise BookingNotConfirmedError
        elif r.status_code == 422:
            raise InvalidBookingTokenError
        elif r.status_code == 500:
            raise ServerError
        else:
            raise UnexpectedError
