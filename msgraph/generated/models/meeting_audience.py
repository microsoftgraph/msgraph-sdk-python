from enum import Enum

class MeetingAudience(str, Enum):
    Everyone = "everyone",
    Organization = "organization",
    UnknownFutureValue = "unknownFutureValue",

