from enum import Enum

class MatchConfidenceLevel(str, Enum):
    Exact = "exact",
    Relaxed = "relaxed",
    UnknownFutureValue = "unknownFutureValue",

