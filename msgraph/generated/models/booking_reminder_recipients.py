from enum import Enum

class BookingReminderRecipients(str, Enum):
    AllAttendees = "allAttendees",
    Staff = "staff",
    Customer = "customer",
    UnknownFutureValue = "unknownFutureValue",

