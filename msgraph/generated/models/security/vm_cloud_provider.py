from enum import Enum

class VmCloudProvider(str, Enum):
    Unknown = "unknown",
    Azure = "azure",
    UnknownFutureValue = "unknownFutureValue",

