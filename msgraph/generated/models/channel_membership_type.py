from enum import Enum

class ChannelMembershipType(str, Enum):
    Standard = "standard",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",
    Shared = "shared",

