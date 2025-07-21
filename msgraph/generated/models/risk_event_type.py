from enum import Enum

class RiskEventType(str, Enum):
    UnlikelyTravel = "unlikelyTravel",
    AnonymizedIPAddress = "anonymizedIPAddress",
    MaliciousIPAddress = "maliciousIPAddress",
    UnfamiliarFeatures = "unfamiliarFeatures",
    MalwareInfectedIPAddress = "malwareInfectedIPAddress",
    SuspiciousIPAddress = "suspiciousIPAddress",
    LeakedCredentials = "leakedCredentials",
    InvestigationsThreatIntelligence = "investigationsThreatIntelligence",
    Generic = "generic",
    AdminConfirmedUserCompromised = "adminConfirmedUserCompromised",
    McasImpossibleTravel = "mcasImpossibleTravel",
    McasSuspiciousInboxManipulationRules = "mcasSuspiciousInboxManipulationRules",
    InvestigationsThreatIntelligenceSigninLinked = "investigationsThreatIntelligenceSigninLinked",
    MaliciousIPAddressValidCredentialsBlockedIP = "maliciousIPAddressValidCredentialsBlockedIP",
    UnknownFutureValue = "unknownFutureValue",

