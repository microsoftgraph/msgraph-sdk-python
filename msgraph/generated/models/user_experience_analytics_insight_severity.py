from enum import Enum

class UserExperienceAnalyticsInsightSeverity(str, Enum):
    # Indicates that the insight severity is none.
    None_ = "none",
    # Indicates that the insight severity is informational.
    Informational = "informational",
    # Indicates that the insight severity is warning.
    Warning = "warning",
    # Indicates that the insight severity is error.
    Error = "error",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

