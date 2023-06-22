from enum import Enum

class AppKeyCredentialRestrictionType(str, Enum):
    AsymmetricKeyLifetime = "asymmetricKeyLifetime",
    UnknownFutureValue = "unknownFutureValue",

