from enum import Enum

class CertificateAuthorityType(str, Enum):
    Root = "root",
    Intermediate = "intermediate",
    UnknownFutureValue = "unknownFutureValue",

