from enum import Enum

class PrivilegedAccessGroupMemberType(str, Enum):
    Direct = "direct",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

