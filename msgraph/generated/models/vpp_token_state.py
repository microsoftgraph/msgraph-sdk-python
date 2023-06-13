from enum import Enum

class VppTokenState(str, Enum):
    # Default state.
    Unknown = "unknown",
    # Token is valid.
    Valid = "valid",
    # Token is expired.
    Expired = "expired",
    # Token is invalid.
    Invalid = "invalid",
    # Token is managed by another MDM Service.
    AssignedToExternalMDM = "assignedToExternalMDM",

