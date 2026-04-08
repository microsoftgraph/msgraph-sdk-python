from enum import Enum

class AssignmentStatus(str, Enum):
    Unassigned = "unassigned",
    InternalError = "internalError",
    UserAssigned = "userAssigned",
    ConferenceAssigned = "conferenceAssigned",
    VoiceApplicationAssigned = "voiceApplicationAssigned",
    ThirdPartyAppAssigned = "thirdPartyAppAssigned",
    PolicyAssigned = "policyAssigned",
    UnknownFutureValue = "unknownFutureValue",

