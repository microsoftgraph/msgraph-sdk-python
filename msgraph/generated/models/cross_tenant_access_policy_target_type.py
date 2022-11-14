from enum import Enum

class CrossTenantAccessPolicyTargetType(Enum):
    User = "user",
    Group = "group",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

