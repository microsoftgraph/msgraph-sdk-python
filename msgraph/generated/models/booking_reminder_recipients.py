from enum import Enum

class BookingReminderRecipients(Enum):
    AllAttendees = "allAttendees",
    Staff = "staff",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

