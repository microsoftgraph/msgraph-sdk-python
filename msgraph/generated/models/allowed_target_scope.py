from enum import Enum

class AllowedTargetScope(str, Enum):
    NotSpecified = "notSpecified",
    SpecificDirectoryUsers = "specificDirectoryUsers",
    SpecificConnectedOrganizationUsers = "specificConnectedOrganizationUsers",
    SpecificDirectoryServicePrincipals = "specificDirectoryServicePrincipals",
    AllMemberUsers = "allMemberUsers",
    AllDirectoryUsers = "allDirectoryUsers",
    AllDirectoryServicePrincipals = "allDirectoryServicePrincipals",
    AllConfiguredConnectedOrganizationUsers = "allConfiguredConnectedOrganizationUsers",
    AllExternalUsers = "allExternalUsers",
    AllDirectoryAgentIdentities = "allDirectoryAgentIdentities",
    UnknownFutureValue = "unknownFutureValue",

