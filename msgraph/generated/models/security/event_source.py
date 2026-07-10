from enum import Enum

class EventSource(str, Enum):
    System = "system",
    Admin = "admin",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

