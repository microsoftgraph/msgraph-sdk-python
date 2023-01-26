from enum import Enum

class DelegatedAdminAccessAssignmentStatus(Enum):
    Pending = "pending",
    Active = "active",
    Deleting = "deleting",
    Deleted = "deleted",
    Error = "error",
    UnknownFutureValue = "unknownFutureValue",

