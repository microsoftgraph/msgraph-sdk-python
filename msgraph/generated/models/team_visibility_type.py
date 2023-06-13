from enum import Enum

class TeamVisibilityType(str, Enum):
    Private = "private",
    Public = "public",
    HiddenMembership = "hiddenMembership",
    UnknownFutureValue = "unknownFutureValue",

