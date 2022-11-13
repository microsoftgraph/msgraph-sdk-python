from enum import Enum

class RecipientScopeType(Enum):
    None_escaped = "none",
    Internal = "internal",
    External = "external",
    ExternalPartner = "externalPartner",
    ExternalNonPartner = "externalNonPartner",

