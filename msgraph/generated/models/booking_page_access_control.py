from enum import Enum

class BookingPageAccessControl(str, Enum):
    Unrestricted = "unrestricted",
    RestrictedToOrganization = "restrictedToOrganization",
    UnknownFutureValue = "unknownFutureValue",

