from enum import Enum

class VirtualEventStatus(str, Enum):
    Draft = "draft",
    Published = "published",
    Canceled = "canceled",
    UnknownFutureValue = "unknownFutureValue",

