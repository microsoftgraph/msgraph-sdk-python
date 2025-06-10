from enum import Enum

class ServiceSource(str, Enum):
    Unknown = "unknown",
    MicrosoftDefenderForEndpoint = "microsoftDefenderForEndpoint",
    MicrosoftDefenderForIdentity = "microsoftDefenderForIdentity",
    MicrosoftDefenderForCloudApps = "microsoftDefenderForCloudApps",
    MicrosoftDefenderForOffice365 = "microsoftDefenderForOffice365",
    Microsoft365Defender = "microsoft365Defender",
    AzureAdIdentityProtection = "azureAdIdentityProtection",
    MicrosoftAppGovernance = "microsoftAppGovernance",
    DataLossPrevention = "dataLossPrevention",
    UnknownFutureValue = "unknownFutureValue",
    MicrosoftDefenderForCloud = "microsoftDefenderForCloud",
    MicrosoftSentinel = "microsoftSentinel",
    MicrosoftInsiderRiskManagement = "microsoftInsiderRiskManagement",
    MicrosoftThreatIntelligence = "microsoftThreatIntelligence",

