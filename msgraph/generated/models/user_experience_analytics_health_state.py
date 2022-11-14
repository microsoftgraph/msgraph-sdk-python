from enum import Enum

class UserExperienceAnalyticsHealthState(Enum):
    Unknown = "unknown",
    InsufficientData = "insufficientData",
    NeedsAttention = "needsAttention",
    MeetingGoals = "meetingGoals",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",

