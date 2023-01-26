from enum import Enum

class DelegatedAdminRelationshipRequestAction(Enum):
    LockForApproval = "lockForApproval",
    Approve = "approve",
    Terminate = "terminate",
    UnknownFutureValue = "unknownFutureValue",

