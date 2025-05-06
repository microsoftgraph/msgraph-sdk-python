from enum import Enum

class AuthenticationMethodPlatform(str, Enum):
    Unknown = "unknown",
    Windows = "windows",
    MacOS = "macOS",
    IOS = "iOS",
    Android = "android",
    Linux = "linux",
    UnknownFutureValue = "unknownFutureValue",

