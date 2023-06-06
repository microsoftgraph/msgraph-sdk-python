from enum import Enum

class ActivityDomain(str, Enum):
    Unknown = "unknown",
    Work = "work",
    Personal = "personal",
    Unrestricted = "unrestricted",

