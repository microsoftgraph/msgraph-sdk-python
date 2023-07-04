from enum import Enum

class UserExperienceAnalyticsHealthState(str, Enum):
    # Indicates that the health state is unknown.
    Unknown = "unknown",
    # Indicates that the health state is insufficient data.
    InsufficientData = "insufficientData",
    # Indicates that the health state needs attention.
    NeedsAttention = "needsAttention",
    # Indicates that the health state is meeting goals.
    MeetingGoals = "meetingGoals",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

