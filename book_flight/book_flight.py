import sys
from argument_parser import ArgumentParser
from searcher import Searcher
from booker import Booker
from exceptions import BookFlightError


def main(args):
    a = ArgumentParser()
    args = a.parse_args(args)

    s = Searcher()
    b = Booker()

    try:
        # 'from' and 'return' are keywords, need to use vars() :-(
        token = s.search(
            args.date,
            vars(args)['from'],
            args.to,
            cheapest=False if args.fastest else True,
            length_of_stay=(0 if args.one_way else vars(args)['return'])
        )
        pnr = b.book(token, args.bags)
        print(pnr)
    except BookFlightError as e:
        print(e, file=sys.stderr)


def run():
    sys.exit(main(sys.argv[1:]))


if __name__ == '__main__':
    run()
