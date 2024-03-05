from enum import Enum

class CloudPcAuditActivityOperationType(str, Enum):
    Create = "create",
    Delete = "delete",
    Patch = "patch",
    UnknownFutureValue = "unknownFutureValue",

