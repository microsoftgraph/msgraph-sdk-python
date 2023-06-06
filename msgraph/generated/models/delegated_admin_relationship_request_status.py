from enum import Enum

class DelegatedAdminRelationshipRequestStatus(str, Enum):
    Created = "created",
    Pending = "pending",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

