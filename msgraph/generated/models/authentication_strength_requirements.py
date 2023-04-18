from enum import Enum

class AuthenticationStrengthRequirements(Enum):
    None_ = "none",
    Mfa = "mfa",
    UnknownFutureValue = "unknownFutureValue",

