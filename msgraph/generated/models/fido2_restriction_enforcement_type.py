from enum import Enum

class Fido2RestrictionEnforcementType(Enum):
    Allow = "allow",
    Block = "block",
    UnknownFutureValue = "unknownFutureValue",

