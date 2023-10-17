from enum import Enum

class PrivilegedAccessGroupRelationships(str, Enum):
    Owner = "owner",
    Member = "member",
    UnknownFutureValue = "unknownFutureValue",

