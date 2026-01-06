from enum import Enum

class WorkLocationUpdateScope(str, Enum):
    CurrentSegment = "currentSegment",
    CurrentDay = "currentDay",
    UnknownFutureValue = "unknownFutureValue",

