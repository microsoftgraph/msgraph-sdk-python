from enum import Enum

class ConditionalAccessDevicePlatform(str, Enum):
    Android = "android",
    IOS = "iOS",
    Windows = "windows",
    WindowsPhone = "windowsPhone",
    MacOS = "macOS",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",
    Linux = "linux",

