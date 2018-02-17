import argparse
from datetime import datetime


class ArgumentParser:
    @staticmethod
    def _valid_date(s):
        try:
            return datetime.strptime(s, "%Y-%m-%d").strftime("%d/%m/%Y")
        except ValueError:
            msg = "Not a valid date: '{0}'.".format(s)
            raise argparse.ArgumentTypeError(msg)

    @staticmethod
    def _valid_iata_code(s):
        if s.isalpha() and len(s) == 3:
            return s
        else:
            msg = "Not a valid IATA code: '{0}'".format(s)
            raise argparse.ArgumentTypeError(msg)

    @staticmethod
    def _positive_int_or_zero(value):
        try:
            int_value = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError("%s is not valid number" % value)
        if int_value < 0:
            raise argparse.ArgumentTypeError("%s is not positive integer nor zero" % value)
        return int_value

    def parse_args(self, args):
        parser = argparse.ArgumentParser()

        parser.add_argument('--date', type=self._valid_date, required=True,
                            help="Date of the flight in format YYYY-MM-DD")

        parser.add_argument('--from', type=self._valid_iata_code, required=True,
                            help="Departure destination defined by 3-letter (IATA) code")

        parser.add_argument('--to', type=self._valid_iata_code, required=True,
                            help="Arrival destination defined by 3-letter (IATA) code")

        group = parser.add_mutually_exclusive_group()
        group.add_argument('--one-way', action='store_true',
                           help="Search for flights only in one direction")
        group.add_argument('--return', type=self._positive_int_or_zero, default=0,
                           help="Book return flight with this number of night stands in arrival destination")

        group = parser.add_mutually_exclusive_group()
        group.add_argument('--cheapest', action='store_true',
                           help="Book the cheapest flight")
        group.add_argument('--fastest', action='store_true',
                           help="Book the fastest flight")

        parser.add_argument('--bags', type=self._positive_int_or_zero, default=0,
                            help="Book the flight with this number of bags")

        return parser.parse_args(args)
