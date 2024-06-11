from enum import Enum

class WindowsDeviceUsageType(str, Enum):
    # Default. Indicates that a device is a single-user device.
    SingleUser = "singleUser",
    # Indicates that a device is a multi-user device.
    Shared = "shared",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

