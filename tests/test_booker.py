from unittest import TestCase
from booker import Booker
from searcher import Searcher
from exceptions import *


class TestBooker(TestCase):
    def setUp(self):
        self.booker = Booker()
        self.searcher = Searcher()
        self.token = self.searcher.search('13/04/2018', 'BCN', 'DUB')

    def test_book_valid(self):
        self.assertIsInstance(self.booker.book(self.token), str)

    def test_book_bad_token(self):
        with self.assertRaises(InvalidBookingTokenError):
            self.assertIsInstance(self.booker.book('dsadsadsa'), str)
