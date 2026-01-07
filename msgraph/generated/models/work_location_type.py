from enum import Enum

class WorkLocationType(str, Enum):
    Unspecified = "unspecified",
    Office = "office",
    Remote = "remote",
    TimeOff = "timeOff",
    UnknownFutureValue = "unknownFutureValue",

