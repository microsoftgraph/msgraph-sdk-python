from enum import Enum

class ExternalEmailOtpState(Enum):
    Default = "default",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

