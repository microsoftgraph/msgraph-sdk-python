from enum import Enum

class ClaimBindingSource(str, Enum):
    Directory = "directory",
    UnknownFutureValue = "unknownFutureValue",

