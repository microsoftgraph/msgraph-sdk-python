from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .managed_app_policy import ManagedAppPolicy
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
    from .windows_information_protection_app import WindowsInformationProtectionApp
    from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
    from .windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
    from .windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
    from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy
    from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
    from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection

from .managed_app_policy import ManagedAppPolicy

@dataclass
class WindowsInformationProtection(ManagedAppPolicy):
    """
    Policy for Windows information protection to configure detailed management settings
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsInformationProtection"
    # Navigation property to list of security groups targeted for policy.
    assignments: Optional[List[TargetedManagedAppPolicyAssignment]] = None
    # Specifies whether to allow Azure RMS encryption for WIP
    azure_rights_management_services_allowed: Optional[bool] = None
    # Specifies a recovery certificate that can be used for data recovery of encrypted files. This is the same as the data recovery agent(DRA) certificate for encrypting file system(EFS)
    data_recovery_certificate: Optional[WindowsInformationProtectionDataRecoveryCertificate] = None
    # Possible values for WIP Protection enforcement levels
    enforcement_level: Optional[WindowsInformationProtectionEnforcementLevel] = None
    # Primary enterprise domain
    enterprise_domain: Optional[str] = None
    # Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to
    enterprise_i_p_ranges: Optional[List[WindowsInformationProtectionIPRangeCollection]] = None
    # Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false
    enterprise_i_p_ranges_are_authoritative: Optional[bool] = None
    # This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies
    enterprise_internal_proxy_servers: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    # This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to
    enterprise_network_domain_names: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    # List of enterprise domains to be protected
    enterprise_protected_domain_names: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    # Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy
    enterprise_proxied_domains: Optional[List[WindowsInformationProtectionProxiedDomainCollection]] = None
    # This is a list of proxy servers. Any server not on this list is considered non-enterprise
    enterprise_proxy_servers: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    # Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
    enterprise_proxy_servers_are_authoritative: Optional[bool] = None
    # Another way to input exempt apps through xml files
    exempt_app_locker_files: Optional[List[WindowsInformationProtectionAppLockerFile]] = None
    # Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.
    exempt_apps: Optional[List[WindowsInformationProtectionApp]] = None
    # Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app
    icons_visible: Optional[bool] = None
    # This switch is for the Windows Search Indexer, to allow or disallow indexing of items
    indexing_encrypted_stores_or_items_blocked: Optional[bool] = None
    # Indicates if the policy is deployed to any inclusion groups or not.
    is_assigned: Optional[bool] = None
    # List of domain names that can used for work or personal resource
    neutral_domain_resources: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    # Another way to input protected apps through xml files
    protected_app_locker_files: Optional[List[WindowsInformationProtectionAppLockerFile]] = None
    # Protected applications can access enterprise data and the data handled by those applications are protected with encryption
    protected_apps: Optional[List[WindowsInformationProtectionApp]] = None
    # Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured
    protection_under_lock_config_required: Optional[bool] = None
    # This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.
    revoke_on_unenroll_disabled: Optional[bool] = None
    # TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access
    rights_management_services_template_id: Optional[UUID] = None
    # Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary
    smb_auto_encrypted_file_extensions: Optional[List[WindowsInformationProtectionResourceCollection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicy".casefold():
            from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

            return MdmWindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionPolicy".casefold():
            from .windows_information_protection_policy import WindowsInformationProtectionPolicy

            return WindowsInformationProtectionPolicy()
        return WindowsInformationProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_policy import ManagedAppPolicy
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .windows_information_protection_app import WindowsInformationProtectionApp
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
        from .windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
        from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
        from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection

        from .managed_app_policy import ManagedAppPolicy
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .windows_information_protection_app import WindowsInformationProtectionApp
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_data_recovery_certificate import WindowsInformationProtectionDataRecoveryCertificate
        from .windows_information_protection_enforcement_level import WindowsInformationProtectionEnforcementLevel
        from .windows_information_protection_i_p_range_collection import WindowsInformationProtectionIPRangeCollection
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_information_protection_proxied_domain_collection import WindowsInformationProtectionProxiedDomainCollection
        from .windows_information_protection_resource_collection import WindowsInformationProtectionResourceCollection

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TargetedManagedAppPolicyAssignment)),
            "azure_rights_management_services_allowed": lambda n : setattr(self, 'azure_rights_management_services_allowed', n.get_bool_value()),
            "data_recovery_certificate": lambda n : setattr(self, 'data_recovery_certificate', n.get_object_value(WindowsInformationProtectionDataRecoveryCertificate)),
            "enforcement_level": lambda n : setattr(self, 'enforcement_level', n.get_enum_value(WindowsInformationProtectionEnforcementLevel)),
            "enterprise_domain": lambda n : setattr(self, 'enterprise_domain', n.get_str_value()),
            "enterprise_i_p_ranges": lambda n : setattr(self, 'enterprise_i_p_ranges', n.get_collection_of_object_values(WindowsInformationProtectionIPRangeCollection)),
            "enterprise_i_p_ranges_are_authoritative": lambda n : setattr(self, 'enterprise_i_p_ranges_are_authoritative', n.get_bool_value()),
            "enterprise_internal_proxy_servers": lambda n : setattr(self, 'enterprise_internal_proxy_servers', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
            "enterprise_network_domain_names": lambda n : setattr(self, 'enterprise_network_domain_names', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
            "enterprise_protected_domain_names": lambda n : setattr(self, 'enterprise_protected_domain_names', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
            "enterprise_proxied_domains": lambda n : setattr(self, 'enterprise_proxied_domains', n.get_collection_of_object_values(WindowsInformationProtectionProxiedDomainCollection)),
            "enterprise_proxy_servers": lambda n : setattr(self, 'enterprise_proxy_servers', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
            "enterprise_proxy_servers_are_authoritative": lambda n : setattr(self, 'enterprise_proxy_servers_are_authoritative', n.get_bool_value()),
            "exempt_app_locker_files": lambda n : setattr(self, 'exempt_app_locker_files', n.get_collection_of_object_values(WindowsInformationProtectionAppLockerFile)),
            "exempt_apps": lambda n : setattr(self, 'exempt_apps', n.get_collection_of_object_values(WindowsInformationProtectionApp)),
            "icons_visible": lambda n : setattr(self, 'icons_visible', n.get_bool_value()),
            "indexing_encrypted_stores_or_items_blocked": lambda n : setattr(self, 'indexing_encrypted_stores_or_items_blocked', n.get_bool_value()),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "neutral_domain_resources": lambda n : setattr(self, 'neutral_domain_resources', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
            "protected_app_locker_files": lambda n : setattr(self, 'protected_app_locker_files', n.get_collection_of_object_values(WindowsInformationProtectionAppLockerFile)),
            "protected_apps": lambda n : setattr(self, 'protected_apps', n.get_collection_of_object_values(WindowsInformationProtectionApp)),
            "protection_under_lock_config_required": lambda n : setattr(self, 'protection_under_lock_config_required', n.get_bool_value()),
            "revoke_on_unenroll_disabled": lambda n : setattr(self, 'revoke_on_unenroll_disabled', n.get_bool_value()),
            "rights_management_services_template_id": lambda n : setattr(self, 'rights_management_services_template_id', n.get_uuid_value()),
            "smb_auto_encrypted_file_extensions": lambda n : setattr(self, 'smb_auto_encrypted_file_extensions', n.get_collection_of_object_values(WindowsInformationProtectionResourceCollection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bool_value("azure_rights_management_services_allowed", self.azure_rights_management_services_allowed)
        writer.write_object_value("data_recovery_certificate", self.data_recovery_certificate)
        writer.write_enum_value("enforcement_level", self.enforcement_level)
        writer.write_str_value("enterprise_domain", self.enterprise_domain)
        writer.write_collection_of_object_values("enterprise_i_p_ranges", self.enterprise_i_p_ranges)
        writer.write_bool_value("enterprise_i_p_ranges_are_authoritative", self.enterprise_i_p_ranges_are_authoritative)
        writer.write_collection_of_object_values("enterprise_internal_proxy_servers", self.enterprise_internal_proxy_servers)
        writer.write_collection_of_object_values("enterprise_network_domain_names", self.enterprise_network_domain_names)
        writer.write_collection_of_object_values("enterprise_protected_domain_names", self.enterprise_protected_domain_names)
        writer.write_collection_of_object_values("enterprise_proxied_domains", self.enterprise_proxied_domains)
        writer.write_collection_of_object_values("enterprise_proxy_servers", self.enterprise_proxy_servers)
        writer.write_bool_value("enterprise_proxy_servers_are_authoritative", self.enterprise_proxy_servers_are_authoritative)
        writer.write_collection_of_object_values("exempt_app_locker_files", self.exempt_app_locker_files)
        writer.write_collection_of_object_values("exempt_apps", self.exempt_apps)
        writer.write_bool_value("icons_visible", self.icons_visible)
        writer.write_bool_value("indexing_encrypted_stores_or_items_blocked", self.indexing_encrypted_stores_or_items_blocked)
        writer.write_bool_value("is_assigned", self.is_assigned)
        writer.write_collection_of_object_values("neutral_domain_resources", self.neutral_domain_resources)
        writer.write_collection_of_object_values("protected_app_locker_files", self.protected_app_locker_files)
        writer.write_collection_of_object_values("protected_apps", self.protected_apps)
        writer.write_bool_value("protection_under_lock_config_required", self.protection_under_lock_config_required)
        writer.write_bool_value("revoke_on_unenroll_disabled", self.revoke_on_unenroll_disabled)
        writer.write_uuid_value("rights_management_services_template_id", self.rights_management_services_template_id)
        writer.write_collection_of_object_values("smb_auto_encrypted_file_extensions", self.smb_auto_encrypted_file_extensions)
    

