from enum import Enum

class ManagedDeviceOwnerType(str, Enum):
    # Unknown device owner type.
    Unknown = "unknown",
    # Corporate device owner type.
    Company = "company",
    # Personal device owner type.
    Personal = "personal",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

