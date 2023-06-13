from enum import Enum

class AccessReviewHistoryStatus(str, Enum):
    Done = "done",
    Inprogress = "inprogress",
    Error = "error",
    Requested = "requested",
    UnknownFutureValue = "unknownFutureValue",

