from enum import Enum

class ConditionalAccessPolicyState(str, Enum):
    Enabled = "enabled",
    Disabled = "disabled",
    EnabledForReportingButNotEnforced = "enabledForReportingButNotEnforced",

