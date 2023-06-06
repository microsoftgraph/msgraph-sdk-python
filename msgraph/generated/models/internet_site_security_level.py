from enum import Enum

class InternetSiteSecurityLevel(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Medium.
    Medium = "medium",
    # Medium-High.
    MediumHigh = "mediumHigh",
    # High.
    High = "high",

