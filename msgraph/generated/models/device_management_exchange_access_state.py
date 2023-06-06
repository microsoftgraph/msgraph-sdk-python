from enum import Enum

class DeviceManagementExchangeAccessState(str, Enum):
    # No access state discovered from Exchange
    None_ = "none",
    # Device access state to Exchange is unknown
    Unknown = "unknown",
    # Device has access to Exchange
    Allowed = "allowed",
    # Device is Blocked in Exchange
    Blocked = "blocked",
    # Device is Quarantined in Exchange
    Quarantined = "quarantined",

