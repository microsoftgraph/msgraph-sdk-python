from enum import Enum

class ServiceSource(Enum):
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

