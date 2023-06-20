from enum import Enum

class ChildSelectability(str, Enum):
    One = "One",
    Many = "Many",
    UnknownFutureValue = "unknownFutureValue",

