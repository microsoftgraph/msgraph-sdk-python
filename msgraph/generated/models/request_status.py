from enum import Enum

class RequestStatus(str, Enum):
    # Represents a governance request that is pending
    Pending = "pending",
    # Represents a governance request that was accepted
    Accepted = "accepted",
    # Represents a governance request that was rejected
    Rejected = "rejected",
    # This will help in making this enum evolable and adding more values in the future-
    UnknownFutureValue = "unknownFutureValue",

