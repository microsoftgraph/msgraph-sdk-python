from enum import Enum

class CustomerAction(str, Enum):
    LocationUpdate = "locationUpdate",
    Release = "release",
    UnknownFutureValue = "unknownFutureValue",

