from enum import Enum

class WorkforceIntegrationSupportedEntities(Enum):
    None_escaped = "none",
    Shift = "shift",
    SwapRequest = "swapRequest",
    UserShiftPreferences = "userShiftPreferences",
    OpenShift = "openShift",
    OpenShiftRequest = "openShiftRequest",
    OfferShiftRequest = "offerShiftRequest",
    UnknownFutureValue = "unknownFutureValue",

