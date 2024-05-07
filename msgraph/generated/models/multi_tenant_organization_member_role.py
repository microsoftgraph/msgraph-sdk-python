from enum import Enum

class MultiTenantOrganizationMemberRole(str, Enum):
    Owner = "owner",
    Member = "member",
    UnknownFutureValue = "unknownFutureValue",

