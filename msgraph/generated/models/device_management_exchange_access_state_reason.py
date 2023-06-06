from enum import Enum

class DeviceManagementExchangeAccessStateReason(str, Enum):
    # No access state reason discovered from Exchange
    None_ = "none",
    # Unknown access state reason
    Unknown = "unknown",
    # Access state determined by Exchange Global rule
    ExchangeGlobalRule = "exchangeGlobalRule",
    # Access state determined by Exchange Individual rule
    ExchangeIndividualRule = "exchangeIndividualRule",
    # Access state determined by Exchange Device rule
    ExchangeDeviceRule = "exchangeDeviceRule",
    # Access state due to Exchange upgrade
    ExchangeUpgrade = "exchangeUpgrade",
    # Access state determined by Exchange Mailbox Policy
    ExchangeMailboxPolicy = "exchangeMailboxPolicy",
    # Access state determined by Exchange
    Other = "other",
    # Access state granted by compliance challenge
    Compliant = "compliant",
    # Access state revoked by compliance challenge
    NotCompliant = "notCompliant",
    # Access state revoked by management challenge
    NotEnrolled = "notEnrolled",
    # Access state due to unknown location
    UnknownLocation = "unknownLocation",
    # Access state due to MFA challenge
    MfaRequired = "mfaRequired",
    # Access State revoked by AAD Access Policy
    AzureADBlockDueToAccessPolicy = "azureADBlockDueToAccessPolicy",
    # Access State revoked by compromised password
    CompromisedPassword = "compromisedPassword",
    # Access state revoked by managed application challenge
    DeviceNotKnownWithManagedApp = "deviceNotKnownWithManagedApp",

