from enum import Enum

class MultiTenantOrganizationMemberState(str, Enum):
    Pending = "pending",
    Active = "active",
    Removed = "removed",
    UnknownFutureValue = "unknownFutureValue",

