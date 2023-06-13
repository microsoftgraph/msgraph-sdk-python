from enum import Enum

class StateManagementSetting(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Blocked.
    Blocked = "blocked",
    # Allowed.
    Allowed = "allowed",

