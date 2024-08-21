from enum import Enum

class DisableReason(str, Enum):
    None_ = "none",
    InvalidBillingProfile = "invalidBillingProfile",
    UserRequested = "userRequested",
    UnknownFutureValue = "unknownFutureValue",

