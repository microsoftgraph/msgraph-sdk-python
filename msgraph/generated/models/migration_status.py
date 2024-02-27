from enum import Enum

class MigrationStatus(str, Enum):
    Ready = "ready",
    NeedsReview = "needsReview",
    AdditionalStepsRequired = "additionalStepsRequired",
    UnknownFutureValue = "unknownFutureValue",

