from enum import Enum

class MobileThreatPartnerTenantState(Enum):
    # Partner is unavailable.
    Unavailable = "unavailable",
    # Partner is available.
    Available = "available",
    # Partner is enabled.
    Enabled = "enabled",
    # Partner is unresponsive.
    Unresponsive = "unresponsive",

