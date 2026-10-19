from enum import Enum

class AccessReviewReviewerScopeType(str, Enum):
    User = "user",
    Group = "group",
    Self = "self",
    Manager = "manager",
    Sponsor = "sponsor",
    ResourceOwner = "resourceOwner",
    ManagerOrSponsor = "managerOrSponsor",
    UnknownFutureValue = "unknownFutureValue",

