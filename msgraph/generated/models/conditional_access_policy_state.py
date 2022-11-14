from enum import Enum

class ConditionalAccessPolicyState(Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    EnabledForReportingButNotEnforced = "enabledForReportingButNotEnforced",

