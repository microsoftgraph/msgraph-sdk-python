from enum import Enum

class SiteSecurityLevel(Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Low.
    Low = "low",
    # Medium-low.
    MediumLow = "mediumLow",
    # Medium.
    Medium = "medium",
    # Medium-high.
    MediumHigh = "mediumHigh",
    # High.
    High = "high",

