from enum import Enum

class MultiTenantOrganizationMemberProcessingStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

