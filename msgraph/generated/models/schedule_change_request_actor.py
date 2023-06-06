from enum import Enum

class ScheduleChangeRequestActor(str, Enum):
    Sender = "sender",
    Recipient = "recipient",
    Manager = "manager",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

