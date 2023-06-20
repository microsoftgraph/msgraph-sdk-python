from enum import Enum

class AuthenticationMethodKeyStrength(str, Enum):
    Normal = "normal",
    Weak = "weak",
    Unknown = "unknown",

