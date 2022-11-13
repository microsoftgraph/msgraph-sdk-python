from enum import Enum

class AuthenticationProtocol(Enum):
    WsFed = "wsFed",
    Saml = "saml",
    UnknownFutureValue = "unknownFutureValue",

