from enum import Enum

class OnlineMeetingRole(str, Enum):
    Attendee = "attendee",
    Presenter = "presenter",
    UnknownFutureValue = "unknownFutureValue",
    Producer = "producer",
    Coorganizer = "coorganizer",

