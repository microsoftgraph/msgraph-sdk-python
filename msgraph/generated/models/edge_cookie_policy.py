from enum import Enum

class EdgeCookiePolicy(str, Enum):
    # Allow the user to set.
    UserDefined = "userDefined",
    # Allow.
    Allow = "allow",
    # Block only third party cookies.
    BlockThirdParty = "blockThirdParty",
    # Block all cookies.
    BlockAll = "blockAll",

