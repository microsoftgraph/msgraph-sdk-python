from enum import Enum

class RelationshipStatus(str, Enum):
    # Represents a relationship that is currently active.
    Active = "active",
    # Represents a relationship that has been terminated.
    Terminated = "terminated",
    # Represents a relationship that has been requested to be terminated by governing tenant.
    TerminationRequestedByGoverningTenant = "terminationRequestedByGoverningTenant",
    # This will help in making this enum evolable and adding more values in the future-
    UnknownFutureValue = "unknownFutureValue",

