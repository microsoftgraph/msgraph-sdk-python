from enum import Enum

class EducationSubmissionStatus(Enum):
    Working = "working",
    Submitted = "submitted",
    Released = "released",
    Returned = "returned",
    UnknownFutureValue = "unknownFutureValue",
    Reassigned = "reassigned",

