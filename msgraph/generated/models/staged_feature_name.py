from enum import Enum

class StagedFeatureName(str, Enum):
    PassthroughAuthentication = "passthroughAuthentication",
    SeamlessSso = "seamlessSso",
    PasswordHashSync = "passwordHashSync",
    EmailAsAlternateId = "emailAsAlternateId",
    UnknownFutureValue = "unknownFutureValue",
    CertificateBasedAuthentication = "certificateBasedAuthentication",
    MultiFactorAuthentication = "multiFactorAuthentication",

