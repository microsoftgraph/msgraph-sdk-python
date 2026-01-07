from enum import Enum

class CloudPcOperatingSystem(str, Enum):
    Windows10 = "windows10",
    Windows11 = "windows11",
    UnknownFutureValue = "unknownFutureValue",

