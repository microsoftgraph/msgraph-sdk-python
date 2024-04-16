from enum import Enum

class ActionAfterRetentionPeriod(str, Enum):
    None_ = "none",
    Delete = "delete",
    StartDispositionReview = "startDispositionReview",
    Relabel = "relabel",
    UnknownFutureValue = "unknownFutureValue",

