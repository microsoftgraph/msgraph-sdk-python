from enum import Enum

class BookingsAvailabilityStatus(Enum):
    Available = "available",
    Busy = "busy",
    SlotsAvailable = "slotsAvailable",
    OutOfOffice = "outOfOffice",
    UnknownFutureValue = "unknownFutureValue",

