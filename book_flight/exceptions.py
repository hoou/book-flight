class BookFlightError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "An error occurred"
        super(BookFlightError, self).__init__(msg)


class BookingNotConfirmedError(BookFlightError):
    def __init__(self):
        super(BookingNotConfirmedError, self).__init__(msg="Booking was not confirmed")


class UnexpectedError(BookFlightError):
    def __init__(self):
        super(UnexpectedError, self).__init__(msg="Something went wrong")


class FlightNotFoundError(BookFlightError):
    def __init__(self):
        super(FlightNotFoundError, self).__init__(msg="Flight not found")


class InvalidBookingTokenError(BookFlightError):
    def __init__(self):
        super(InvalidBookingTokenError, self).__init__(msg="Invalid booking token")


class ServerError(BookFlightError):
    def __init__(self):
        super(ServerError, self).__init__(msg="Server error - try again later")
