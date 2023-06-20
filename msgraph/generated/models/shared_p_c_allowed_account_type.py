from enum import Enum

class SharedPCAllowedAccountType(str, Enum):
    # Only guest accounts.
    Guest = "guest",
    # Only domain-joined accounts.
    Domain = "domain",

