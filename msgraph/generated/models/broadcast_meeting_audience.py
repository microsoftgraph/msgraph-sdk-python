from enum import Enum

class BroadcastMeetingAudience(str, Enum):
    RoleIsAttendee = "roleIsAttendee",
    Organization = "organization",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

