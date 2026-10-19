from enum import Enum

class CustomTaskExtensionReplyMode(str, Enum):
    None_ = "none",
    Callback = "callback",
    Response = "response",
    UnknownFutureValue = "unknownFutureValue",

