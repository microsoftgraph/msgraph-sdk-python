from enum import Enum

class MeetingMessageType(Enum):
    None_ = "none",
    MeetingRequest = "meetingRequest",
    MeetingCancelled = "meetingCancelled",
    MeetingAccepted = "meetingAccepted",
    MeetingTenativelyAccepted = "meetingTenativelyAccepted",
    MeetingDeclined = "meetingDeclined",

