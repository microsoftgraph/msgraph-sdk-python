from enum import Enum

class CommunityPrivacy(str, Enum):
    Public = "public",
    Private = "private",
    UnknownFutureValue = "unknownFutureValue",

