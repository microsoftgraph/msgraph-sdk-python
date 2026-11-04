from enum import Enum

class IsolationType(str, Enum):
    Full = "full",
    Selective = "selective",
    UnknownFutureValue = "unknownFutureValue",

