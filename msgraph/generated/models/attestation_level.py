from enum import Enum

class AttestationLevel(str, Enum):
    Attested = "attested",
    NotAttested = "notAttested",
    UnknownFutureValue = "unknownFutureValue",

