from enum import Enum

class RestrictionAction(str, Enum):
    Warn = "warn",
    Audit = "audit",
    Block = "block",

