from enum import Enum

class IdentityProvider(str, Enum):
    EntraID = "entraID",
    ActiveDirectory = "activeDirectory",
    Okta = "okta",
    UnknownFutureValue = "unknownFutureValue",

