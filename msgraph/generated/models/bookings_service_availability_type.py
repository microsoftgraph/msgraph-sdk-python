from enum import Enum

class BookingsServiceAvailabilityType(str, Enum):
    BookWhenStaffAreFree = "bookWhenStaffAreFree",
    NotBookable = "notBookable",
    CustomWeeklyHours = "customWeeklyHours",
    UnknownFutureValue = "unknownFutureValue",

