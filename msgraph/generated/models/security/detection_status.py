from enum import Enum

class DetectionStatus(str, Enum):
    Detected = "detected",
    Blocked = "blocked",
    Prevented = "prevented",
    UnknownFutureValue = "unknownFutureValue",

