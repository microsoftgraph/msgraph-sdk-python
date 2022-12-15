from enum import Enum

class DetectionSource(Enum):
    Unknown = "unknown",
    MicrosoftDefenderForEndpoint = "microsoftDefenderForEndpoint",
    Antivirus = "antivirus",
    SmartScreen = "smartScreen",
    CustomTi = "customTi",
    MicrosoftDefenderForOffice365 = "microsoftDefenderForOffice365",
    AutomatedInvestigation = "automatedInvestigation",
    MicrosoftThreatExperts = "microsoftThreatExperts",
    CustomDetection = "customDetection",
    MicrosoftDefenderForIdentity = "microsoftDefenderForIdentity",
    CloudAppSecurity = "cloudAppSecurity",
    Microsoft365Defender = "microsoft365Defender",
    AzureAdIdentityProtection = "azureAdIdentityProtection",
    Manual = "manual",
    MicrosoftDataLossPrevention = "microsoftDataLossPrevention",
    AppGovernancePolicy = "appGovernancePolicy",
    AppGovernanceDetection = "appGovernanceDetection",
    UnknownFutureValue = "unknownFutureValue",

