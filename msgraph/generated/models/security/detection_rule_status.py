from enum import Enum

class DetectionRuleStatus(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    AutoDisabled = "autoDisabled",
    UnknownFutureValue = "unknownFutureValue",

