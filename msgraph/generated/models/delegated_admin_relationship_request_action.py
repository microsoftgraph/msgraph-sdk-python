from enum import Enum

class DelegatedAdminRelationshipRequestAction(str, Enum):
    LockForApproval = "lockForApproval",
    Approve = "approve",
    Terminate = "terminate",
    UnknownFutureValue = "unknownFutureValue",
    Reject = "reject",

