## Description

Simple booking script created as task for kiwi.com

## Dependencies

requests package

## Usage

book_flight.py [-h] --date DATE --from FROM --to TO
                      [--one-way | --return RETURN] [--cheapest | --fastest]
                      [--bags BAGS]

optional arguments:
-  `-h, --help`       show this help message and exit
-  `--date DATE`      Date of the flight in format YYYY-MM-DD
-  `--from FROM`      Departure destination defined by 3-letter (IATA) code
-  `--to TO`          Arrival destination defined by 3-letter (IATA) code
-  `--one-way`        Search for flights only in one direction
-  `--return RETURN`  Book return flight with this number of night stands in
                   arrival destination
-  `--cheapest`       Book the cheapest flight
-  `--fastest`        Book the fastest flight
-  `--bags BAGS`      Book the flight with this number of bags

## Examples

```
./book_flight.py --date 2018-04-13 --from BCN --to DUB --one-way

./book_flight.py --date 2018-04-13 --from LHR --to DXB --return 5

./book_flight.py --date 2018-04-13 --from NRT --to SYD --cheapest --bags 2

./book_flight.py --date 2018-04-13 --from CPH --to MIA --fastest
```

## Contributors

Tibor Mikita

## License

MIT