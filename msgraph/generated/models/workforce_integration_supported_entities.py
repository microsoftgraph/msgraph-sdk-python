from enum import Enum

class WorkforceIntegrationSupportedEntities(str, Enum):
    None_ = "none",
    Shift = "shift",
    SwapRequest = "swapRequest",
    UserShiftPreferences = "userShiftPreferences",
    OpenShift = "openShift",
    OpenShiftRequest = "openShiftRequest",
    OfferShiftRequest = "offerShiftRequest",
    UnknownFutureValue = "unknownFutureValue",
    TimeCard = "timeCard",
    TimeOffReason = "timeOffReason",
    TimeOff = "timeOff",
    TimeOffRequest = "timeOffRequest",

