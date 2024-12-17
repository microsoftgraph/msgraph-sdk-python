from enum import Enum

class EligibilityFilteringEnabledEntities(str, Enum):
    None_ = "none",
    SwapRequest = "swapRequest",
    OfferShiftRequest = "offerShiftRequest",
    UnknownFutureValue = "unknownFutureValue",
    TimeOffReason = "timeOffReason",

