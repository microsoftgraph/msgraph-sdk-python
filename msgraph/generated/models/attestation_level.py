from enum import Enum

class AttestationLevel(Enum):
    Attested = "attested",
    NotAttested = "notAttested",
    UnknownFutureValue = "unknownFutureValue",

