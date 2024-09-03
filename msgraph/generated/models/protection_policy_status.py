from enum import Enum

class ProtectionPolicyStatus(str, Enum):
    Inactive = "inactive",
    ActiveWithErrors = "activeWithErrors",
    Updating = "updating",
    Active = "active",
    UnknownFutureValue = "unknownFutureValue",

