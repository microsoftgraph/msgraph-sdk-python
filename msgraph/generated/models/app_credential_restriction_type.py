from enum import Enum

class AppCredentialRestrictionType(Enum):
    PasswordAddition = "passwordAddition",
    PasswordLifetime = "passwordLifetime",
    SymmetricKeyAddition = "symmetricKeyAddition",
    SymmetricKeyLifetime = "symmetricKeyLifetime",
    CustomPasswordAddition = "customPasswordAddition",
    UnknownFutureValue = "unknownFutureValue",

