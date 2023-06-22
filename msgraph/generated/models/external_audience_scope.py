from enum import Enum

class ExternalAudienceScope(str, Enum):
    None_ = "none",
    ContactsOnly = "contactsOnly",
    All = "all",

