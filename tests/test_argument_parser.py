from argparse import ArgumentTypeError
from unittest import TestCase
from argument_parser import ArgumentParser


class TestArgumentParser(TestCase):

    def setUp(self):
        self.parser = ArgumentParser()

    def test__valid_date_bad_format(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._valid_date('10.12.2015')

    def test__valid_date_good_format(self):
        self.assertEqual(self.parser._valid_date('2015-12-10'), '10/12/2015')

    def test__valid_iata_code_short(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._valid_iata_code('AB')

    def test__valid_iata_code_long(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._valid_iata_code('ABCD')

    def test__valid_iata_code_numeric(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._valid_iata_code('AB1')

    def test__valid_iata_code_good_format(self):
        self.assertEqual(self.parser._valid_iata_code('ABC'), 'ABC')

    def test__positive_int_or_zero_negative(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._positive_int_or_zero(-1)

    def test__positive_int_or_zero_alpha(self):
        with self.assertRaises(ArgumentTypeError):
            self.parser._positive_int_or_zero('a')

    def test__positive_int_or_zero_zero(self):
        self.assertEqual(self.parser._positive_int_or_zero(0), 0)

    def test__positive_int_or_zero_positive(self):
        self.assertEqual(self.parser._positive_int_or_zero(1), 1)

    def test_parse_args_empty(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_parse_args_missing_date(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--from', 'BCN', '--to', 'DUB', '--one-way'])

    def test_parse_args_cheapest_fastest_together(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '2018-04-13', '--from', 'CPH', '--to', 'MIA', '--fastest', '--cheapest'])

    def test_parse_args_one_way_return_together(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(
                ['--date', '2018-04-13', '--from', 'BCN', '--to', 'DUB', '--one-way', '--return', '5'])

    def test_parse_args_return_without_value(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '2018-04-13', '--from', 'LHR', '--to', 'DXB', '--return'])

    def test_parse_args_bags_without_value(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '2018-04-13', '--from', 'NRT', '--to', 'SYD', '--cheapest', '--bags'])

    def test_parse_args_from_without_value(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '2018-04-13', '--from', '--to', 'SYD'])

    def test_parse_args_to_without_value(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '2018-04-13', '--from', 'NRT', '--to'])

    def test_parse_args_date_without_value(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args(['--date', '--from', 'NRT', '--to', 'SYD'])
