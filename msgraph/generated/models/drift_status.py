from enum import Enum

class DriftStatus(str, Enum):
    Active = "active",
    Fixed = "fixed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

