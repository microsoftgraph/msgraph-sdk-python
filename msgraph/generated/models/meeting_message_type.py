from enum import Enum

class MeetingMessageType(Enum):
    None_escaped = "none",
    MeetingRequest = "meetingRequest",
    MeetingCancelled = "meetingCancelled",
    MeetingAccepted = "meetingAccepted",
    MeetingTenativelyAccepted = "meetingTenativelyAccepted",
    MeetingDeclined = "meetingDeclined",

