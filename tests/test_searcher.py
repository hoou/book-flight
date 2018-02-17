from unittest import TestCase
from searcher import Searcher
from exceptions import *


class TestSearcher(TestCase):
    def setUp(self):
        self.searcher = Searcher()

    def test_search_valid(self):
        self.assertIsInstance(self.searcher.search('13/04/2018', 'BCN', 'DUB'), str)

    def test_search_bad_date_format(self):
        with self.assertRaises(UnexpectedError):
            self.searcher.search('13.04.2018', 'BCN', 'DUB')

    def test_search_non_existing_flight(self):
        with self.assertRaises(FlightNotFoundError):
            self.searcher.search('13/04/2015', 'AAA', 'BBB')

