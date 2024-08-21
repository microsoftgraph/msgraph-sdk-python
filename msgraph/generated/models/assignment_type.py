from enum import Enum

class AssignmentType(str, Enum):
    Required = "required",
    Recommended = "recommended",
    UnknownFutureValue = "unknownFutureValue",
    PeerRecommended = "peerRecommended",

