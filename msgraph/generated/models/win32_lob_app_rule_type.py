from enum import Enum

class Win32LobAppRuleType(str, Enum):
    # Detection rule.
    Detection = "detection",
    # Requirement rule.
    Requirement = "requirement",

