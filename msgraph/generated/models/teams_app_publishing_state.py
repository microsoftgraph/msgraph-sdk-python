from enum import Enum

class TeamsAppPublishingState(str, Enum):
    Submitted = "submitted",
    Rejected = "rejected",
    Published = "published",
    UnknownFutureValue = "unknownFutureValue",

