from enum import Enum

class ConditionalAccessTransferMethods(str, Enum):
    None_ = "none",
    DeviceCodeFlow = "deviceCodeFlow",
    AuthenticationTransfer = "authenticationTransfer",
    UnknownFutureValue = "unknownFutureValue",

