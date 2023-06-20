from enum import Enum

class AclType(str, Enum):
    User = "user",
    Group = "group",
    Everyone = "everyone",
    EveryoneExceptGuests = "everyoneExceptGuests",
    ExternalGroup = "externalGroup",
    UnknownFutureValue = "unknownFutureValue",

