from enum import Enum

class VerifiedIdProfileState(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

