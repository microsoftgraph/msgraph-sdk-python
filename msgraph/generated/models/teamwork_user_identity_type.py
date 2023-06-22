from enum import Enum

class TeamworkUserIdentityType(str, Enum):
    AadUser = "aadUser",
    OnPremiseAadUser = "onPremiseAadUser",
    AnonymousGuest = "anonymousGuest",
    FederatedUser = "federatedUser",
    PersonalMicrosoftAccountUser = "personalMicrosoftAccountUser",
    SkypeUser = "skypeUser",
    PhoneUser = "phoneUser",
    UnknownFutureValue = "unknownFutureValue",
    EmailUser = "emailUser",

