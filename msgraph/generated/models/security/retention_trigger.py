from enum import Enum

class RetentionTrigger(str, Enum):
    DateLabeled = "dateLabeled",
    DateCreated = "dateCreated",
    DateModified = "dateModified",
    DateOfEvent = "dateOfEvent",
    UnknownFutureValue = "unknownFutureValue",

