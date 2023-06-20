from enum import Enum

class AuthenticationPhoneType(str, Enum):
    Mobile = "mobile",
    AlternateMobile = "alternateMobile",
    Office = "office",
    UnknownFutureValue = "unknownFutureValue",

