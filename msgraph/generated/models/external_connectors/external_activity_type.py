from enum import Enum

class ExternalActivityType(Enum):
    Viewed = "viewed",
    Modified = "modified",
    Created = "created",
    Commented = "commented",
    UnknownFutureValue = "unknownFutureValue",

