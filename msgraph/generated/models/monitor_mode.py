from enum import Enum

class MonitorMode(str, Enum):
    MonitorOnly = "monitorOnly",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

