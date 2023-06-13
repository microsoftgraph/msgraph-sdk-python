from enum import Enum

class ExternalEmailOtpState(str, Enum):
    Default = "default",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

