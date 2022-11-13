from enum import Enum

class CountryLookupMethodType(Enum):
    ClientIpAddress = "clientIpAddress",
    AuthenticatorAppGps = "authenticatorAppGps",
    UnknownFutureValue = "unknownFutureValue",

