from enum import Enum

class InsiderRiskLevel(str, Enum):
    None_ = "none",
    Minor = "minor",
    Moderate = "moderate",
    Elevated = "elevated",
    UnknownFutureValue = "unknownFutureValue",

