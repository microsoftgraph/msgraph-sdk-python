from enum import Enum

class SignInFrequencyAuthenticationType(Enum):
    PrimaryAndSecondaryAuthentication = "primaryAndSecondaryAuthentication",
    SecondaryAuthentication = "secondaryAuthentication",
    UnknownFutureValue = "unknownFutureValue",

