from enum import Enum

class MeetingRequestType(Enum):
    None_ = "none",
    NewMeetingRequest = "newMeetingRequest",
    FullUpdate = "fullUpdate",
    InformationalUpdate = "informationalUpdate",
    SilentUpdate = "silentUpdate",
    Outdated = "outdated",
    PrincipalWantsCopy = "principalWantsCopy",

