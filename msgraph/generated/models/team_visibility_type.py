from enum import Enum

class TeamVisibilityType(Enum):
    Private = "private",
    Public = "public",
    HiddenMembership = "hiddenMembership",
    UnknownFutureValue = "unknownFutureValue",

