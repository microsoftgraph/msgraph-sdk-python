from enum import Enum

class CloudPcDeviceImageStatus(str, Enum):
    Pending = "pending",
    Ready = "ready",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

