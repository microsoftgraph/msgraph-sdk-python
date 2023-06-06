from enum import Enum

class SignInFrequencyAuthenticationType(str, Enum):
    PrimaryAndSecondaryAuthentication = "primaryAndSecondaryAuthentication",
    SecondaryAuthentication = "secondaryAuthentication",
    UnknownFutureValue = "unknownFutureValue",

