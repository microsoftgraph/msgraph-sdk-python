from enum import Enum

class StateManagementSetting(Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Blocked.
    Blocked = "blocked",
    # Allowed.
    Allowed = "allowed",

