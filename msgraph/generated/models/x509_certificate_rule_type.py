from enum import Enum

class X509CertificateRuleType(str, Enum):
    IssuerSubject = "issuerSubject",
    PolicyOID = "policyOID",
    UnknownFutureValue = "unknownFutureValue",
    IssuerSubjectAndPolicyOID = "issuerSubjectAndPolicyOID",

