from enum import Enum

class PrintEvent(str, Enum):
    JobStarted = "jobStarted",
    UnknownFutureValue = "unknownFutureValue",

