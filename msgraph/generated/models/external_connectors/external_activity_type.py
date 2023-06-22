from enum import Enum

class ExternalActivityType(str, Enum):
    Viewed = "viewed",
    Modified = "modified",
    Created = "created",
    Commented = "commented",
    UnknownFutureValue = "unknownFutureValue",

