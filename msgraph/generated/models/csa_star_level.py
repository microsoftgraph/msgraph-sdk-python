from enum import Enum

class CsaStarLevel(str, Enum):
    None_ = "none",
    Attestation = "attestation",
    Certification = "certification",
    ContinuousMonitoring = "continuousMonitoring",
    CStarAssessment = "cStarAssessment",
    SelfAssessment = "selfAssessment",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

