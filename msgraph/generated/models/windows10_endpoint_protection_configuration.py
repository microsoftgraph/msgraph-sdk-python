from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_locker_application_control_type = lazy_import('msgraph.generated.models.app_locker_application_control_type')
application_guard_block_clipboard_sharing_type = lazy_import('msgraph.generated.models.application_guard_block_clipboard_sharing_type')
application_guard_block_file_transfer_type = lazy_import('msgraph.generated.models.application_guard_block_file_transfer_type')
bit_locker_removable_drive_policy = lazy_import('msgraph.generated.models.bit_locker_removable_drive_policy')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
firewall_certificate_revocation_list_check_method_type = lazy_import('msgraph.generated.models.firewall_certificate_revocation_list_check_method_type')
firewall_packet_queueing_method_type = lazy_import('msgraph.generated.models.firewall_packet_queueing_method_type')
firewall_pre_shared_key_encoding_method_type = lazy_import('msgraph.generated.models.firewall_pre_shared_key_encoding_method_type')
windows_firewall_network_profile = lazy_import('msgraph.generated.models.windows_firewall_network_profile')

class Windows10EndpointProtectionConfiguration(device_configuration.DeviceConfiguration):
    @property
    def application_guard_allow_persistence(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPersistence property value. Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        Returns: Optional[bool]
        """
        return self._application_guard_allow_persistence
    
    @application_guard_allow_persistence.setter
    def application_guard_allow_persistence(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPersistence property value. Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        Args:
            value: Value to set for the applicationGuardAllowPersistence property.
        """
        self._application_guard_allow_persistence = value
    
    @property
    def application_guard_allow_print_to_local_printers(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToLocalPrinters property value. Allow printing to Local Printers from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_local_printers
    
    @application_guard_allow_print_to_local_printers.setter
    def application_guard_allow_print_to_local_printers(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToLocalPrinters property value. Allow printing to Local Printers from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToLocalPrinters property.
        """
        self._application_guard_allow_print_to_local_printers = value
    
    @property
    def application_guard_allow_print_to_network_printers(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToNetworkPrinters property value. Allow printing to Network Printers from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_network_printers
    
    @application_guard_allow_print_to_network_printers.setter
    def application_guard_allow_print_to_network_printers(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToNetworkPrinters property value. Allow printing to Network Printers from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToNetworkPrinters property.
        """
        self._application_guard_allow_print_to_network_printers = value
    
    @property
    def application_guard_allow_print_to_p_d_f(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToPDF property value. Allow printing to PDF from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_p_d_f
    
    @application_guard_allow_print_to_p_d_f.setter
    def application_guard_allow_print_to_p_d_f(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToPDF property value. Allow printing to PDF from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToPDF property.
        """
        self._application_guard_allow_print_to_p_d_f = value
    
    @property
    def application_guard_allow_print_to_x_p_s(self,) -> Optional[bool]:
        """
        Gets the applicationGuardAllowPrintToXPS property value. Allow printing to XPS from Container
        Returns: Optional[bool]
        """
        return self._application_guard_allow_print_to_x_p_s
    
    @application_guard_allow_print_to_x_p_s.setter
    def application_guard_allow_print_to_x_p_s(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardAllowPrintToXPS property value. Allow printing to XPS from Container
        Args:
            value: Value to set for the applicationGuardAllowPrintToXPS property.
        """
        self._application_guard_allow_print_to_x_p_s = value
    
    @property
    def application_guard_block_clipboard_sharing(self,) -> Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType]:
        """
        Gets the applicationGuardBlockClipboardSharing property value. Possible values for applicationGuardBlockClipboardSharingType
        Returns: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType]
        """
        return self._application_guard_block_clipboard_sharing
    
    @application_guard_block_clipboard_sharing.setter
    def application_guard_block_clipboard_sharing(self,value: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType] = None) -> None:
        """
        Sets the applicationGuardBlockClipboardSharing property value. Possible values for applicationGuardBlockClipboardSharingType
        Args:
            value: Value to set for the applicationGuardBlockClipboardSharing property.
        """
        self._application_guard_block_clipboard_sharing = value
    
    @property
    def application_guard_block_file_transfer(self,) -> Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType]:
        """
        Gets the applicationGuardBlockFileTransfer property value. Possible values for applicationGuardBlockFileTransfer
        Returns: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType]
        """
        return self._application_guard_block_file_transfer
    
    @application_guard_block_file_transfer.setter
    def application_guard_block_file_transfer(self,value: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType] = None) -> None:
        """
        Sets the applicationGuardBlockFileTransfer property value. Possible values for applicationGuardBlockFileTransfer
        Args:
            value: Value to set for the applicationGuardBlockFileTransfer property.
        """
        self._application_guard_block_file_transfer = value
    
    @property
    def application_guard_block_non_enterprise_content(self,) -> Optional[bool]:
        """
        Gets the applicationGuardBlockNonEnterpriseContent property value. Block enterprise sites to load non-enterprise content, such as third party plug-ins
        Returns: Optional[bool]
        """
        return self._application_guard_block_non_enterprise_content
    
    @application_guard_block_non_enterprise_content.setter
    def application_guard_block_non_enterprise_content(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardBlockNonEnterpriseContent property value. Block enterprise sites to load non-enterprise content, such as third party plug-ins
        Args:
            value: Value to set for the applicationGuardBlockNonEnterpriseContent property.
        """
        self._application_guard_block_non_enterprise_content = value
    
    @property
    def application_guard_enabled(self,) -> Optional[bool]:
        """
        Gets the applicationGuardEnabled property value. Enable Windows Defender Application Guard
        Returns: Optional[bool]
        """
        return self._application_guard_enabled
    
    @application_guard_enabled.setter
    def application_guard_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardEnabled property value. Enable Windows Defender Application Guard
        Args:
            value: Value to set for the applicationGuardEnabled property.
        """
        self._application_guard_enabled = value
    
    @property
    def application_guard_force_auditing(self,) -> Optional[bool]:
        """
        Gets the applicationGuardForceAuditing property value. Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        Returns: Optional[bool]
        """
        return self._application_guard_force_auditing
    
    @application_guard_force_auditing.setter
    def application_guard_force_auditing(self,value: Optional[bool] = None) -> None:
        """
        Sets the applicationGuardForceAuditing property value. Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        Args:
            value: Value to set for the applicationGuardForceAuditing property.
        """
        self._application_guard_force_auditing = value
    
    @property
    def app_locker_application_control(self,) -> Optional[app_locker_application_control_type.AppLockerApplicationControlType]:
        """
        Gets the appLockerApplicationControl property value. Possible values of AppLocker Application Control Types
        Returns: Optional[app_locker_application_control_type.AppLockerApplicationControlType]
        """
        return self._app_locker_application_control
    
    @app_locker_application_control.setter
    def app_locker_application_control(self,value: Optional[app_locker_application_control_type.AppLockerApplicationControlType] = None) -> None:
        """
        Sets the appLockerApplicationControl property value. Possible values of AppLocker Application Control Types
        Args:
            value: Value to set for the appLockerApplicationControl property.
        """
        self._app_locker_application_control = value
    
    @property
    def bit_locker_disable_warning_for_other_disk_encryption(self,) -> Optional[bool]:
        """
        Gets the bitLockerDisableWarningForOtherDiskEncryption property value. Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        Returns: Optional[bool]
        """
        return self._bit_locker_disable_warning_for_other_disk_encryption
    
    @bit_locker_disable_warning_for_other_disk_encryption.setter
    def bit_locker_disable_warning_for_other_disk_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerDisableWarningForOtherDiskEncryption property value. Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        Args:
            value: Value to set for the bitLockerDisableWarningForOtherDiskEncryption property.
        """
        self._bit_locker_disable_warning_for_other_disk_encryption = value
    
    @property
    def bit_locker_enable_storage_card_encryption_on_mobile(self,) -> Optional[bool]:
        """
        Gets the bitLockerEnableStorageCardEncryptionOnMobile property value. Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        Returns: Optional[bool]
        """
        return self._bit_locker_enable_storage_card_encryption_on_mobile
    
    @bit_locker_enable_storage_card_encryption_on_mobile.setter
    def bit_locker_enable_storage_card_encryption_on_mobile(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEnableStorageCardEncryptionOnMobile property value. Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        Args:
            value: Value to set for the bitLockerEnableStorageCardEncryptionOnMobile property.
        """
        self._bit_locker_enable_storage_card_encryption_on_mobile = value
    
    @property
    def bit_locker_encrypt_device(self,) -> Optional[bool]:
        """
        Gets the bitLockerEncryptDevice property value. Allows the admin to require encryption to be turned on using BitLocker.
        Returns: Optional[bool]
        """
        return self._bit_locker_encrypt_device
    
    @bit_locker_encrypt_device.setter
    def bit_locker_encrypt_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEncryptDevice property value. Allows the admin to require encryption to be turned on using BitLocker.
        Args:
            value: Value to set for the bitLockerEncryptDevice property.
        """
        self._bit_locker_encrypt_device = value
    
    @property
    def bit_locker_removable_drive_policy(self,) -> Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy]:
        """
        Gets the bitLockerRemovableDrivePolicy property value. BitLocker Removable Drive Policy.
        Returns: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy]
        """
        return self._bit_locker_removable_drive_policy
    
    @bit_locker_removable_drive_policy.setter
    def bit_locker_removable_drive_policy(self,value: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy] = None) -> None:
        """
        Sets the bitLockerRemovableDrivePolicy property value. BitLocker Removable Drive Policy.
        Args:
            value: Value to set for the bitLockerRemovableDrivePolicy property.
        """
        self._bit_locker_removable_drive_policy = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10EndpointProtectionConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10EndpointProtectionConfiguration"
        # Allow persisting user generated data inside the App Guard Containter (favorites, cookies, web passwords, etc.)
        self._application_guard_allow_persistence: Optional[bool] = None
        # Allow printing to Local Printers from Container
        self._application_guard_allow_print_to_local_printers: Optional[bool] = None
        # Allow printing to Network Printers from Container
        self._application_guard_allow_print_to_network_printers: Optional[bool] = None
        # Allow printing to PDF from Container
        self._application_guard_allow_print_to_p_d_f: Optional[bool] = None
        # Allow printing to XPS from Container
        self._application_guard_allow_print_to_x_p_s: Optional[bool] = None
        # Possible values for applicationGuardBlockClipboardSharingType
        self._application_guard_block_clipboard_sharing: Optional[application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType] = None
        # Possible values for applicationGuardBlockFileTransfer
        self._application_guard_block_file_transfer: Optional[application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType] = None
        # Block enterprise sites to load non-enterprise content, such as third party plug-ins
        self._application_guard_block_non_enterprise_content: Optional[bool] = None
        # Enable Windows Defender Application Guard
        self._application_guard_enabled: Optional[bool] = None
        # Force auditing will persist Windows logs and events to meet security/compliance criteria (sample events are user login-logoff, use of privilege rights, software installation, system changes, etc.)
        self._application_guard_force_auditing: Optional[bool] = None
        # Possible values of AppLocker Application Control Types
        self._app_locker_application_control: Optional[app_locker_application_control_type.AppLockerApplicationControlType] = None
        # Allows the Admin to disable the warning prompt for other disk encryption on the user machines.
        self._bit_locker_disable_warning_for_other_disk_encryption: Optional[bool] = None
        # Allows the admin to require encryption to be turned on using BitLocker. This policy is valid only for a mobile SKU.
        self._bit_locker_enable_storage_card_encryption_on_mobile: Optional[bool] = None
        # Allows the admin to require encryption to be turned on using BitLocker.
        self._bit_locker_encrypt_device: Optional[bool] = None
        # BitLocker Removable Drive Policy.
        self._bit_locker_removable_drive_policy: Optional[bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy] = None
        # List of folder paths to be added to the list of protected folders
        self._defender_additional_guarded_folders: Optional[List[str]] = None
        # List of exe files and folders to be excluded from attack surface reduction rules
        self._defender_attack_surface_reduction_excluded_paths: Optional[List[str]] = None
        # Xml content containing information regarding exploit protection details.
        self._defender_exploit_protection_xml: Optional[bytes] = None
        # Name of the file from which DefenderExploitProtectionXml was obtained.
        self._defender_exploit_protection_xml_file_name: Optional[str] = None
        # List of paths to exe that are allowed to access protected folders
        self._defender_guarded_folders_allowed_app_paths: Optional[List[str]] = None
        # Indicates whether or not to block user from overriding Exploit Protection settings.
        self._defender_security_center_block_exploit_protection_override: Optional[bool] = None
        # Blocks stateful FTP connections to the device
        self._firewall_block_stateful_f_t_p: Optional[bool] = None
        # Possible values for firewallCertificateRevocationListCheckMethod
        self._firewall_certificate_revocation_list_check_method: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType] = None
        # Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        self._firewall_idle_timeout_for_security_association_in_seconds: Optional[int] = None
        # Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        self._firewall_i_p_sec_exemptions_allow_d_h_c_p: Optional[bool] = None
        # Configures IPSec exemptions to allow ICMP
        self._firewall_i_p_sec_exemptions_allow_i_c_m_p: Optional[bool] = None
        # Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        self._firewall_i_p_sec_exemptions_allow_neighbor_discovery: Optional[bool] = None
        # Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        self._firewall_i_p_sec_exemptions_allow_router_discovery: Optional[bool] = None
        # If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        self._firewall_merge_keying_module_settings: Optional[bool] = None
        # Possible values for firewallPacketQueueingMethod
        self._firewall_packet_queueing_method: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType] = None
        # Possible values for firewallPreSharedKeyEncodingMethod
        self._firewall_pre_shared_key_encoding_method: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType] = None
        # Configures the firewall profile settings for domain networks
        self._firewall_profile_domain: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Configures the firewall profile settings for private networks
        self._firewall_profile_private: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Configures the firewall profile settings for public networks
        self._firewall_profile_public: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None
        # Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        self._smart_screen_block_override_for_files: Optional[bool] = None
        # Allows IT Admins to configure SmartScreen for Windows.
        self._smart_screen_enable_in_shell: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EndpointProtectionConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EndpointProtectionConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10EndpointProtectionConfiguration()
    
    @property
    def defender_additional_guarded_folders(self,) -> Optional[List[str]]:
        """
        Gets the defenderAdditionalGuardedFolders property value. List of folder paths to be added to the list of protected folders
        Returns: Optional[List[str]]
        """
        return self._defender_additional_guarded_folders
    
    @defender_additional_guarded_folders.setter
    def defender_additional_guarded_folders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderAdditionalGuardedFolders property value. List of folder paths to be added to the list of protected folders
        Args:
            value: Value to set for the defenderAdditionalGuardedFolders property.
        """
        self._defender_additional_guarded_folders = value
    
    @property
    def defender_attack_surface_reduction_excluded_paths(self,) -> Optional[List[str]]:
        """
        Gets the defenderAttackSurfaceReductionExcludedPaths property value. List of exe files and folders to be excluded from attack surface reduction rules
        Returns: Optional[List[str]]
        """
        return self._defender_attack_surface_reduction_excluded_paths
    
    @defender_attack_surface_reduction_excluded_paths.setter
    def defender_attack_surface_reduction_excluded_paths(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderAttackSurfaceReductionExcludedPaths property value. List of exe files and folders to be excluded from attack surface reduction rules
        Args:
            value: Value to set for the defenderAttackSurfaceReductionExcludedPaths property.
        """
        self._defender_attack_surface_reduction_excluded_paths = value
    
    @property
    def defender_exploit_protection_xml(self,) -> Optional[bytes]:
        """
        Gets the defenderExploitProtectionXml property value. Xml content containing information regarding exploit protection details.
        Returns: Optional[bytes]
        """
        return self._defender_exploit_protection_xml
    
    @defender_exploit_protection_xml.setter
    def defender_exploit_protection_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the defenderExploitProtectionXml property value. Xml content containing information regarding exploit protection details.
        Args:
            value: Value to set for the defenderExploitProtectionXml property.
        """
        self._defender_exploit_protection_xml = value
    
    @property
    def defender_exploit_protection_xml_file_name(self,) -> Optional[str]:
        """
        Gets the defenderExploitProtectionXmlFileName property value. Name of the file from which DefenderExploitProtectionXml was obtained.
        Returns: Optional[str]
        """
        return self._defender_exploit_protection_xml_file_name
    
    @defender_exploit_protection_xml_file_name.setter
    def defender_exploit_protection_xml_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the defenderExploitProtectionXmlFileName property value. Name of the file from which DefenderExploitProtectionXml was obtained.
        Args:
            value: Value to set for the defenderExploitProtectionXmlFileName property.
        """
        self._defender_exploit_protection_xml_file_name = value
    
    @property
    def defender_guarded_folders_allowed_app_paths(self,) -> Optional[List[str]]:
        """
        Gets the defenderGuardedFoldersAllowedAppPaths property value. List of paths to exe that are allowed to access protected folders
        Returns: Optional[List[str]]
        """
        return self._defender_guarded_folders_allowed_app_paths
    
    @defender_guarded_folders_allowed_app_paths.setter
    def defender_guarded_folders_allowed_app_paths(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the defenderGuardedFoldersAllowedAppPaths property value. List of paths to exe that are allowed to access protected folders
        Args:
            value: Value to set for the defenderGuardedFoldersAllowedAppPaths property.
        """
        self._defender_guarded_folders_allowed_app_paths = value
    
    @property
    def defender_security_center_block_exploit_protection_override(self,) -> Optional[bool]:
        """
        Gets the defenderSecurityCenterBlockExploitProtectionOverride property value. Indicates whether or not to block user from overriding Exploit Protection settings.
        Returns: Optional[bool]
        """
        return self._defender_security_center_block_exploit_protection_override
    
    @defender_security_center_block_exploit_protection_override.setter
    def defender_security_center_block_exploit_protection_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the defenderSecurityCenterBlockExploitProtectionOverride property value. Indicates whether or not to block user from overriding Exploit Protection settings.
        Args:
            value: Value to set for the defenderSecurityCenterBlockExploitProtectionOverride property.
        """
        self._defender_security_center_block_exploit_protection_override = value
    
    @property
    def firewall_block_stateful_f_t_p(self,) -> Optional[bool]:
        """
        Gets the firewallBlockStatefulFTP property value. Blocks stateful FTP connections to the device
        Returns: Optional[bool]
        """
        return self._firewall_block_stateful_f_t_p
    
    @firewall_block_stateful_f_t_p.setter
    def firewall_block_stateful_f_t_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallBlockStatefulFTP property value. Blocks stateful FTP connections to the device
        Args:
            value: Value to set for the firewallBlockStatefulFTP property.
        """
        self._firewall_block_stateful_f_t_p = value
    
    @property
    def firewall_certificate_revocation_list_check_method(self,) -> Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType]:
        """
        Gets the firewallCertificateRevocationListCheckMethod property value. Possible values for firewallCertificateRevocationListCheckMethod
        Returns: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType]
        """
        return self._firewall_certificate_revocation_list_check_method
    
    @firewall_certificate_revocation_list_check_method.setter
    def firewall_certificate_revocation_list_check_method(self,value: Optional[firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType] = None) -> None:
        """
        Sets the firewallCertificateRevocationListCheckMethod property value. Possible values for firewallCertificateRevocationListCheckMethod
        Args:
            value: Value to set for the firewallCertificateRevocationListCheckMethod property.
        """
        self._firewall_certificate_revocation_list_check_method = value
    
    @property
    def firewall_idle_timeout_for_security_association_in_seconds(self,) -> Optional[int]:
        """
        Gets the firewallIdleTimeoutForSecurityAssociationInSeconds property value. Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        Returns: Optional[int]
        """
        return self._firewall_idle_timeout_for_security_association_in_seconds
    
    @firewall_idle_timeout_for_security_association_in_seconds.setter
    def firewall_idle_timeout_for_security_association_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the firewallIdleTimeoutForSecurityAssociationInSeconds property value. Configures the idle timeout for security associations, in seconds, from 300 to 3600 inclusive. This is the period after which security associations will expire and be deleted. Valid values 300 to 3600
        Args:
            value: Value to set for the firewallIdleTimeoutForSecurityAssociationInSeconds property.
        """
        self._firewall_idle_timeout_for_security_association_in_seconds = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_d_h_c_p(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowDHCP property value. Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_d_h_c_p
    
    @firewall_i_p_sec_exemptions_allow_d_h_c_p.setter
    def firewall_i_p_sec_exemptions_allow_d_h_c_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowDHCP property value. Configures IPSec exemptions to allow both IPv4 and IPv6 DHCP traffic
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowDHCP property.
        """
        self._firewall_i_p_sec_exemptions_allow_d_h_c_p = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_i_c_m_p(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowICMP property value. Configures IPSec exemptions to allow ICMP
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_i_c_m_p
    
    @firewall_i_p_sec_exemptions_allow_i_c_m_p.setter
    def firewall_i_p_sec_exemptions_allow_i_c_m_p(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowICMP property value. Configures IPSec exemptions to allow ICMP
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowICMP property.
        """
        self._firewall_i_p_sec_exemptions_allow_i_c_m_p = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_neighbor_discovery(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowNeighborDiscovery property value. Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_neighbor_discovery
    
    @firewall_i_p_sec_exemptions_allow_neighbor_discovery.setter
    def firewall_i_p_sec_exemptions_allow_neighbor_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowNeighborDiscovery property value. Configures IPSec exemptions to allow neighbor discovery IPv6 ICMP type-codes
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowNeighborDiscovery property.
        """
        self._firewall_i_p_sec_exemptions_allow_neighbor_discovery = value
    
    @property
    def firewall_i_p_sec_exemptions_allow_router_discovery(self,) -> Optional[bool]:
        """
        Gets the firewallIPSecExemptionsAllowRouterDiscovery property value. Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        Returns: Optional[bool]
        """
        return self._firewall_i_p_sec_exemptions_allow_router_discovery
    
    @firewall_i_p_sec_exemptions_allow_router_discovery.setter
    def firewall_i_p_sec_exemptions_allow_router_discovery(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallIPSecExemptionsAllowRouterDiscovery property value. Configures IPSec exemptions to allow router discovery IPv6 ICMP type-codes
        Args:
            value: Value to set for the firewallIPSecExemptionsAllowRouterDiscovery property.
        """
        self._firewall_i_p_sec_exemptions_allow_router_discovery = value
    
    @property
    def firewall_merge_keying_module_settings(self,) -> Optional[bool]:
        """
        Gets the firewallMergeKeyingModuleSettings property value. If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        Returns: Optional[bool]
        """
        return self._firewall_merge_keying_module_settings
    
    @firewall_merge_keying_module_settings.setter
    def firewall_merge_keying_module_settings(self,value: Optional[bool] = None) -> None:
        """
        Sets the firewallMergeKeyingModuleSettings property value. If an authentication set is not fully supported by a keying module, direct the module to ignore only unsupported authentication suites rather than the entire set
        Args:
            value: Value to set for the firewallMergeKeyingModuleSettings property.
        """
        self._firewall_merge_keying_module_settings = value
    
    @property
    def firewall_packet_queueing_method(self,) -> Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType]:
        """
        Gets the firewallPacketQueueingMethod property value. Possible values for firewallPacketQueueingMethod
        Returns: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType]
        """
        return self._firewall_packet_queueing_method
    
    @firewall_packet_queueing_method.setter
    def firewall_packet_queueing_method(self,value: Optional[firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType] = None) -> None:
        """
        Sets the firewallPacketQueueingMethod property value. Possible values for firewallPacketQueueingMethod
        Args:
            value: Value to set for the firewallPacketQueueingMethod property.
        """
        self._firewall_packet_queueing_method = value
    
    @property
    def firewall_pre_shared_key_encoding_method(self,) -> Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType]:
        """
        Gets the firewallPreSharedKeyEncodingMethod property value. Possible values for firewallPreSharedKeyEncodingMethod
        Returns: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType]
        """
        return self._firewall_pre_shared_key_encoding_method
    
    @firewall_pre_shared_key_encoding_method.setter
    def firewall_pre_shared_key_encoding_method(self,value: Optional[firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType] = None) -> None:
        """
        Sets the firewallPreSharedKeyEncodingMethod property value. Possible values for firewallPreSharedKeyEncodingMethod
        Args:
            value: Value to set for the firewallPreSharedKeyEncodingMethod property.
        """
        self._firewall_pre_shared_key_encoding_method = value
    
    @property
    def firewall_profile_domain(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfileDomain property value. Configures the firewall profile settings for domain networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_domain
    
    @firewall_profile_domain.setter
    def firewall_profile_domain(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfileDomain property value. Configures the firewall profile settings for domain networks
        Args:
            value: Value to set for the firewallProfileDomain property.
        """
        self._firewall_profile_domain = value
    
    @property
    def firewall_profile_private(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfilePrivate property value. Configures the firewall profile settings for private networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_private
    
    @firewall_profile_private.setter
    def firewall_profile_private(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfilePrivate property value. Configures the firewall profile settings for private networks
        Args:
            value: Value to set for the firewallProfilePrivate property.
        """
        self._firewall_profile_private = value
    
    @property
    def firewall_profile_public(self,) -> Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]:
        """
        Gets the firewallProfilePublic property value. Configures the firewall profile settings for public networks
        Returns: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile]
        """
        return self._firewall_profile_public
    
    @firewall_profile_public.setter
    def firewall_profile_public(self,value: Optional[windows_firewall_network_profile.WindowsFirewallNetworkProfile] = None) -> None:
        """
        Sets the firewallProfilePublic property value. Configures the firewall profile settings for public networks
        Args:
            value: Value to set for the firewallProfilePublic property.
        """
        self._firewall_profile_public = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_guard_allow_persistence": lambda n : setattr(self, 'application_guard_allow_persistence', n.get_bool_value()),
            "application_guard_allow_print_to_local_printers": lambda n : setattr(self, 'application_guard_allow_print_to_local_printers', n.get_bool_value()),
            "application_guard_allow_print_to_network_printers": lambda n : setattr(self, 'application_guard_allow_print_to_network_printers', n.get_bool_value()),
            "application_guard_allow_print_to_p_d_f": lambda n : setattr(self, 'application_guard_allow_print_to_p_d_f', n.get_bool_value()),
            "application_guard_allow_print_to_x_p_s": lambda n : setattr(self, 'application_guard_allow_print_to_x_p_s', n.get_bool_value()),
            "application_guard_block_clipboard_sharing": lambda n : setattr(self, 'application_guard_block_clipboard_sharing', n.get_enum_value(application_guard_block_clipboard_sharing_type.ApplicationGuardBlockClipboardSharingType)),
            "application_guard_block_file_transfer": lambda n : setattr(self, 'application_guard_block_file_transfer', n.get_enum_value(application_guard_block_file_transfer_type.ApplicationGuardBlockFileTransferType)),
            "application_guard_block_non_enterprise_content": lambda n : setattr(self, 'application_guard_block_non_enterprise_content', n.get_bool_value()),
            "application_guard_enabled": lambda n : setattr(self, 'application_guard_enabled', n.get_bool_value()),
            "application_guard_force_auditing": lambda n : setattr(self, 'application_guard_force_auditing', n.get_bool_value()),
            "app_locker_application_control": lambda n : setattr(self, 'app_locker_application_control', n.get_enum_value(app_locker_application_control_type.AppLockerApplicationControlType)),
            "bit_locker_disable_warning_for_other_disk_encryption": lambda n : setattr(self, 'bit_locker_disable_warning_for_other_disk_encryption', n.get_bool_value()),
            "bit_locker_enable_storage_card_encryption_on_mobile": lambda n : setattr(self, 'bit_locker_enable_storage_card_encryption_on_mobile', n.get_bool_value()),
            "bit_locker_encrypt_device": lambda n : setattr(self, 'bit_locker_encrypt_device', n.get_bool_value()),
            "bit_locker_removable_drive_policy": lambda n : setattr(self, 'bit_locker_removable_drive_policy', n.get_object_value(bit_locker_removable_drive_policy.BitLockerRemovableDrivePolicy)),
            "defender_additional_guarded_folders": lambda n : setattr(self, 'defender_additional_guarded_folders', n.get_collection_of_primitive_values(str)),
            "defender_attack_surface_reduction_excluded_paths": lambda n : setattr(self, 'defender_attack_surface_reduction_excluded_paths', n.get_collection_of_primitive_values(str)),
            "defender_exploit_protection_xml": lambda n : setattr(self, 'defender_exploit_protection_xml', n.get_bytes_value()),
            "defender_exploit_protection_xml_file_name": lambda n : setattr(self, 'defender_exploit_protection_xml_file_name', n.get_str_value()),
            "defender_guarded_folders_allowed_app_paths": lambda n : setattr(self, 'defender_guarded_folders_allowed_app_paths', n.get_collection_of_primitive_values(str)),
            "defender_security_center_block_exploit_protection_override": lambda n : setattr(self, 'defender_security_center_block_exploit_protection_override', n.get_bool_value()),
            "firewall_block_stateful_f_t_p": lambda n : setattr(self, 'firewall_block_stateful_f_t_p', n.get_bool_value()),
            "firewall_certificate_revocation_list_check_method": lambda n : setattr(self, 'firewall_certificate_revocation_list_check_method', n.get_enum_value(firewall_certificate_revocation_list_check_method_type.FirewallCertificateRevocationListCheckMethodType)),
            "firewall_idle_timeout_for_security_association_in_seconds": lambda n : setattr(self, 'firewall_idle_timeout_for_security_association_in_seconds', n.get_int_value()),
            "firewall_i_p_sec_exemptions_allow_d_h_c_p": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_d_h_c_p', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_i_c_m_p": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_i_c_m_p', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_neighbor_discovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_neighbor_discovery', n.get_bool_value()),
            "firewall_i_p_sec_exemptions_allow_router_discovery": lambda n : setattr(self, 'firewall_i_p_sec_exemptions_allow_router_discovery', n.get_bool_value()),
            "firewall_merge_keying_module_settings": lambda n : setattr(self, 'firewall_merge_keying_module_settings', n.get_bool_value()),
            "firewall_packet_queueing_method": lambda n : setattr(self, 'firewall_packet_queueing_method', n.get_enum_value(firewall_packet_queueing_method_type.FirewallPacketQueueingMethodType)),
            "firewall_pre_shared_key_encoding_method": lambda n : setattr(self, 'firewall_pre_shared_key_encoding_method', n.get_enum_value(firewall_pre_shared_key_encoding_method_type.FirewallPreSharedKeyEncodingMethodType)),
            "firewall_profile_domain": lambda n : setattr(self, 'firewall_profile_domain', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "firewall_profile_private": lambda n : setattr(self, 'firewall_profile_private', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "firewall_profile_public": lambda n : setattr(self, 'firewall_profile_public', n.get_object_value(windows_firewall_network_profile.WindowsFirewallNetworkProfile)),
            "smart_screen_block_override_for_files": lambda n : setattr(self, 'smart_screen_block_override_for_files', n.get_bool_value()),
            "smart_screen_enable_in_shell": lambda n : setattr(self, 'smart_screen_enable_in_shell', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
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
        writer.write_enum_value("appLockerApplicationControl", self.app_locker_application_control)
        writer.write_bool_value("bitLockerDisableWarningForOtherDiskEncryption", self.bit_locker_disable_warning_for_other_disk_encryption)
        writer.write_bool_value("bitLockerEnableStorageCardEncryptionOnMobile", self.bit_locker_enable_storage_card_encryption_on_mobile)
        writer.write_bool_value("bitLockerEncryptDevice", self.bit_locker_encrypt_device)
        writer.write_object_value("bitLockerRemovableDrivePolicy", self.bit_locker_removable_drive_policy)
        writer.write_collection_of_primitive_values("defenderAdditionalGuardedFolders", self.defender_additional_guarded_folders)
        writer.write_collection_of_primitive_values("defenderAttackSurfaceReductionExcludedPaths", self.defender_attack_surface_reduction_excluded_paths)
        writer.write_object_value("defenderExploitProtectionXml", self.defender_exploit_protection_xml)
        writer.write_str_value("defenderExploitProtectionXmlFileName", self.defender_exploit_protection_xml_file_name)
        writer.write_collection_of_primitive_values("defenderGuardedFoldersAllowedAppPaths", self.defender_guarded_folders_allowed_app_paths)
        writer.write_bool_value("defenderSecurityCenterBlockExploitProtectionOverride", self.defender_security_center_block_exploit_protection_override)
        writer.write_bool_value("firewallBlockStatefulFTP", self.firewall_block_stateful_f_t_p)
        writer.write_enum_value("firewallCertificateRevocationListCheckMethod", self.firewall_certificate_revocation_list_check_method)
        writer.write_int_value("firewallIdleTimeoutForSecurityAssociationInSeconds", self.firewall_idle_timeout_for_security_association_in_seconds)
        writer.write_bool_value("firewallIPSecExemptionsAllowDHCP", self.firewall_i_p_sec_exemptions_allow_d_h_c_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowICMP", self.firewall_i_p_sec_exemptions_allow_i_c_m_p)
        writer.write_bool_value("firewallIPSecExemptionsAllowNeighborDiscovery", self.firewall_i_p_sec_exemptions_allow_neighbor_discovery)
        writer.write_bool_value("firewallIPSecExemptionsAllowRouterDiscovery", self.firewall_i_p_sec_exemptions_allow_router_discovery)
        writer.write_bool_value("firewallMergeKeyingModuleSettings", self.firewall_merge_keying_module_settings)
        writer.write_enum_value("firewallPacketQueueingMethod", self.firewall_packet_queueing_method)
        writer.write_enum_value("firewallPreSharedKeyEncodingMethod", self.firewall_pre_shared_key_encoding_method)
        writer.write_object_value("firewallProfileDomain", self.firewall_profile_domain)
        writer.write_object_value("firewallProfilePrivate", self.firewall_profile_private)
        writer.write_object_value("firewallProfilePublic", self.firewall_profile_public)
        writer.write_bool_value("smartScreenBlockOverrideForFiles", self.smart_screen_block_override_for_files)
        writer.write_bool_value("smartScreenEnableInShell", self.smart_screen_enable_in_shell)
    
    @property
    def smart_screen_block_override_for_files(self,) -> Optional[bool]:
        """
        Gets the smartScreenBlockOverrideForFiles property value. Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        Returns: Optional[bool]
        """
        return self._smart_screen_block_override_for_files
    
    @smart_screen_block_override_for_files.setter
    def smart_screen_block_override_for_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenBlockOverrideForFiles property value. Allows IT Admins to control whether users can can ignore SmartScreen warnings and run malicious files.
        Args:
            value: Value to set for the smartScreenBlockOverrideForFiles property.
        """
        self._smart_screen_block_override_for_files = value
    
    @property
    def smart_screen_enable_in_shell(self,) -> Optional[bool]:
        """
        Gets the smartScreenEnableInShell property value. Allows IT Admins to configure SmartScreen for Windows.
        Returns: Optional[bool]
        """
        return self._smart_screen_enable_in_shell
    
    @smart_screen_enable_in_shell.setter
    def smart_screen_enable_in_shell(self,value: Optional[bool] = None) -> None:
        """
        Sets the smartScreenEnableInShell property value. Allows IT Admins to configure SmartScreen for Windows.
        Args:
            value: Value to set for the smartScreenEnableInShell property.
        """
        self._smart_screen_enable_in_shell = value
    

