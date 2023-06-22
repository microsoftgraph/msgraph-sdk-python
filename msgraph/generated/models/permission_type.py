from enum import Enum

class PermissionType(str, Enum):
    Application = "application",
    Delegated = "delegated",
    DelegatedUserConsentable = "delegatedUserConsentable",

