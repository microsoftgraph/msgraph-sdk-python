from enum import Enum

class AuthenticationStrengthRequirements(str, Enum):
    None_ = "none",
    Mfa = "mfa",
    UnknownFutureValue = "unknownFutureValue",

