from enum import Enum

class AllowInvitesFrom(str, Enum):
    None_ = "none",
    AdminsAndGuestInviters = "adminsAndGuestInviters",
    AdminsGuestInvitersAndAllMembers = "adminsGuestInvitersAndAllMembers",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

