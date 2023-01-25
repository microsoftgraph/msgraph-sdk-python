from enum import Enum

class DelegatedAdminRelationshipRequestStatus(Enum):
    Created = "created",
    Pending = "pending",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

