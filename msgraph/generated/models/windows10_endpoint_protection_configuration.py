from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
    from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
    from .app_locker_application_control_type import AppLockerApplicationControlType
    from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
    from .device_configuration import DeviceConfiguration
    from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
    from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
    from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
    from .windows_firewall_network_profile import WindowsFirewallNetworkProfile

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10EndpointProtectionConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the Windows10EndpointProtectionConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EndpointProtectionConfiguration"
    # Possible values of AppLocker Application Control Types
    app_locker_application_control: Optional[AppLockerApplicationControlType] = None
    # Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
    application_guard_allow_persistence: Optional[bool] = None
    # Allow printing to Local Printers from Container
    application_guard_allow_print_to_local_printers: Optional[bool] = None
    # Allow printing to Network Printers from Container
    application_guard_allow_print_to_network_printers: Optional[bool] = None
    # Allow printing to PDF from Container
    application_guard_allow_print_to_p_d_f: Optional[bool] = None
    # Allow printing to XPS from Container
    application_guard_allow_print_to_x_p_s: Optional[bool] = None
    # Possible values for applicationGuardBlockClipboardSharingType
    application_guard_block_clipboard_sharing: Optional[ApplicationGuardBlockClipboardSharingType] = None
    # Possible values for applicationGuardBlockFileTransfer
    application_guard_block_file_transfer: Optional[ApplicationGuardBlockFileTransferType] = None
    # Block enterprise sites to load non-enterprise content, such as third party plug-ins
    application_guard_block_non_enterprise_content: Optional[bool] = None
    # Enable Windows Defender Application Guard
    application_guard_enabled: Optional[bool] = None
    # Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
    application_guard_force_auditing: Optional[bool] = None
    # Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
    bit_locker_disable_warning_for_other_disk_encryption: Optional[bool] = None
    # Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
    bit_locker_enable_storage_card_encryption_on_mobile: Optional[bool] = None
    # Allows the admin to require encryption to be turned on using BitLocker.
    bit_locker_encrypt_device: Optional[bool] = None
    # BitLocker Removable Drive Policy.
    bit_locker_removable_drive_policy: Optional[BitLockerRemovableDrivePolicy] = None
    # List of folder paths to be added to the list of protected folders
    defender_additional_guarded_folders: Optional[list[str]] = None
    # List of exe files and folders to be excluded from attack surface reduction rules
    defender_attack_surface_reduction_excluded_paths: Optional[list[str]] = None
    # Xml content containing information regarding exploit protection details.
    defender_exploit_protection_xml: Optional[bytes] = None
    # Name of the file from which DefenderExploitProtectionXml was obtained.
    defender_exploit_protection_xml_file_name: Optional[str] = None
    # List of paths to exe that are allowed to access protected folders
    defender_guarded_folders_allowed_app_paths: Optional[list[str]] = None
    # Indicates whether or not to block user from overriding Exploit Protection settings.
    defender_security_center_block_exploit_protection_override: Optional[bool] = None
    # Blocks stateful FTP connections to the device
    firewall_block_stateful_f_t_p: Optional[bool] = None
    # Possible values for firewallCertificateRevocationListCheckMethod
    firewall_certificate_revocation_list_check_method: Optional[FirewallCertificateRevocationListCheckMethodType] = None
    # Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
    firewall_i_p_sec_exemptions_allow_d_h_c_p: Optional[bool] = None
    # Configures IPSec exemptions to allow ICMP
    firewall_i_p_sec_exemptions_allow_i_c_m_p: Optional[bool] = None
    # Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
    firewall_i_p_sec_exemptions_allow_neighbor_discovery: Optional[bool] = None
    # Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
    firewall_i_p_sec_exemptions_allow_router_discovery: Optional[bool] = None
    # Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
    firewall_idle_timeout_for_security_association_in_seconds: Optional[int] = None
    # If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
    firewall_merge_keying_module_settings: Optional[bool] = None
    # Possible values for firewallPacketQueueingMethod
    firewall_packet_queueing_method: Optional[FirewallPacketQueueingMethodType] = None
    # Possible values for firewallPreSharedKeyEncodingMethod
    firewall_pre_shared_key_encoding_method: Optional[FirewallPreSharedKeyEncodingMethodType] = None
    # Configures the firewall profile settings for domain networks
    firewall_profile_domain: Optional[WindowsFirewallNetworkProfile] = None
    # Configures the firewall profile settings for private networks
    firewall_profile_private: Optional[WindowsFirewallNetworkProfile] = None
    # Configures the firewall profile settings for public networks
    firewall_profile_public: Optional[WindowsFirewallNetworkProfile] = None
    # Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
    smart_screen_block_override_for_files: Optional[bool] = None
    # Allows IT Admins to configure SmartScreen for Windows.
    smart_screen_enable_in_shell: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10EndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EndpointProtectionConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10EndpointProtectionConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
        from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
        from .app_locker_application_control_type import AppLockerApplicationControlType
        from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
        from .device_configuration import DeviceConfiguration
        from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
        from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
        from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
        from .windows_firewall_network_profile import WindowsFirewallNetworkProfile

        from .application_guard_block_clipboard_sharing_type import ApplicationGuardBlockClipboardSharingType
        from .application_guard_block_file_transfer_type import ApplicationGuardBlockFileTransferType
        from .app_locker_application_control_type import AppLockerApplicationControlType
        from .bit_locker_removable_drive_policy import BitLockerRemovableDrivePolicy
        from .device_configuration import DeviceConfiguration
        from .firewall_certificate_revocation_list_check_method_type import FirewallCertificateRevocationListCheckMethodType
        from .firewall_packet_queueing_method_type import FirewallPacketQueueingMethodType
        from .firewall_pre_shared_key_encoding_method_type import FirewallPreSharedKeyEncodingMethodType
        from .windows_firewall_network_profile import WindowsFirewallNetworkProfile

        fields: dict[str, Callable[[Any], None]] = {
            "appLockerApplicationControl": lambda n : setattr(self, 'app_locker_application_control', n.get_enum_value(AppLockerApplicationControlType)),
            "applicationGuardAllowPersistence": lambda n : setattr(self, 'application_guard_allow_persistence', n.get_bool_value()),
            "applicationGuardAllowPrintToLocalPrinters": lambda n : setattr(self, 'application_guard_allow_print_to_local_printers', n.get_bool_value()),
            "applicationGuardAllowPrintToNetworkPrinters": lambda n : setattr(self, 'application_guard_allow_print_to_network_printers', n.get_bool_value()),
            "applicationGuardAllowPrintToPDF": lambda n : setattr(self, 'application_guard_allow_print_to_p_d_f', n.get_bool_value()),
            "applicationGuardAllowPrintToXPS": lambda n : setattr(self, 'application_guard_allow_print_to_x_p_s', n.get_bool_value()),
            "applicationGuardBlockClipboardSharing": lambda n : setattr(self, 'application_guard_block_clipboard_sharing', n.get_enum_value(ApplicationGuardBlockClipboardSharingType)),
            "applicationGuardBlockFileTransfer": lambda n : setattr(self, 'application_guard_block_file_transfer', n.get_enum_value(ApplicationGuardBlockFileTransferType)),
            "applicationGuardBlockNonEnterpriseContent": lambda n : setattr(self, 'application_guard_block_non_enterprise_content', n.get_bool_value()),
            "applicationGuardEnabled": lambda n : setattr(self, 'application_guard_enabled', n.get_bool_value()),
            "applicationGuardForceAuditing": lambda n : setattr(self, 'application_guard_force_auditing', n.get_bool_value()),
            "bitLockerDisableWarningForOtherDiskEncryption": lambda n : setattr(self, 'bit_locker_disable_warning_for_other_disk_encryption', n.get_bool_value()),
            "bitLockerEnableStorageCardEncryptionOnMobile": lambda n : setattr(self, 'bit_locker_enable_storage_card_encryption_on_mobile', n.get_bool_value()),
            "bitLockerEncryptDevice": lambda n : setattr(self, 'bit_locker_encrypt_device', n.get_bool_value()),
            "bitLockerRemovableDrivePolicy": lambda n : setattr(self, 'bit_locker_removable_drive_policy', n.get_object_value(BitLockerRemovableDrivePolicy)),
            "defenderAdditionalGuardedFolders": lambda n : setattr(self, 'defender_additional_guarded_folders', n.get_collection_of_primitive_values(str)),
            "defenderAttackSurfaceReductionExcludedPaths": lambda n : setattr(self, 'defender_attack_surface_reduction_excluded_paths', n.get_collection_of_primitive_values(str)),
            "defenderExploitProtectionXml": lambda n : setattr(self, 'defender_exploit_protection_xml', n.get_bytes_value()),
            "defenderExploitProtectionXmlFileName": lambda n : setattr(self, 'defender_exploit_protection_xml_file_name', n.get_str_value()),
            "defenderGuardedFoldersAllowedAppPaths": lambda n : setattr(self, 'defender_guarded_folders_allowed_app_paths', n.get_collection_of_primitive_values(str)),
            "defenderSecurityCenterBlockExploitProtectionOverride": lambda n : setattr(self, 'defender_security_center_block_exploit_protection_override', n.get_bool_value()),
            "firewallBlockStatefulFTP": lambda n : setattr(self, 'firewall_block_stateful_f_t_p', n.get_bool_value()),
            "firewallCertificateRevocationListCheckMethod": lambda n : setattr(self, 'firewall_certificate_revocation_list_check_method', n.get_enum_value(FirewallCertificateRevocationListCheckMethodType)),
            "firewallIPSecExemptionsAllowDHCP": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_d_h_c_p', n.get_bool_value()),
            "firewallIPSecExemptionsAllowICMP": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_i_c_m_p', n.get_bool_value()),
            "firewallIPSecExemptionsAllowNeighborDiscovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_neighbor_discovery', n.get_bool_value()),
            "firewallIPSecExemptionsAllowRouterDiscovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_router_discovery', n.get_bool_value()),
            "firewallIdleTimeoutForSecurityAssociationInSeconds": lambda n : setattr(self, 'firewall_idle_timeout_for_security_association_in_seconds', n.get_int_value()),
            "firewallMergeKeyingModuleSettings": lambda n : setattr(self, 'firewall_merge_keying_module_settings', n.get_bool_value()),
            "firewallPacketQueueingMethod": lambda n : setattr(self, 'firewall_packet_queueing_method', n.get_enum_value(FirewallPacketQueueingMethodType)),
            "firewallPreSharedKeyEncodingMethod": lambda n : setattr(self, 'firewall_pre_shared_key_encoding_method', n.get_enum_value(FirewallPreSharedKeyEncodingMethodType)),
            "firewallProfileDomain": lambda n : setattr(self, 'firewall_profile_domain', n.get_object_value(WindowsFirewallNetworkProfile)),
            "firewallProfilePrivate": lambda n : setattr(self, 'firewall_profile_private', n.get_object_value(WindowsFirewallNetworkProfile)),
            "firewallProfilePublic": lambda n : setattr(self, 'firewall_profile_public', n.get_object_value(WindowsFirewallNetworkProfile)),
            "smartScreenBlockOverrideForFiles": lambda n : setattr(self, 'smart_screen_block_override_for_files', n.get_bool_value()),
            "smartScreenEnableInShell": lambda n : setattr(self, 'smart_screen_enable_in_shell', n.get_bool_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("appLockerApplicationControl", self.app_locker_application_control)
        writer.write_bool_value("applicationGuardAllowPersistence", self.application_guard_allow_persistence)
        writer.write_bool_value("applicationGuardAllowPrintToLocalPrinters", self.application_guard_allow_print_to_local_printers)
        writer.write_bool_value("applicationGuardAllowPrintToNetworkPrinters", self.application_guard_allow_print_to_network_printers)
        writer.write_bool_value("applicationGuardAllowPrintToPDF", self.application_guard_allow_print_to_p_d_f)
        writer.write_bool_value("applicationGuardAllowPrintToXPS", self.application_guard_allow_print_to_x_p_s)
        writer.write_enum_value("applicationGuardBlockClipboardSharing", self.application_guard_block_clipboard_sharing)
        writer.write_enum_value("applicationGuardBlockFileTransfer", self.application_guard_block_file_transfer)
        writer.write_bool_value("applicationGuardBlockNonEnterpriseContent", self.application_guard_block_non_enterprise_content)
        writer.write_bool_value("applicationGuardEnabled", self.application_guard_enabled)
        writer.write_bool_value("applicationGuardForceAuditing", self.application_guard_force_auditing)
        writer.write_bool_value("bitLockerDisableWarningForOtherDiskEncryption", self.bit_locker_disable_warning_for_other_disk_encryption)
        writer.write_bool_value("bitLockerEnableStorageCardEncryptionOnMobile", self.bit_locker_enable_storage_card_encryption_on_mobile)
        writer.write_bool_value("bitLockerEncryptDevice", self.bit_locker_encrypt_device)
        writer.write_object_value("bitLockerRemovableDrivePolicy", self.bit_locker_removable_drive_policy)
        writer.write_collection_of_primitive_values("defenderAdditionalGuardedFolders", self.defender_additional_guarded_folders)
        writer.write_collection_of_primitive_values("defenderAttackSurfaceReductionExcludedPaths", self.defender_attack_surface_reduction_excluded_paths)
        writer.write_bytes_value("defenderExploitProtectionXml", self.defender_exploit_protection_xml)
        writer.write_str_value("defenderExploitProtectionXmlFileName", self.defender_exploit_protection_xml_file_name)
        writer.write_collection_of_primitive_values("defenderGuardedFoldersAllowedAppPaths", self.defender_guarded_folders_allowed_app_paths)
        writer.write_bool_value("defenderSecurityCenterBlockExploitProtectionOverride", self.defender_security_center_block_exploit_protection_override)
        writer.write_bool_value("firewallBlockStatefulFTP", self.firewall_block_stateful_f_t_p)
        writer.write_enum_value("firewallCertificateRevocationListCheckMethod", self.firewall_certificate_revocation_list_check_method)
        writer.write_bool_value("firewallIPSecExemptionsAllowDHCP", self.firewall_i_p_sec_exemptions_allow_d_h_c_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowICMP", self.firewall_i_p_sec_exemptions_allow_i_c_m_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowNeighborDiscovery", self.firewall_i_p_sec_exemptions_allow_neighbor_discovery)
        writer.write_bool_value("firewallIPSecExemptionsAllowRouterDiscovery", self.firewall_i_p_sec_exemptions_allow_router_discovery)
        writer.write_int_value("firewallIdleTimeoutForSecurityAssociationInSeconds", self.firewall_idle_timeout_for_security_association_in_seconds)
        writer.write_bool_value("firewallMergeKeyingModuleSettings", self.firewall_merge_keying_module_settings)
        writer.write_enum_value("firewallPacketQueueingMethod", self.firewall_packet_queueing_method)
        writer.write_enum_value("firewallPreSharedKeyEncodingMethod", self.firewall_pre_shared_key_encoding_method)
        writer.write_object_value("firewallProfileDomain", self.firewall_profile_domain)
        writer.write_object_value("firewallProfilePrivate", self.firewall_profile_private)
        writer.write_object_value("firewallProfilePublic", self.firewall_profile_public)
        writer.write_bool_value("smartScreenBlockOverrideForFiles", self.smart_screen_block_override_for_files)
        writer.write_bool_value("smartScreenEnableInShell", self.smart_screen_enable_in_shell)
    

