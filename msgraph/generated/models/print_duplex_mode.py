from enum import Enum

class PrintDuplexMode(str, Enum):
    FlipOnLongEdge = "flipOnLongEdge",
    FlipOnShortEdge = "flipOnShortEdge",
    OneSided = "oneSided",
    UnknownFutureValue = "unknownFutureValue",

