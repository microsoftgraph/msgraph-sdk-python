from enum import Enum

class TeamsAppPublishingState(Enum):
    Submitted = "submitted",
    Rejected = "rejected",
    Published = "published",
    UnknownFutureValue = "unknownFutureValue",

