from enum import Enum

class CustomExtensionCalloutInstanceStatus(str, Enum):
    CalloutSent = "calloutSent",
    CallbackReceived = "callbackReceived",
    CalloutFailed = "calloutFailed",
    CallbackTimedOut = "callbackTimedOut",
    WaitingForCallback = "waitingForCallback",
    UnknownFutureValue = "unknownFutureValue",

