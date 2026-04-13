from enum import Enum

class PasskeyTypes(str, Enum):
    DeviceBound = "deviceBound",
    Synced = "synced",
    UnknownFutureValue = "unknownFutureValue",

