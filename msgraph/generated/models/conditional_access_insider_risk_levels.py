from enum import Enum

class ConditionalAccessInsiderRiskLevels(str, Enum):
    Minor = "minor",
    Moderate = "moderate",
    Elevated = "elevated",
    UnknownFutureValue = "unknownFutureValue",

