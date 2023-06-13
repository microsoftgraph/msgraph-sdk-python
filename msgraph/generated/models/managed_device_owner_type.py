from enum import Enum

class ManagedDeviceOwnerType(str, Enum):
    # Unknown.
    Unknown = "unknown",
    # Owned by company.
    Company = "company",
    # Owned by person.
    Personal = "personal",

