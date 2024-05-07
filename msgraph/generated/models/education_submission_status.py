from enum import Enum

class EducationSubmissionStatus(str, Enum):
    Working = "working",
    Submitted = "submitted",
    Released = "released",
    Returned = "returned",
    UnknownFutureValue = "unknownFutureValue",
    Reassigned = "reassigned",
    Excused = "excused",

