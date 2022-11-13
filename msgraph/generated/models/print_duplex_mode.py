from enum import Enum

class PrintDuplexMode(Enum):
    FlipOnLongEdge = "flipOnLongEdge",
    FlipOnShortEdge = "flipOnShortEdge",
    OneSided = "oneSided",
    UnknownFutureValue = "unknownFutureValue",

