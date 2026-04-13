from enum import Enum

class NumberCapability(str, Enum):
    ConferenceAssignment = "conferenceAssignment",
    VoiceApplicationAssignment = "voiceApplicationAssignment",
    UserAssignment = "userAssignment",
    TeamsPhoneMobile = "teamsPhoneMobile",
    UnknownFutureValue = "unknownFutureValue",

