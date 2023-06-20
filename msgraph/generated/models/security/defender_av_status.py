from enum import Enum

class DefenderAvStatus(str, Enum):
    NotReporting = "notReporting",
    Disabled = "disabled",
    NotUpdated = "notUpdated",
    Updated = "updated",
    Unknown = "unknown",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

