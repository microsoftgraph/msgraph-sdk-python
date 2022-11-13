from enum import Enum

class ManagedDeviceOwnerType(Enum):
    # Unknown.
    Unknown = "unknown",
    # Owned by company.
    Company = "company",
    # Owned by person.
    Personal = "personal",

