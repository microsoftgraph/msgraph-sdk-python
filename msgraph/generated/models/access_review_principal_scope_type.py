from enum import Enum

class AccessReviewPrincipalScopeType(str, Enum):
    AllUsers = "allUsers",
    GuestUsers = "guestUsers",
    InactiveUsers = "inactiveUsers",
    InactiveGuestUsers = "inactiveGuestUsers",
    UnknownFutureValue = "unknownFutureValue",

