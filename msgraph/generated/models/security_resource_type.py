from enum import Enum

class SecurityResourceType(str, Enum):
    Unknown = "unknown",
    Attacked = "attacked",
    Related = "related",
    UnknownFutureValue = "unknownFutureValue",

