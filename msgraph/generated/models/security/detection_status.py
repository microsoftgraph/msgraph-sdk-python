from enum import Enum

class DetectionStatus(Enum):
    Detected = "detected",
    Blocked = "blocked",
    Prevented = "prevented",
    UnknownFutureValue = "unknownFutureValue",

