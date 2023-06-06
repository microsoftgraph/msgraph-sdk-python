from enum import Enum

class CountryLookupMethodType(str, Enum):
    ClientIpAddress = "clientIpAddress",
    AuthenticatorAppGps = "authenticatorAppGps",
    UnknownFutureValue = "unknownFutureValue",

