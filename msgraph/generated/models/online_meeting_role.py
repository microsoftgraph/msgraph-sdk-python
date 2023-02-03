from enum import Enum

class OnlineMeetingRole(Enum):
    Attendee = "attendee",
    Presenter = "presenter",
    UnknownFutureValue = "unknownFutureValue",
    Producer = "producer",
    Coorganizer = "coorganizer",

