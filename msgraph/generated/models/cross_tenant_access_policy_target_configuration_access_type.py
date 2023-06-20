from enum import Enum

class CrossTenantAccessPolicyTargetConfigurationAccessType(str, Enum):
    Allowed = "allowed",
    Blocked = "blocked",
    UnknownFutureValue = "unknownFutureValue",

