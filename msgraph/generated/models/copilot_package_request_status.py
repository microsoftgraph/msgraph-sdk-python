from enum import Enum

class CopilotPackageRequestStatus(str, Enum):
    # The request is awaiting a decision.
    Pending = "pending",
    # The request was approved.
    Approved = "approved",
    # The request was rejected.
    Rejected = "rejected",
    # An evolvable sentinel for future request statuses.
    UnknownFutureValue = "unknownFutureValue",

