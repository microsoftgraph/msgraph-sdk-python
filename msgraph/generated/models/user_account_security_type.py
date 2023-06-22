from enum import Enum

class UserAccountSecurityType(str, Enum):
    Unknown = "unknown",
    Standard = "standard",
    Power = "power",
    Administrator = "administrator",
    UnknownFutureValue = "unknownFutureValue",

