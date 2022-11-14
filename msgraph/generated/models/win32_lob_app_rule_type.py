from enum import Enum

class Win32LobAppRuleType(Enum):
    # Detection rule.
    Detection = "detection",
    # Requirement rule.
    Requirement = "requirement",

