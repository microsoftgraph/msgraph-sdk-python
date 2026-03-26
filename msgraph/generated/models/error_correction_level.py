from enum import Enum

class ErrorCorrectionLevel(str, Enum):
    L = "l",
    M = "m",
    Q = "q",
    H = "h",
    UnknownFutureValue = "unknownFutureValue",

