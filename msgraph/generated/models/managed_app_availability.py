from enum import Enum

class ManagedAppAvailability(Enum):
    # A globally available app to all tenants.
    Global_ = "global",
    # A line of business apps private to an organization.
    LineOfBusiness = "lineOfBusiness",

