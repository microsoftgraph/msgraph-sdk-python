from enum import Enum

class DestinationType(str, Enum):
    New = "new",
    InPlace = "inPlace",
    UnknownFutureValue = "unknownFutureValue",

