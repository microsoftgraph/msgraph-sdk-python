from enum import Enum

class Fido2RestrictionEnforcementType(str, Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

