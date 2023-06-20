from enum import Enum

class ComplianceStatus(str, Enum):
    Unknown = "unknown",
    NotApplicable = "notApplicable",
    Compliant = "compliant",
    Remediated = "remediated",
    NonCompliant = "nonCompliant",
    Error = "error",
    Conflict = "conflict",
    NotAssigned = "notAssigned",

