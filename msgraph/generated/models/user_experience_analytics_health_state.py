from enum import Enum

class UserExperienceAnalyticsHealthState(str, Enum):
    Unknown = "unknown",
    InsufficientData = "insufficientData",
    NeedsAttention = "needsAttention",
    MeetingGoals = "meetingGoals",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",

