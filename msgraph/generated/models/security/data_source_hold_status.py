from enum import Enum

class DataSourceHoldStatus(Enum):
    NotApplied = "notApplied",
    Applied = "applied",
    Applying = "applying",
    Removing = "removing",
    Partial = "partial",
    UnknownFutureValue = "unknownFutureValue",

