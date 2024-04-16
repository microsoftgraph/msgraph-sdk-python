from enum import Enum

class B2bIdentityProvidersType(str, Enum):
    AzureActiveDirectory = "azureActiveDirectory",
    ExternalFederation = "externalFederation",
    SocialIdentityProviders = "socialIdentityProviders",
    EmailOneTimePasscode = "emailOneTimePasscode",
    MicrosoftAccount = "microsoftAccount",
    DefaultConfiguredIdp = "defaultConfiguredIdp",
    UnknownFutureValue = "unknownFutureValue",

