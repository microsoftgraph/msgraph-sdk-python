from enum import Enum

class AuthenticationMethodSignInState(Enum):
    NotSupported = "notSupported",
    NotAllowedByPolicy = "notAllowedByPolicy",
    NotEnabled = "notEnabled",
    PhoneNumberNotUnique = "phoneNumberNotUnique",
    Ready = "ready",
    NotConfigured = "notConfigured",
    UnknownFutureValue = "unknownFutureValue",

