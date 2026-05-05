from enum import Enum

class NotifyMembers(str, Enum):
    All = "all",
    AllowSelected = "allowSelected",
    BlockSelected = "blockSelected",
    UnknownFutureValue = "unknownFutureValue",

