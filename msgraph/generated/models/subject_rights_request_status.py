from enum import Enum

class SubjectRightsRequestStatus(str, Enum):
    Active = "active",
    Closed = "closed",
    UnknownFutureValue = "unknownFutureValue",

