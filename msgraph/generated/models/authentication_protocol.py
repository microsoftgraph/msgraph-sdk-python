from enum import Enum

class AuthenticationProtocol(str, Enum):
    WsFed = "wsFed",
    Saml = "saml",
    UnknownFutureValue = "unknownFutureValue",

