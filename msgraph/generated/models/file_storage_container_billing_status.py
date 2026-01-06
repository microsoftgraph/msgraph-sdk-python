from enum import Enum

class FileStorageContainerBillingStatus(str, Enum):
    Invalid = "invalid",
    Valid = "valid",
    UnknownFutureValue = "unknownFutureValue",

