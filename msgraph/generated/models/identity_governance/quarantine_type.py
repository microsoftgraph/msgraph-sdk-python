from enum import Enum

class QuarantineType(str, Enum):
    NotQuarantined = "notQuarantined",
    CountBasedThresholdExceeded = "countBasedThresholdExceeded",
    PercentageBasedThresholdExceeded = "percentageBasedThresholdExceeded",
    MultipleConditionsExceeded = "multipleConditionsExceeded",
    UnknownFutureValue = "unknownFutureValue",

