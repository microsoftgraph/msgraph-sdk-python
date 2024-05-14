from enum import Enum

class HealthIssueType(str, Enum):
    Sensor = "sensor",
    Global_ = "global",
    UnknownFutureValue = "unknownFutureValue",

