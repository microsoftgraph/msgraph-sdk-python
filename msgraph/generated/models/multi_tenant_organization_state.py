from enum import Enum

class MultiTenantOrganizationState(str, Enum):
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

