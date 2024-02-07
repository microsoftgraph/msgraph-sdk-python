from enum import Enum

class PermissionType(str, Enum):
    DelegatedUserConsentable = "delegatedUserConsentable",
    Delegated = "delegated",
    Application = "application",

