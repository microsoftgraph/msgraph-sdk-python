from enum import Enum

class AllowInvitesFrom(Enum):
    None_escaped = "none",
    AdminsAndGuestInviters = "adminsAndGuestInviters",
    AdminsGuestInvitersAndAllMembers = "adminsGuestInvitersAndAllMembers",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",

