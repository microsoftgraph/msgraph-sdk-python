from enum import Enum

class IncludedUserRoles(str, Enum):
    All = "all",
    PrivilegedAdmin = "privilegedAdmin",
    Admin = "admin",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

