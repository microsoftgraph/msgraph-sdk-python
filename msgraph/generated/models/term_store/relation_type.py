from enum import Enum

class RelationType(str, Enum):
    Pin = "pin",
    Reuse = "reuse",
    UnknownFutureValue = "unknownFutureValue",

