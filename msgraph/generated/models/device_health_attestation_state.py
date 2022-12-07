from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceHealthAttestationState(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attestation_identity_key(self,) -> Optional[str]:
        """
        Gets the attestationIdentityKey property value. TWhen an Attestation Identity Key (AIK) is present on a device, it indicates that the device has an endorsement key (EK) certificate.
        Returns: Optional[str]
        """
        return self._attestation_identity_key
    
    @attestation_identity_key.setter
    def attestation_identity_key(self,value: Optional[str] = None) -> None:
        """
        Sets the attestationIdentityKey property value. TWhen an Attestation Identity Key (AIK) is present on a device, it indicates that the device has an endorsement key (EK) certificate.
        Args:
            value: Value to set for the attestationIdentityKey property.
        """
        self._attestation_identity_key = value
    
    @property
    def bit_locker_status(self,) -> Optional[str]:
        """
        Gets the bitLockerStatus property value. On or Off of BitLocker Drive Encryption
        Returns: Optional[str]
        """
        return self._bit_locker_status
    
    @bit_locker_status.setter
    def bit_locker_status(self,value: Optional[str] = None) -> None:
        """
        Sets the bitLockerStatus property value. On or Off of BitLocker Drive Encryption
        Args:
            value: Value to set for the bitLockerStatus property.
        """
        self._bit_locker_status = value
    
    @property
    def boot_app_security_version(self,) -> Optional[str]:
        """
        Gets the bootAppSecurityVersion property value. The security version number of the Boot Application
        Returns: Optional[str]
        """
        return self._boot_app_security_version
    
    @boot_app_security_version.setter
    def boot_app_security_version(self,value: Optional[str] = None) -> None:
        """
        Sets the bootAppSecurityVersion property value. The security version number of the Boot Application
        Args:
            value: Value to set for the bootAppSecurityVersion property.
        """
        self._boot_app_security_version = value
    
    @property
    def boot_debugging(self,) -> Optional[str]:
        """
        Gets the bootDebugging property value. When bootDebugging is enabled, the device is used in development and testing
        Returns: Optional[str]
        """
        return self._boot_debugging
    
    @boot_debugging.setter
    def boot_debugging(self,value: Optional[str] = None) -> None:
        """
        Sets the bootDebugging property value. When bootDebugging is enabled, the device is used in development and testing
        Args:
            value: Value to set for the bootDebugging property.
        """
        self._boot_debugging = value
    
    @property
    def boot_manager_security_version(self,) -> Optional[str]:
        """
        Gets the bootManagerSecurityVersion property value. The security version number of the Boot Application
        Returns: Optional[str]
        """
        return self._boot_manager_security_version
    
    @boot_manager_security_version.setter
    def boot_manager_security_version(self,value: Optional[str] = None) -> None:
        """
        Sets the bootManagerSecurityVersion property value. The security version number of the Boot Application
        Args:
            value: Value to set for the bootManagerSecurityVersion property.
        """
        self._boot_manager_security_version = value
    
    @property
    def boot_manager_version(self,) -> Optional[str]:
        """
        Gets the bootManagerVersion property value. The version of the Boot Manager
        Returns: Optional[str]
        """
        return self._boot_manager_version
    
    @boot_manager_version.setter
    def boot_manager_version(self,value: Optional[str] = None) -> None:
        """
        Sets the bootManagerVersion property value. The version of the Boot Manager
        Args:
            value: Value to set for the bootManagerVersion property.
        """
        self._boot_manager_version = value
    
    @property
    def boot_revision_list_info(self,) -> Optional[str]:
        """
        Gets the bootRevisionListInfo property value. The Boot Revision List that was loaded during initial boot on the attested device
        Returns: Optional[str]
        """
        return self._boot_revision_list_info
    
    @boot_revision_list_info.setter
    def boot_revision_list_info(self,value: Optional[str] = None) -> None:
        """
        Sets the bootRevisionListInfo property value. The Boot Revision List that was loaded during initial boot on the attested device
        Args:
            value: Value to set for the bootRevisionListInfo property.
        """
        self._boot_revision_list_info = value
    
    @property
    def code_integrity(self,) -> Optional[str]:
        """
        Gets the codeIntegrity property value. When code integrity is enabled, code execution is restricted to integrity verified code
        Returns: Optional[str]
        """
        return self._code_integrity
    
    @code_integrity.setter
    def code_integrity(self,value: Optional[str] = None) -> None:
        """
        Sets the codeIntegrity property value. When code integrity is enabled, code execution is restricted to integrity verified code
        Args:
            value: Value to set for the codeIntegrity property.
        """
        self._code_integrity = value
    
    @property
    def code_integrity_check_version(self,) -> Optional[str]:
        """
        Gets the codeIntegrityCheckVersion property value. The version of the Boot Manager
        Returns: Optional[str]
        """
        return self._code_integrity_check_version
    
    @code_integrity_check_version.setter
    def code_integrity_check_version(self,value: Optional[str] = None) -> None:
        """
        Sets the codeIntegrityCheckVersion property value. The version of the Boot Manager
        Args:
            value: Value to set for the codeIntegrityCheckVersion property.
        """
        self._code_integrity_check_version = value
    
    @property
    def code_integrity_policy(self,) -> Optional[str]:
        """
        Gets the codeIntegrityPolicy property value. The Code Integrity policy that is controlling the security of the boot environment
        Returns: Optional[str]
        """
        return self._code_integrity_policy
    
    @code_integrity_policy.setter
    def code_integrity_policy(self,value: Optional[str] = None) -> None:
        """
        Sets the codeIntegrityPolicy property value. The Code Integrity policy that is controlling the security of the boot environment
        Args:
            value: Value to set for the codeIntegrityPolicy property.
        """
        self._code_integrity_policy = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceHealthAttestationState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # TWhen an Attestation Identity Key (AIK) is present on a device, it indicates that the device has an endorsement key (EK) certificate.
        self._attestation_identity_key: Optional[str] = None
        # On or Off of BitLocker Drive Encryption
        self._bit_locker_status: Optional[str] = None
        # The security version number of the Boot Application
        self._boot_app_security_version: Optional[str] = None
        # When bootDebugging is enabled, the device is used in development and testing
        self._boot_debugging: Optional[str] = None
        # The security version number of the Boot Application
        self._boot_manager_security_version: Optional[str] = None
        # The version of the Boot Manager
        self._boot_manager_version: Optional[str] = None
        # The Boot Revision List that was loaded during initial boot on the attested device
        self._boot_revision_list_info: Optional[str] = None
        # When code integrity is enabled, code execution is restricted to integrity verified code
        self._code_integrity: Optional[str] = None
        # The version of the Boot Manager
        self._code_integrity_check_version: Optional[str] = None
        # The Code Integrity policy that is controlling the security of the boot environment
        self._code_integrity_policy: Optional[str] = None
        # The DHA report version. (Namespace version)
        self._content_namespace_url: Optional[str] = None
        # The HealthAttestation state schema version
        self._content_version: Optional[str] = None
        # DEP Policy defines a set of hardware and software technologies that perform additional checks on memory
        self._data_excution_policy: Optional[str] = None
        # The DHA report version. (Namespace version)
        self._device_health_attestation_status: Optional[str] = None
        # ELAM provides protection for the computers in your network when they start up
        self._early_launch_anti_malware_driver_protection: Optional[str] = None
        # This attribute indicates if DHA is supported for the device
        self._health_attestation_supported_status: Optional[str] = None
        # This attribute appears if DHA-Service detects an integrity issue
        self._health_status_mismatch_info: Optional[str] = None
        # The DateTime when device was evaluated or issued to MDM
        self._issued_date_time: Optional[datetime] = None
        # The Timestamp of the last update.
        self._last_update_date_time: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # When operatingSystemKernelDebugging is enabled, the device is used in development and testing
        self._operating_system_kernel_debugging: Optional[str] = None
        # The Operating System Revision List that was loaded during initial boot on the attested device
        self._operating_system_rev_list_info: Optional[str] = None
        # The measurement that is captured in PCR[0]
        self._pcr0: Optional[str] = None
        # Informational attribute that identifies the HASH algorithm that was used by TPM
        self._pcr_hash_algorithm: Optional[str] = None
        # The number of times a PC device has hibernated or resumed
        self._reset_count: Optional[int] = None
        # The number of times a PC device has rebooted
        self._restart_count: Optional[int] = None
        # Safe mode is a troubleshooting option for Windows that starts your computer in a limited state
        self._safe_mode: Optional[str] = None
        # When Secure Boot is enabled, the core components must have the correct cryptographic signatures
        self._secure_boot: Optional[str] = None
        # Fingerprint of the Custom Secure Boot Configuration Policy
        self._secure_boot_configuration_policy_finger_print: Optional[str] = None
        # When test signing is allowed, the device does not enforce signature validation during boot
        self._test_signing: Optional[str] = None
        # The security version number of the Boot Application
        self._tpm_version: Optional[str] = None
        # VSM is a container that protects high value assets from a compromised kernel
        self._virtual_secure_mode: Optional[str] = None
        # Operating system running with limited services that is used to prepare a computer for Windows
        self._windows_p_e: Optional[str] = None
    
    @property
    def content_namespace_url(self,) -> Optional[str]:
        """
        Gets the contentNamespaceUrl property value. The DHA report version. (Namespace version)
        Returns: Optional[str]
        """
        return self._content_namespace_url
    
    @content_namespace_url.setter
    def content_namespace_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentNamespaceUrl property value. The DHA report version. (Namespace version)
        Args:
            value: Value to set for the contentNamespaceUrl property.
        """
        self._content_namespace_url = value
    
    @property
    def content_version(self,) -> Optional[str]:
        """
        Gets the contentVersion property value. The HealthAttestation state schema version
        Returns: Optional[str]
        """
        return self._content_version
    
    @content_version.setter
    def content_version(self,value: Optional[str] = None) -> None:
        """
        Sets the contentVersion property value. The HealthAttestation state schema version
        Args:
            value: Value to set for the contentVersion property.
        """
        self._content_version = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthAttestationState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthAttestationState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceHealthAttestationState()
    
    @property
    def data_excution_policy(self,) -> Optional[str]:
        """
        Gets the dataExcutionPolicy property value. DEP Policy defines a set of hardware and software technologies that perform additional checks on memory
        Returns: Optional[str]
        """
        return self._data_excution_policy
    
    @data_excution_policy.setter
    def data_excution_policy(self,value: Optional[str] = None) -> None:
        """
        Sets the dataExcutionPolicy property value. DEP Policy defines a set of hardware and software technologies that perform additional checks on memory
        Args:
            value: Value to set for the dataExcutionPolicy property.
        """
        self._data_excution_policy = value
    
    @property
    def device_health_attestation_status(self,) -> Optional[str]:
        """
        Gets the deviceHealthAttestationStatus property value. The DHA report version. (Namespace version)
        Returns: Optional[str]
        """
        return self._device_health_attestation_status
    
    @device_health_attestation_status.setter
    def device_health_attestation_status(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceHealthAttestationStatus property value. The DHA report version. (Namespace version)
        Args:
            value: Value to set for the deviceHealthAttestationStatus property.
        """
        self._device_health_attestation_status = value
    
    @property
    def early_launch_anti_malware_driver_protection(self,) -> Optional[str]:
        """
        Gets the earlyLaunchAntiMalwareDriverProtection property value. ELAM provides protection for the computers in your network when they start up
        Returns: Optional[str]
        """
        return self._early_launch_anti_malware_driver_protection
    
    @early_launch_anti_malware_driver_protection.setter
    def early_launch_anti_malware_driver_protection(self,value: Optional[str] = None) -> None:
        """
        Sets the earlyLaunchAntiMalwareDriverProtection property value. ELAM provides protection for the computers in your network when they start up
        Args:
            value: Value to set for the earlyLaunchAntiMalwareDriverProtection property.
        """
        self._early_launch_anti_malware_driver_protection = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attestation_identity_key": lambda n : setattr(self, 'attestation_identity_key', n.get_str_value()),
            "bit_locker_status": lambda n : setattr(self, 'bit_locker_status', n.get_str_value()),
            "boot_app_security_version": lambda n : setattr(self, 'boot_app_security_version', n.get_str_value()),
            "boot_debugging": lambda n : setattr(self, 'boot_debugging', n.get_str_value()),
            "boot_manager_security_version": lambda n : setattr(self, 'boot_manager_security_version', n.get_str_value()),
            "boot_manager_version": lambda n : setattr(self, 'boot_manager_version', n.get_str_value()),
            "boot_revision_list_info": lambda n : setattr(self, 'boot_revision_list_info', n.get_str_value()),
            "code_integrity": lambda n : setattr(self, 'code_integrity', n.get_str_value()),
            "code_integrity_check_version": lambda n : setattr(self, 'code_integrity_check_version', n.get_str_value()),
            "code_integrity_policy": lambda n : setattr(self, 'code_integrity_policy', n.get_str_value()),
            "content_namespace_url": lambda n : setattr(self, 'content_namespace_url', n.get_str_value()),
            "content_version": lambda n : setattr(self, 'content_version', n.get_str_value()),
            "data_excution_policy": lambda n : setattr(self, 'data_excution_policy', n.get_str_value()),
            "device_health_attestation_status": lambda n : setattr(self, 'device_health_attestation_status', n.get_str_value()),
            "early_launch_anti_malware_driver_protection": lambda n : setattr(self, 'early_launch_anti_malware_driver_protection', n.get_str_value()),
            "health_attestation_supported_status": lambda n : setattr(self, 'health_attestation_supported_status', n.get_str_value()),
            "health_status_mismatch_info": lambda n : setattr(self, 'health_status_mismatch_info', n.get_str_value()),
            "issued_date_time": lambda n : setattr(self, 'issued_date_time', n.get_datetime_value()),
            "last_update_date_time": lambda n : setattr(self, 'last_update_date_time', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system_kernel_debugging": lambda n : setattr(self, 'operating_system_kernel_debugging', n.get_str_value()),
            "operating_system_rev_list_info": lambda n : setattr(self, 'operating_system_rev_list_info', n.get_str_value()),
            "pcr0": lambda n : setattr(self, 'pcr0', n.get_str_value()),
            "pcr_hash_algorithm": lambda n : setattr(self, 'pcr_hash_algorithm', n.get_str_value()),
            "reset_count": lambda n : setattr(self, 'reset_count', n.get_int_value()),
            "restart_count": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "safe_mode": lambda n : setattr(self, 'safe_mode', n.get_str_value()),
            "secure_boot": lambda n : setattr(self, 'secure_boot', n.get_str_value()),
            "secure_boot_configuration_policy_finger_print": lambda n : setattr(self, 'secure_boot_configuration_policy_finger_print', n.get_str_value()),
            "test_signing": lambda n : setattr(self, 'test_signing', n.get_str_value()),
            "tpm_version": lambda n : setattr(self, 'tpm_version', n.get_str_value()),
            "virtual_secure_mode": lambda n : setattr(self, 'virtual_secure_mode', n.get_str_value()),
            "windows_p_e": lambda n : setattr(self, 'windows_p_e', n.get_str_value()),
        }
        return fields
    
    @property
    def health_attestation_supported_status(self,) -> Optional[str]:
        """
        Gets the healthAttestationSupportedStatus property value. This attribute indicates if DHA is supported for the device
        Returns: Optional[str]
        """
        return self._health_attestation_supported_status
    
    @health_attestation_supported_status.setter
    def health_attestation_supported_status(self,value: Optional[str] = None) -> None:
        """
        Sets the healthAttestationSupportedStatus property value. This attribute indicates if DHA is supported for the device
        Args:
            value: Value to set for the healthAttestationSupportedStatus property.
        """
        self._health_attestation_supported_status = value
    
    @property
    def health_status_mismatch_info(self,) -> Optional[str]:
        """
        Gets the healthStatusMismatchInfo property value. This attribute appears if DHA-Service detects an integrity issue
        Returns: Optional[str]
        """
        return self._health_status_mismatch_info
    
    @health_status_mismatch_info.setter
    def health_status_mismatch_info(self,value: Optional[str] = None) -> None:
        """
        Sets the healthStatusMismatchInfo property value. This attribute appears if DHA-Service detects an integrity issue
        Args:
            value: Value to set for the healthStatusMismatchInfo property.
        """
        self._health_status_mismatch_info = value
    
    @property
    def issued_date_time(self,) -> Optional[datetime]:
        """
        Gets the issuedDateTime property value. The DateTime when device was evaluated or issued to MDM
        Returns: Optional[datetime]
        """
        return self._issued_date_time
    
    @issued_date_time.setter
    def issued_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the issuedDateTime property value. The DateTime when device was evaluated or issued to MDM
        Args:
            value: Value to set for the issuedDateTime property.
        """
        self._issued_date_time = value
    
    @property
    def last_update_date_time(self,) -> Optional[str]:
        """
        Gets the lastUpdateDateTime property value. The Timestamp of the last update.
        Returns: Optional[str]
        """
        return self._last_update_date_time
    
    @last_update_date_time.setter
    def last_update_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the lastUpdateDateTime property value. The Timestamp of the last update.
        Args:
            value: Value to set for the lastUpdateDateTime property.
        """
        self._last_update_date_time = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operating_system_kernel_debugging(self,) -> Optional[str]:
        """
        Gets the operatingSystemKernelDebugging property value. When operatingSystemKernelDebugging is enabled, the device is used in development and testing
        Returns: Optional[str]
        """
        return self._operating_system_kernel_debugging
    
    @operating_system_kernel_debugging.setter
    def operating_system_kernel_debugging(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemKernelDebugging property value. When operatingSystemKernelDebugging is enabled, the device is used in development and testing
        Args:
            value: Value to set for the operatingSystemKernelDebugging property.
        """
        self._operating_system_kernel_debugging = value
    
    @property
    def operating_system_rev_list_info(self,) -> Optional[str]:
        """
        Gets the operatingSystemRevListInfo property value. The Operating System Revision List that was loaded during initial boot on the attested device
        Returns: Optional[str]
        """
        return self._operating_system_rev_list_info
    
    @operating_system_rev_list_info.setter
    def operating_system_rev_list_info(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemRevListInfo property value. The Operating System Revision List that was loaded during initial boot on the attested device
        Args:
            value: Value to set for the operatingSystemRevListInfo property.
        """
        self._operating_system_rev_list_info = value
    
    @property
    def pcr0(self,) -> Optional[str]:
        """
        Gets the pcr0 property value. The measurement that is captured in PCR[0]
        Returns: Optional[str]
        """
        return self._pcr0
    
    @pcr0.setter
    def pcr0(self,value: Optional[str] = None) -> None:
        """
        Sets the pcr0 property value. The measurement that is captured in PCR[0]
        Args:
            value: Value to set for the pcr0 property.
        """
        self._pcr0 = value
    
    @property
    def pcr_hash_algorithm(self,) -> Optional[str]:
        """
        Gets the pcrHashAlgorithm property value. Informational attribute that identifies the HASH algorithm that was used by TPM
        Returns: Optional[str]
        """
        return self._pcr_hash_algorithm
    
    @pcr_hash_algorithm.setter
    def pcr_hash_algorithm(self,value: Optional[str] = None) -> None:
        """
        Sets the pcrHashAlgorithm property value. Informational attribute that identifies the HASH algorithm that was used by TPM
        Args:
            value: Value to set for the pcrHashAlgorithm property.
        """
        self._pcr_hash_algorithm = value
    
    @property
    def reset_count(self,) -> Optional[int]:
        """
        Gets the resetCount property value. The number of times a PC device has hibernated or resumed
        Returns: Optional[int]
        """
        return self._reset_count
    
    @reset_count.setter
    def reset_count(self,value: Optional[int] = None) -> None:
        """
        Sets the resetCount property value. The number of times a PC device has hibernated or resumed
        Args:
            value: Value to set for the resetCount property.
        """
        self._reset_count = value
    
    @property
    def restart_count(self,) -> Optional[int]:
        """
        Gets the restartCount property value. The number of times a PC device has rebooted
        Returns: Optional[int]
        """
        return self._restart_count
    
    @restart_count.setter
    def restart_count(self,value: Optional[int] = None) -> None:
        """
        Sets the restartCount property value. The number of times a PC device has rebooted
        Args:
            value: Value to set for the restartCount property.
        """
        self._restart_count = value
    
    @property
    def safe_mode(self,) -> Optional[str]:
        """
        Gets the safeMode property value. Safe mode is a troubleshooting option for Windows that starts your computer in a limited state
        Returns: Optional[str]
        """
        return self._safe_mode
    
    @safe_mode.setter
    def safe_mode(self,value: Optional[str] = None) -> None:
        """
        Sets the safeMode property value. Safe mode is a troubleshooting option for Windows that starts your computer in a limited state
        Args:
            value: Value to set for the safeMode property.
        """
        self._safe_mode = value
    
    @property
    def secure_boot(self,) -> Optional[str]:
        """
        Gets the secureBoot property value. When Secure Boot is enabled, the core components must have the correct cryptographic signatures
        Returns: Optional[str]
        """
        return self._secure_boot
    
    @secure_boot.setter
    def secure_boot(self,value: Optional[str] = None) -> None:
        """
        Sets the secureBoot property value. When Secure Boot is enabled, the core components must have the correct cryptographic signatures
        Args:
            value: Value to set for the secureBoot property.
        """
        self._secure_boot = value
    
    @property
    def secure_boot_configuration_policy_finger_print(self,) -> Optional[str]:
        """
        Gets the secureBootConfigurationPolicyFingerPrint property value. Fingerprint of the Custom Secure Boot Configuration Policy
        Returns: Optional[str]
        """
        return self._secure_boot_configuration_policy_finger_print
    
    @secure_boot_configuration_policy_finger_print.setter
    def secure_boot_configuration_policy_finger_print(self,value: Optional[str] = None) -> None:
        """
        Sets the secureBootConfigurationPolicyFingerPrint property value. Fingerprint of the Custom Secure Boot Configuration Policy
        Args:
            value: Value to set for the secureBootConfigurationPolicyFingerPrint property.
        """
        self._secure_boot_configuration_policy_finger_print = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("attestationIdentityKey", self.attestation_identity_key)
        writer.write_str_value("bitLockerStatus", self.bit_locker_status)
        writer.write_str_value("bootAppSecurityVersion", self.boot_app_security_version)
        writer.write_str_value("bootDebugging", self.boot_debugging)
        writer.write_str_value("bootManagerSecurityVersion", self.boot_manager_security_version)
        writer.write_str_value("bootManagerVersion", self.boot_manager_version)
        writer.write_str_value("bootRevisionListInfo", self.boot_revision_list_info)
        writer.write_str_value("codeIntegrity", self.code_integrity)
        writer.write_str_value("codeIntegrityCheckVersion", self.code_integrity_check_version)
        writer.write_str_value("codeIntegrityPolicy", self.code_integrity_policy)
        writer.write_str_value("contentNamespaceUrl", self.content_namespace_url)
        writer.write_str_value("contentVersion", self.content_version)
        writer.write_str_value("dataExcutionPolicy", self.data_excution_policy)
        writer.write_str_value("deviceHealthAttestationStatus", self.device_health_attestation_status)
        writer.write_str_value("earlyLaunchAntiMalwareDriverProtection", self.early_launch_anti_malware_driver_protection)
        writer.write_str_value("healthAttestationSupportedStatus", self.health_attestation_supported_status)
        writer.write_str_value("healthStatusMismatchInfo", self.health_status_mismatch_info)
        writer.write_datetime_value("issuedDateTime", self.issued_date_time)
        writer.write_str_value("lastUpdateDateTime", self.last_update_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystemKernelDebugging", self.operating_system_kernel_debugging)
        writer.write_str_value("operatingSystemRevListInfo", self.operating_system_rev_list_info)
        writer.write_str_value("pcr0", self.pcr0)
        writer.write_str_value("pcrHashAlgorithm", self.pcr_hash_algorithm)
        writer.write_int_value("resetCount", self.reset_count)
        writer.write_int_value("restartCount", self.restart_count)
        writer.write_str_value("safeMode", self.safe_mode)
        writer.write_str_value("secureBoot", self.secure_boot)
        writer.write_str_value("secureBootConfigurationPolicyFingerPrint", self.secure_boot_configuration_policy_finger_print)
        writer.write_str_value("testSigning", self.test_signing)
        writer.write_str_value("tpmVersion", self.tpm_version)
        writer.write_str_value("virtualSecureMode", self.virtual_secure_mode)
        writer.write_str_value("windowsPE", self.windows_p_e)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def test_signing(self,) -> Optional[str]:
        """
        Gets the testSigning property value. When test signing is allowed, the device does not enforce signature validation during boot
        Returns: Optional[str]
        """
        return self._test_signing
    
    @test_signing.setter
    def test_signing(self,value: Optional[str] = None) -> None:
        """
        Sets the testSigning property value. When test signing is allowed, the device does not enforce signature validation during boot
        Args:
            value: Value to set for the testSigning property.
        """
        self._test_signing = value
    
    @property
    def tpm_version(self,) -> Optional[str]:
        """
        Gets the tpmVersion property value. The security version number of the Boot Application
        Returns: Optional[str]
        """
        return self._tpm_version
    
    @tpm_version.setter
    def tpm_version(self,value: Optional[str] = None) -> None:
        """
        Sets the tpmVersion property value. The security version number of the Boot Application
        Args:
            value: Value to set for the tpmVersion property.
        """
        self._tpm_version = value
    
    @property
    def virtual_secure_mode(self,) -> Optional[str]:
        """
        Gets the virtualSecureMode property value. VSM is a container that protects high value assets from a compromised kernel
        Returns: Optional[str]
        """
        return self._virtual_secure_mode
    
    @virtual_secure_mode.setter
    def virtual_secure_mode(self,value: Optional[str] = None) -> None:
        """
        Sets the virtualSecureMode property value. VSM is a container that protects high value assets from a compromised kernel
        Args:
            value: Value to set for the virtualSecureMode property.
        """
        self._virtual_secure_mode = value
    
    @property
    def windows_p_e(self,) -> Optional[str]:
        """
        Gets the windowsPE property value. Operating system running with limited services that is used to prepare a computer for Windows
        Returns: Optional[str]
        """
        return self._windows_p_e
    
    @windows_p_e.setter
    def windows_p_e(self,value: Optional[str] = None) -> None:
        """
        Sets the windowsPE property value. Operating system running with limited services that is used to prepare a computer for Windows
        Args:
            value: Value to set for the windowsPE property.
        """
        self._windows_p_e = value
    

