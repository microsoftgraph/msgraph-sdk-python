from enum import Enum

class AuthenticationMethodFeature(str, Enum):
    SsprRegistered = "ssprRegistered",
    SsprEnabled = "ssprEnabled",
    SsprCapable = "ssprCapable",
    PasswordlessCapable = "passwordlessCapable",
    MfaCapable = "mfaCapable",
    UnknownFutureValue = "unknownFutureValue",

