from enum import Enum

class VirtualAppointmentMessageType(str, Enum):
    Confirmation = "confirmation",
    Reschedule = "reschedule",
    Cancellation = "cancellation",
    UnknownFutureValue = "unknownFutureValue",

