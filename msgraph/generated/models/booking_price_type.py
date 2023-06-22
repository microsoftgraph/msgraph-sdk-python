from enum import Enum

class BookingPriceType(str, Enum):
    # The price of the service is not defined.
    Undefined = "undefined",
    # The price of the service is fixed.
    FixedPrice = "fixedPrice",
    # The price of the service starts with a particular value, but can be higher based on the final services performed.
    StartingAt = "startingAt",
    # The price of the service depends on the number of hours a staff member works on the service.
    Hourly = "hourly",
    # The service is free.
    Free = "free",
    # The price of the service varies.
    PriceVaries = "priceVaries",
    # The price of the service is not listed.
    CallUs = "callUs",
    # The price of the service is not set.
    NotSet = "notSet",
    UnknownFutureValue = "unknownFutureValue",

