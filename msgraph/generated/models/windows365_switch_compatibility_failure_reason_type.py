from enum import Enum

class Windows365SwitchCompatibilityFailureReasonType(str, Enum):
    OsVersionNotSupported = "osVersionNotSupported",
    HardwareNotSupported = "hardwareNotSupported",
    UnknownFutureValue = "unknownFutureValue",

