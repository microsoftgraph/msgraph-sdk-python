from enum import Enum

class ManagementAgentType(str, Enum):
    # The device is managed by Exchange server.
    Eas = "eas",
    # The device is managed by Intune MDM.
    Mdm = "mdm",
    # The device is managed by both Exchange server and Intune MDM.
    EasMdm = "easMdm",
    # Intune client managed.
    IntuneClient = "intuneClient",
    # The device is EAS and Intune client dual managed.
    EasIntuneClient = "easIntuneClient",
    # The device is managed by Configuration Manager.
    ConfigurationManagerClient = "configurationManagerClient",
    # The device is managed by Configuration Manager and MDM.
    ConfigurationManagerClientMdm = "configurationManagerClientMdm",
    # The device is managed by Configuration Manager, MDM and Eas.
    ConfigurationManagerClientMdmEas = "configurationManagerClientMdmEas",
    # Unknown management agent type.
    Unknown = "unknown",
    # The device attributes are fetched from Jamf.
    Jamf = "jamf",
    # The device is managed by Google's CloudDPC.
    GoogleCloudDevicePolicyController = "googleCloudDevicePolicyController",
    # This device is managed by Microsoft 365 through Intune.
    Microsoft365ManagedMdm = "microsoft365ManagedMdm",
    MsSense = "msSense",

