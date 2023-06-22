from enum import Enum

class DefenderScanType(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # System scan disabled.
    Disabled = "disabled",
    # Quick system scan.
    Quick = "quick",
    # Full system scan.
    Full = "full",

