from enum import Enum

class IoTDeviceImportanceType(str, Enum):
    Unknown = "unknown",
    Low = "low",
    Normal = "normal",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

