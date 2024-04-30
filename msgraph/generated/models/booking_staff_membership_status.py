from enum import Enum

class BookingStaffMembershipStatus(str, Enum):
    Active = "active",
    PendingAcceptance = "pendingAcceptance",
    RejectedByStaff = "rejectedByStaff",
    UnknownFutureValue = "unknownFutureValue",

