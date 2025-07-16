from enum import Enum

class UnifiedRoleManagementPolicyRuleTargetOperations(str, Enum):
    All = "all",
    Activate = "activate",
    Deactivate = "deactivate",
    Assign = "assign",
    Update = "update",
    Remove = "remove",
    Extend = "extend",
    Renew = "renew",
    UnknownFutureValue = "unknownFutureValue",

