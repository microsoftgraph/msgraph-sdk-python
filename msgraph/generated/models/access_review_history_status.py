from enum import Enum

class AccessReviewHistoryStatus(Enum):
    Done = "done",
    Inprogress = "inprogress",
    Error = "error",
    Requested = "requested",
    UnknownFutureValue = "unknownFutureValue",

