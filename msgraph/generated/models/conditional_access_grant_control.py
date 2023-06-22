from enum import Enum

class ConditionalAccessGrantControl(str, Enum):
    Block = "block",
    Mfa = "mfa",
    CompliantDevice = "compliantDevice",
    DomainJoinedDevice = "domainJoinedDevice",
    ApprovedApplication = "approvedApplication",
    CompliantApplication = "compliantApplication",
    PasswordChange = "passwordChange",
    UnknownFutureValue = "unknownFutureValue",

