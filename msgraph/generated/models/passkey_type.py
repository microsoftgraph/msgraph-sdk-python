from enum import Enum

class PasskeyType(str, Enum):
    DeviceBound = "deviceBound",
    Synced = "synced",
    UnknownFutureValue = "unknownFutureValue",

