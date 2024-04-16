from enum import Enum

class DefaultRecordBehavior(str, Enum):
    StartLocked = "startLocked",
    StartUnlocked = "startUnlocked",
    UnknownFutureValue = "unknownFutureValue",

