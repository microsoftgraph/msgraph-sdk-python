from enum import Enum

class CrossTenantAccessPolicyTargetType(str, Enum):
    User = "user",
    Group = "group",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

