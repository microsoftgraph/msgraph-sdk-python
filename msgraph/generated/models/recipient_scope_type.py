from enum import Enum

class RecipientScopeType(Enum):
    None_ = "none",
    Internal = "internal",
    External = "external",
    ExternalPartner = "externalPartner",
    ExternalNonPartner = "externalNonPartner",

