from enum import Enum

class CloudPcDeviceImageOsStatus(str, Enum):
    Supported = "supported",
    SupportedWithWarning = "supportedWithWarning",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

