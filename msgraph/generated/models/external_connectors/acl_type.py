from enum import Enum

class AclType(Enum):
    User = "user",
    Group = "group",
    Everyone = "everyone",
    EveryoneExceptGuests = "everyoneExceptGuests",
    ExternalGroup = "externalGroup",
    UnknownFutureValue = "unknownFutureValue",

