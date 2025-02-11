from enum import Enum

class TimeCardState(str, Enum):
    ClockedIn = "clockedIn",
    OnBreak = "onBreak",
    ClockedOut = "clockedOut",
    UnknownFutureValue = "unknownFutureValue",

