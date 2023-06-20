from enum import Enum

class BookingsAvailabilityStatus(str, Enum):
    Available = "available",
    Busy = "busy",
    SlotsAvailable = "slotsAvailable",
    OutOfOffice = "outOfOffice",
    UnknownFutureValue = "unknownFutureValue",

