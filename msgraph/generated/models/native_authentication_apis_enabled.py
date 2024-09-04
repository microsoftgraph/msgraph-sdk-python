from enum import Enum

class NativeAuthenticationApisEnabled(str, Enum):
    None_ = "none",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

