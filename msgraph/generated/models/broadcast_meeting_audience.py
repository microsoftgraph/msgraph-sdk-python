from enum import Enum

class BroadcastMeetingAudience(Enum):
    RoleIsAttendee = "roleIsAttendee",
    Organization = "organization",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

