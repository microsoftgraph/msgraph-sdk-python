from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')
targeted_managed_app_policy_assignment = lazy_import('msgraph.generated.models.targeted_managed_app_policy_assignment')
windows_information_protection_app = lazy_import('msgraph.generated.models.windows_information_protection_app')
windows_information_protection_app_locker_file = lazy_import('msgraph.generated.models.windows_information_protection_app_locker_file')
windows_information_protection_data_recovery_certificate = lazy_import('msgraph.generated.models.windows_information_protection_data_recovery_certificate')
windows_information_protection_enforcement_level = lazy_import('msgraph.generated.models.windows_information_protection_enforcement_level')
windows_information_protection_i_p_range_collection = lazy_import('msgraph.generated.models.windows_information_protection_i_p_range_collection')
windows_information_protection_proxied_domain_collection = lazy_import('msgraph.generated.models.windows_information_protection_proxied_domain_collection')
windows_information_protection_resource_collection = lazy_import('msgraph.generated.models.windows_information_protection_resource_collection')

class WindowsInformationProtection(managed_app_policy.ManagedAppPolicy):
    @property
    def assignments(self,) -> Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]:
        """
        Gets the assignments property value. Navigation property to list of security groups targeted for policy.
        Returns: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. Navigation property to list of security groups targeted for policy.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def azure_rights_management_services_allowed(self,) -> Optional[bool]:
        """
        Gets the azureRightsManagementServicesAllowed property value. Specifies whether to allow Azure RMS encryption for WIP
        Returns: Optional[bool]
        """
        return self._azure_rights_management_services_allowed
    
    @azure_rights_management_services_allowed.setter
    def azure_rights_management_services_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureRightsManagementServicesAllowed property value. Specifies whether to allow Azure RMS encryption for WIP
        Args:
            value: Value to set for the azureRightsManagementServicesAllowed property.
        """
        self._azure_rights_management_services_allowed = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsInformationProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsInformationProtection"
        # Navigation property to list of security groups targeted for policy.
        self._assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
        # Specifies whether to allow Azure RMS encryption for WIP
        self._azure_rights_management_services_allowed: Optional[bool] = None
        # Specifies a recovery certificate that can be used for data recovery of encrypted files. This is the same as the data recovery agent(DRA) certificate for encrypting file system(EFS)
        self._data_recovery_certificate: Optional[windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate] = None
        # Possible values for WIP Protection enforcement levels
        self._enforcement_level: Optional[windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel] = None
        # Primary enterprise domain
        self._enterprise_domain: Optional[str] = None
        # This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies
        self._enterprise_internal_proxy_servers: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
        # Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to
        self._enterprise_i_p_ranges: Optional[List[windows_information_protection_i_p_range_collection.WindowsInformationProtectionIPRangeCollection]] = None
        # Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false
        self._enterprise_i_p_ranges_are_authoritative: Optional[bool] = None
        # This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to
        self._enterprise_network_domain_names: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
        # List of enterprise domains to be protected
        self._enterprise_protected_domain_names: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
        # Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy
        self._enterprise_proxied_domains: Optional[List[windows_information_protection_proxied_domain_collection.WindowsInformationProtectionProxiedDomainCollection]] = None
        # This is a list of proxy servers. Any server not on this list is considered non-enterprise
        self._enterprise_proxy_servers: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
        # Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        self._enterprise_proxy_servers_are_authoritative: Optional[bool] = None
        # Another way to input exempt apps through xml files
        self._exempt_app_locker_files: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]] = None
        # Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.
        self._exempt_apps: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]] = None
        # Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app
        self._icons_visible: Optional[bool] = None
        # This switch is for the Windows Search Indexer, to allow or disallow indexing of items
        self._indexing_encrypted_stores_or_items_blocked: Optional[bool] = None
        # Indicates if the policy is deployed to any inclusion groups or not.
        self._is_assigned: Optional[bool] = None
        # List of domain names that can used for work or personal resource
        self._neutral_domain_resources: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
        # Another way to input protected apps through xml files
        self._protected_app_locker_files: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]] = None
        # Protected applications can access enterprise data and the data handled by those applications are protected with encryption
        self._protected_apps: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]] = None
        # Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured
        self._protection_under_lock_config_required: Optional[bool] = None
        # This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.
        self._revoke_on_unenroll_disabled: Optional[bool] = None
        # TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access
        self._rights_management_services_template_id: Optional[Guid] = None
        # Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary
        self._smb_auto_encrypted_file_extensions: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtection()
    
    @property
    def data_recovery_certificate(self,) -> Optional[windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate]:
        """
        Gets the dataRecoveryCertificate property value. Specifies a recovery certificate that can be used for data recovery of encrypted files. This is the same as the data recovery agent(DRA) certificate for encrypting file system(EFS)
        Returns: Optional[windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate]
        """
        return self._data_recovery_certificate
    
    @data_recovery_certificate.setter
    def data_recovery_certificate(self,value: Optional[windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate] = None) -> None:
        """
        Sets the dataRecoveryCertificate property value. Specifies a recovery certificate that can be used for data recovery of encrypted files. This is the same as the data recovery agent(DRA) certificate for encrypting file system(EFS)
        Args:
            value: Value to set for the dataRecoveryCertificate property.
        """
        self._data_recovery_certificate = value
    
    @property
    def enforcement_level(self,) -> Optional[windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel]:
        """
        Gets the enforcementLevel property value. Possible values for WIP Protection enforcement levels
        Returns: Optional[windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel]
        """
        return self._enforcement_level
    
    @enforcement_level.setter
    def enforcement_level(self,value: Optional[windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel] = None) -> None:
        """
        Sets the enforcementLevel property value. Possible values for WIP Protection enforcement levels
        Args:
            value: Value to set for the enforcementLevel property.
        """
        self._enforcement_level = value
    
    @property
    def enterprise_domain(self,) -> Optional[str]:
        """
        Gets the enterpriseDomain property value. Primary enterprise domain
        Returns: Optional[str]
        """
        return self._enterprise_domain
    
    @enterprise_domain.setter
    def enterprise_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the enterpriseDomain property value. Primary enterprise domain
        Args:
            value: Value to set for the enterpriseDomain property.
        """
        self._enterprise_domain = value
    
    @property
    def enterprise_internal_proxy_servers(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the enterpriseInternalProxyServers property value. This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._enterprise_internal_proxy_servers
    
    @enterprise_internal_proxy_servers.setter
    def enterprise_internal_proxy_servers(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the enterpriseInternalProxyServers property value. This is the comma-separated list of internal proxy servers. For example, '157.54.14.28, 157.54.11.118, 10.202.14.167, 157.53.14.163, 157.69.210.59'. These proxies have been configured by the admin to connect to specific resources on the Internet. They are considered to be enterprise network locations. The proxies are only leveraged in configuring the EnterpriseProxiedDomains policy to force traffic to the matched domains through these proxies
        Args:
            value: Value to set for the enterpriseInternalProxyServers property.
        """
        self._enterprise_internal_proxy_servers = value
    
    @property
    def enterprise_i_p_ranges(self,) -> Optional[List[windows_information_protection_i_p_range_collection.WindowsInformationProtectionIPRangeCollection]]:
        """
        Gets the enterpriseIPRanges property value. Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to
        Returns: Optional[List[windows_information_protection_i_p_range_collection.WindowsInformationProtectionIPRangeCollection]]
        """
        return self._enterprise_i_p_ranges
    
    @enterprise_i_p_ranges.setter
    def enterprise_i_p_ranges(self,value: Optional[List[windows_information_protection_i_p_range_collection.WindowsInformationProtectionIPRangeCollection]] = None) -> None:
        """
        Sets the enterpriseIPRanges property value. Sets the enterprise IP ranges that define the computers in the enterprise network. Data that comes from those computers will be considered part of the enterprise and protected. These locations will be considered a safe destination for enterprise data to be shared to
        Args:
            value: Value to set for the enterpriseIPRanges property.
        """
        self._enterprise_i_p_ranges = value
    
    @property
    def enterprise_i_p_ranges_are_authoritative(self,) -> Optional[bool]:
        """
        Gets the enterpriseIPRangesAreAuthoritative property value. Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false
        Returns: Optional[bool]
        """
        return self._enterprise_i_p_ranges_are_authoritative
    
    @enterprise_i_p_ranges_are_authoritative.setter
    def enterprise_i_p_ranges_are_authoritative(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseIPRangesAreAuthoritative property value. Boolean value that tells the client to accept the configured list and not to use heuristics to attempt to find other subnets. Default is false
        Args:
            value: Value to set for the enterpriseIPRangesAreAuthoritative property.
        """
        self._enterprise_i_p_ranges_are_authoritative = value
    
    @property
    def enterprise_network_domain_names(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the enterpriseNetworkDomainNames property value. This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._enterprise_network_domain_names
    
    @enterprise_network_domain_names.setter
    def enterprise_network_domain_names(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the enterpriseNetworkDomainNames property value. This is the list of domains that comprise the boundaries of the enterprise. Data from one of these domains that is sent to a device will be considered enterprise data and protected These locations will be considered a safe destination for enterprise data to be shared to
        Args:
            value: Value to set for the enterpriseNetworkDomainNames property.
        """
        self._enterprise_network_domain_names = value
    
    @property
    def enterprise_protected_domain_names(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the enterpriseProtectedDomainNames property value. List of enterprise domains to be protected
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._enterprise_protected_domain_names
    
    @enterprise_protected_domain_names.setter
    def enterprise_protected_domain_names(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the enterpriseProtectedDomainNames property value. List of enterprise domains to be protected
        Args:
            value: Value to set for the enterpriseProtectedDomainNames property.
        """
        self._enterprise_protected_domain_names = value
    
    @property
    def enterprise_proxied_domains(self,) -> Optional[List[windows_information_protection_proxied_domain_collection.WindowsInformationProtectionProxiedDomainCollection]]:
        """
        Gets the enterpriseProxiedDomains property value. Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy
        Returns: Optional[List[windows_information_protection_proxied_domain_collection.WindowsInformationProtectionProxiedDomainCollection]]
        """
        return self._enterprise_proxied_domains
    
    @enterprise_proxied_domains.setter
    def enterprise_proxied_domains(self,value: Optional[List[windows_information_protection_proxied_domain_collection.WindowsInformationProtectionProxiedDomainCollection]] = None) -> None:
        """
        Sets the enterpriseProxiedDomains property value. Contains a list of Enterprise resource domains hosted in the cloud that need to be protected. Connections to these resources are considered enterprise data. If a proxy is paired with a cloud resource, traffic to the cloud resource will be routed through the enterprise network via the denoted proxy server (on Port 80). A proxy server used for this purpose must also be configured using the EnterpriseInternalProxyServers policy
        Args:
            value: Value to set for the enterpriseProxiedDomains property.
        """
        self._enterprise_proxied_domains = value
    
    @property
    def enterprise_proxy_servers(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the enterpriseProxyServers property value. This is a list of proxy servers. Any server not on this list is considered non-enterprise
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._enterprise_proxy_servers
    
    @enterprise_proxy_servers.setter
    def enterprise_proxy_servers(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the enterpriseProxyServers property value. This is a list of proxy servers. Any server not on this list is considered non-enterprise
        Args:
            value: Value to set for the enterpriseProxyServers property.
        """
        self._enterprise_proxy_servers = value
    
    @property
    def enterprise_proxy_servers_are_authoritative(self,) -> Optional[bool]:
        """
        Gets the enterpriseProxyServersAreAuthoritative property value. Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        Returns: Optional[bool]
        """
        return self._enterprise_proxy_servers_are_authoritative
    
    @enterprise_proxy_servers_are_authoritative.setter
    def enterprise_proxy_servers_are_authoritative(self,value: Optional[bool] = None) -> None:
        """
        Sets the enterpriseProxyServersAreAuthoritative property value. Boolean value that tells the client to accept the configured list of proxies and not try to detect other work proxies. Default is false
        Args:
            value: Value to set for the enterpriseProxyServersAreAuthoritative property.
        """
        self._enterprise_proxy_servers_are_authoritative = value
    
    @property
    def exempt_app_locker_files(self,) -> Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]]:
        """
        Gets the exemptAppLockerFiles property value. Another way to input exempt apps through xml files
        Returns: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]]
        """
        return self._exempt_app_locker_files
    
    @exempt_app_locker_files.setter
    def exempt_app_locker_files(self,value: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]] = None) -> None:
        """
        Sets the exemptAppLockerFiles property value. Another way to input exempt apps through xml files
        Args:
            value: Value to set for the exemptAppLockerFiles property.
        """
        self._exempt_app_locker_files = value
    
    @property
    def exempt_apps(self,) -> Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]]:
        """
        Gets the exemptApps property value. Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.
        Returns: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]]
        """
        return self._exempt_apps
    
    @exempt_apps.setter
    def exempt_apps(self,value: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]] = None) -> None:
        """
        Sets the exemptApps property value. Exempt applications can also access enterprise data, but the data handled by those applications are not protected. This is because some critical enterprise applications may have compatibility problems with encrypted data.
        Args:
            value: Value to set for the exemptApps property.
        """
        self._exempt_apps = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment)),
            "azure_rights_management_services_allowed": lambda n : setattr(self, 'azure_rights_management_services_allowed', n.get_bool_value()),
            "data_recovery_certificate": lambda n : setattr(self, 'data_recovery_certificate', n.get_object_value(windows_information_protection_data_recovery_certificate.WindowsInformationProtectionDataRecoveryCertificate)),
            "enforcement_level": lambda n : setattr(self, 'enforcement_level', n.get_enum_value(windows_information_protection_enforcement_level.WindowsInformationProtectionEnforcementLevel)),
            "enterprise_domain": lambda n : setattr(self, 'enterprise_domain', n.get_str_value()),
            "enterprise_internal_proxy_servers": lambda n : setattr(self, 'enterprise_internal_proxy_servers', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
            "enterprise_i_p_ranges": lambda n : setattr(self, 'enterprise_i_p_ranges', n.get_collection_of_object_values(windows_information_protection_i_p_range_collection.WindowsInformationProtectionIPRangeCollection)),
            "enterprise_i_p_ranges_are_authoritative": lambda n : setattr(self, 'enterprise_i_p_ranges_are_authoritative', n.get_bool_value()),
            "enterprise_network_domain_names": lambda n : setattr(self, 'enterprise_network_domain_names', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
            "enterprise_protected_domain_names": lambda n : setattr(self, 'enterprise_protected_domain_names', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
            "enterprise_proxied_domains": lambda n : setattr(self, 'enterprise_proxied_domains', n.get_collection_of_object_values(windows_information_protection_proxied_domain_collection.WindowsInformationProtectionProxiedDomainCollection)),
            "enterprise_proxy_servers": lambda n : setattr(self, 'enterprise_proxy_servers', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
            "enterprise_proxy_servers_are_authoritative": lambda n : setattr(self, 'enterprise_proxy_servers_are_authoritative', n.get_bool_value()),
            "exempt_app_locker_files": lambda n : setattr(self, 'exempt_app_locker_files', n.get_collection_of_object_values(windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile)),
            "exempt_apps": lambda n : setattr(self, 'exempt_apps', n.get_collection_of_object_values(windows_information_protection_app.WindowsInformationProtectionApp)),
            "icons_visible": lambda n : setattr(self, 'icons_visible', n.get_bool_value()),
            "indexing_encrypted_stores_or_items_blocked": lambda n : setattr(self, 'indexing_encrypted_stores_or_items_blocked', n.get_bool_value()),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "neutral_domain_resources": lambda n : setattr(self, 'neutral_domain_resources', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
            "protected_app_locker_files": lambda n : setattr(self, 'protected_app_locker_files', n.get_collection_of_object_values(windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile)),
            "protected_apps": lambda n : setattr(self, 'protected_apps', n.get_collection_of_object_values(windows_information_protection_app.WindowsInformationProtectionApp)),
            "protection_under_lock_config_required": lambda n : setattr(self, 'protection_under_lock_config_required', n.get_bool_value()),
            "revoke_on_unenroll_disabled": lambda n : setattr(self, 'revoke_on_unenroll_disabled', n.get_bool_value()),
            "rights_management_services_template_id": lambda n : setattr(self, 'rights_management_services_template_id', n.get_object_value(Guid)),
            "smb_auto_encrypted_file_extensions": lambda n : setattr(self, 'smb_auto_encrypted_file_extensions', n.get_collection_of_object_values(windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def icons_visible(self,) -> Optional[bool]:
        """
        Gets the iconsVisible property value. Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app
        Returns: Optional[bool]
        """
        return self._icons_visible
    
    @icons_visible.setter
    def icons_visible(self,value: Optional[bool] = None) -> None:
        """
        Sets the iconsVisible property value. Determines whether overlays are added to icons for WIP protected files in Explorer and enterprise only app tiles in the Start menu. Starting in Windows 10, version 1703 this setting also configures the visibility of the WIP icon in the title bar of a WIP-protected app
        Args:
            value: Value to set for the iconsVisible property.
        """
        self._icons_visible = value
    
    @property
    def indexing_encrypted_stores_or_items_blocked(self,) -> Optional[bool]:
        """
        Gets the indexingEncryptedStoresOrItemsBlocked property value. This switch is for the Windows Search Indexer, to allow or disallow indexing of items
        Returns: Optional[bool]
        """
        return self._indexing_encrypted_stores_or_items_blocked
    
    @indexing_encrypted_stores_or_items_blocked.setter
    def indexing_encrypted_stores_or_items_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the indexingEncryptedStoresOrItemsBlocked property value. This switch is for the Windows Search Indexer, to allow or disallow indexing of items
        Args:
            value: Value to set for the indexingEncryptedStoresOrItemsBlocked property.
        """
        self._indexing_encrypted_stores_or_items_blocked = value
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. Indicates if the policy is deployed to any inclusion groups or not.
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. Indicates if the policy is deployed to any inclusion groups or not.
        Args:
            value: Value to set for the isAssigned property.
        """
        self._is_assigned = value
    
    @property
    def neutral_domain_resources(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the neutralDomainResources property value. List of domain names that can used for work or personal resource
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._neutral_domain_resources
    
    @neutral_domain_resources.setter
    def neutral_domain_resources(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the neutralDomainResources property value. List of domain names that can used for work or personal resource
        Args:
            value: Value to set for the neutralDomainResources property.
        """
        self._neutral_domain_resources = value
    
    @property
    def protected_app_locker_files(self,) -> Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]]:
        """
        Gets the protectedAppLockerFiles property value. Another way to input protected apps through xml files
        Returns: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]]
        """
        return self._protected_app_locker_files
    
    @protected_app_locker_files.setter
    def protected_app_locker_files(self,value: Optional[List[windows_information_protection_app_locker_file.WindowsInformationProtectionAppLockerFile]] = None) -> None:
        """
        Sets the protectedAppLockerFiles property value. Another way to input protected apps through xml files
        Args:
            value: Value to set for the protectedAppLockerFiles property.
        """
        self._protected_app_locker_files = value
    
    @property
    def protected_apps(self,) -> Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]]:
        """
        Gets the protectedApps property value. Protected applications can access enterprise data and the data handled by those applications are protected with encryption
        Returns: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]]
        """
        return self._protected_apps
    
    @protected_apps.setter
    def protected_apps(self,value: Optional[List[windows_information_protection_app.WindowsInformationProtectionApp]] = None) -> None:
        """
        Sets the protectedApps property value. Protected applications can access enterprise data and the data handled by those applications are protected with encryption
        Args:
            value: Value to set for the protectedApps property.
        """
        self._protected_apps = value
    
    @property
    def protection_under_lock_config_required(self,) -> Optional[bool]:
        """
        Gets the protectionUnderLockConfigRequired property value. Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured
        Returns: Optional[bool]
        """
        return self._protection_under_lock_config_required
    
    @protection_under_lock_config_required.setter
    def protection_under_lock_config_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the protectionUnderLockConfigRequired property value. Specifies whether the protection under lock feature (also known as encrypt under pin) should be configured
        Args:
            value: Value to set for the protectionUnderLockConfigRequired property.
        """
        self._protection_under_lock_config_required = value
    
    @property
    def revoke_on_unenroll_disabled(self,) -> Optional[bool]:
        """
        Gets the revokeOnUnenrollDisabled property value. This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.
        Returns: Optional[bool]
        """
        return self._revoke_on_unenroll_disabled
    
    @revoke_on_unenroll_disabled.setter
    def revoke_on_unenroll_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the revokeOnUnenrollDisabled property value. This policy controls whether to revoke the WIP keys when a device unenrolls from the management service. If set to 1 (Don't revoke keys), the keys will not be revoked and the user will continue to have access to protected files after unenrollment. If the keys are not revoked, there will be no revoked file cleanup subsequently.
        Args:
            value: Value to set for the revokeOnUnenrollDisabled property.
        """
        self._revoke_on_unenroll_disabled = value
    
    @property
    def rights_management_services_template_id(self,) -> Optional[Guid]:
        """
        Gets the rightsManagementServicesTemplateId property value. TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access
        Returns: Optional[Guid]
        """
        return self._rights_management_services_template_id
    
    @rights_management_services_template_id.setter
    def rights_management_services_template_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the rightsManagementServicesTemplateId property value. TemplateID GUID to use for RMS encryption. The RMS template allows the IT admin to configure the details about who has access to RMS-protected file and how long they have access
        Args:
            value: Value to set for the rightsManagementServicesTemplateId property.
        """
        self._rights_management_services_template_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_bool_value("azureRightsManagementServicesAllowed", self.azure_rights_management_services_allowed)
        writer.write_object_value("dataRecoveryCertificate", self.data_recovery_certificate)
        writer.write_enum_value("enforcementLevel", self.enforcement_level)
        writer.write_str_value("enterpriseDomain", self.enterprise_domain)
        writer.write_collection_of_object_values("enterpriseInternalProxyServers", self.enterprise_internal_proxy_servers)
        writer.write_collection_of_object_values("enterpriseIPRanges", self.enterprise_i_p_ranges)
        writer.write_bool_value("enterpriseIPRangesAreAuthoritative", self.enterprise_i_p_ranges_are_authoritative)
        writer.write_collection_of_object_values("enterpriseNetworkDomainNames", self.enterprise_network_domain_names)
        writer.write_collection_of_object_values("enterpriseProtectedDomainNames", self.enterprise_protected_domain_names)
        writer.write_collection_of_object_values("enterpriseProxiedDomains", self.enterprise_proxied_domains)
        writer.write_collection_of_object_values("enterpriseProxyServers", self.enterprise_proxy_servers)
        writer.write_bool_value("enterpriseProxyServersAreAuthoritative", self.enterprise_proxy_servers_are_authoritative)
        writer.write_collection_of_object_values("exemptAppLockerFiles", self.exempt_app_locker_files)
        writer.write_collection_of_object_values("exemptApps", self.exempt_apps)
        writer.write_bool_value("iconsVisible", self.icons_visible)
        writer.write_bool_value("indexingEncryptedStoresOrItemsBlocked", self.indexing_encrypted_stores_or_items_blocked)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_collection_of_object_values("neutralDomainResources", self.neutral_domain_resources)
        writer.write_collection_of_object_values("protectedAppLockerFiles", self.protected_app_locker_files)
        writer.write_collection_of_object_values("protectedApps", self.protected_apps)
        writer.write_bool_value("protectionUnderLockConfigRequired", self.protection_under_lock_config_required)
        writer.write_bool_value("revokeOnUnenrollDisabled", self.revoke_on_unenroll_disabled)
        writer.write_object_value("rightsManagementServicesTemplateId", self.rights_management_services_template_id)
        writer.write_collection_of_object_values("smbAutoEncryptedFileExtensions", self.smb_auto_encrypted_file_extensions)
    
    @property
    def smb_auto_encrypted_file_extensions(self,) -> Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]:
        """
        Gets the smbAutoEncryptedFileExtensions property value. Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary
        Returns: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]]
        """
        return self._smb_auto_encrypted_file_extensions
    
    @smb_auto_encrypted_file_extensions.setter
    def smb_auto_encrypted_file_extensions(self,value: Optional[List[windows_information_protection_resource_collection.WindowsInformationProtectionResourceCollection]] = None) -> None:
        """
        Sets the smbAutoEncryptedFileExtensions property value. Specifies a list of file extensions, so that files with these extensions are encrypted when copying from an SMB share within the corporate boundary
        Args:
            value: Value to set for the smbAutoEncryptedFileExtensions property.
        """
        self._smb_auto_encrypted_file_extensions = value
    

