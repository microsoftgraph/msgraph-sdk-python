from enum import Enum

class SystemBrowserEnabledOn(str, Enum):
    None_ = "none",
    Ios = "ios",
    Android = "android",
    Mac = "mac",
    Linux = "linux",
    UnknownFutureValue = "unknownFutureValue",

