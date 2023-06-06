from enum import Enum

class RecipientScopeType(str, Enum):
    None_ = "none",
    Internal = "internal",
    External = "external",
    ExternalPartner = "externalPartner",
    ExternalNonPartner = "externalNonPartner",

