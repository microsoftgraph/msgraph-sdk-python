from enum import Enum

class ScheduleChangeRequestActor(Enum):
    Sender = "sender",
    Recipient = "recipient",
    Manager = "manager",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

