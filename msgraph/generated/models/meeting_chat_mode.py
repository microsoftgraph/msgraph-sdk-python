from enum import Enum

class MeetingChatMode(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    Limited = "limited",
    UnknownFutureValue = "unknownFutureValue",

