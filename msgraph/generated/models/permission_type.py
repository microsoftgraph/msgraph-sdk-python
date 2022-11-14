from enum import Enum

class PermissionType(Enum):
    Application = "application",
    Delegated = "delegated",
    DelegatedUserConsentable = "delegatedUserConsentable",

