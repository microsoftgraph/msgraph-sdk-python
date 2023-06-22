from enum import Enum

class AdvancedConfigState(str, Enum):
    Default = "default",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

