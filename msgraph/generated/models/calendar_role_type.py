from enum import Enum

class CalendarRoleType(str, Enum):
    None_ = "none",
    FreeBusyRead = "freeBusyRead",
    LimitedRead = "limitedRead",
    Read = "read",
    Write = "write",
    DelegateWithoutPrivateEventAccess = "delegateWithoutPrivateEventAccess",
    DelegateWithPrivateEventAccess = "delegateWithPrivateEventAccess",
    Custom = "custom",

