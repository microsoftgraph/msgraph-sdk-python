from enum import Enum

class MatchMode(str, Enum):
    Any = "any",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

