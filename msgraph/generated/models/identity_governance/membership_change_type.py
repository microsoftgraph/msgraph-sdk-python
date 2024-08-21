from enum import Enum

class MembershipChangeType(str, Enum):
    Add = "add",
    Remove = "remove",
    UnknownFutureValue = "unknownFutureValue",

