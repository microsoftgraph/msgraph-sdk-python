from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceHealthAttestationState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # TWhen an Attestation Identity Key (AIK) is present on a device, it indicates that the device has an endorsement key (EK) certificate.
    attestation_identity_key: Optional[str] = None
    # On or Off of BitLocker Drive Encryption
    bit_locker_status: Optional[str] = None
    # The security version number of the Boot Application
    boot_app_security_version: Optional[str] = None
    # When bootDebugging is enabled, the device is used in development and testing
    boot_debugging: Optional[str] = None
    # The security version number of the Boot Application
    boot_manager_security_version: Optional[str] = None
    # The version of the Boot Manager
    boot_manager_version: Optional[str] = None
    # The Boot Revision List that was loaded during initial boot on the attested device
    boot_revision_list_info: Optional[str] = None
    # When code integrity is enabled, code execution is restricted to integrity verified code
    code_integrity: Optional[str] = None
    # The version of the Boot Manager
    code_integrity_check_version: Optional[str] = None
    # The Code Integrity policy that is controlling the security of the boot environment
    code_integrity_policy: Optional[str] = None
    # The DHA report version. (Namespace version)
    content_namespace_url: Optional[str] = None
    # The HealthAttestation state schema version
    content_version: Optional[str] = None
    # DEP Policy defines a set of hardware and software technologies that perform additional checks on memory
    data_excution_policy: Optional[str] = None
    # The DHA report version. (Namespace version)
    device_health_attestation_status: Optional[str] = None
    # ELAM provides protection for the computers in your network when they start up
    early_launch_anti_malware_driver_protection: Optional[str] = None
    # This attribute indicates if DHA is supported for the device
    health_attestation_supported_status: Optional[str] = None
    # This attribute appears if DHA-Service detects an integrity issue
    health_status_mismatch_info: Optional[str] = None
    # The DateTime when device was evaluated or issued to MDM
    issued_date_time: Optional[datetime.datetime] = None
    # The Timestamp of the last update.
    last_update_date_time: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When operatingSystemKernelDebugging is enabled, the device is used in development and testing
    operating_system_kernel_debugging: Optional[str] = None
    # The Operating System Revision List that was loaded during initial boot on the attested device
    operating_system_rev_list_info: Optional[str] = None
    # Informational attribute that identifies the HASH algorithm that was used by TPM
    pcr_hash_algorithm: Optional[str] = None
    # The measurement that is captured in PCR[0]
    pcr0: Optional[str] = None
    # The number of times a PC device has hibernated or resumed
    reset_count: Optional[int] = None
    # The number of times a PC device has rebooted
    restart_count: Optional[int] = None
    # Safe mode is a troubleshooting option for Windows that starts your computer in a limited state
    safe_mode: Optional[str] = None
    # When Secure Boot is enabled, the core components must have the correct cryptographic signatures
    secure_boot: Optional[str] = None
    # Fingerprint of the Custom Secure Boot Configuration Policy
    secure_boot_configuration_policy_finger_print: Optional[str] = None
    # When test signing is allowed, the device does not enforce signature validation during boot
    test_signing: Optional[str] = None
    # The security version number of the Boot Application
    tpm_version: Optional[str] = None
    # VSM is a container that protects high value assets from a compromised kernel
    virtual_secure_mode: Optional[str] = None
    # Operating system running with limited services that is used to prepare a computer for Windows
    windows_p_e: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceHealthAttestationState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceHealthAttestationState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceHealthAttestationState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
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
            "pcr_hash_algorithm": lambda n : setattr(self, 'pcr_hash_algorithm', n.get_str_value()),
            "pcr0": lambda n : setattr(self, 'pcr0', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("attestation_identity_key", self.attestation_identity_key)
        writer.write_str_value("bit_locker_status", self.bit_locker_status)
        writer.write_str_value("boot_app_security_version", self.boot_app_security_version)
        writer.write_str_value("boot_debugging", self.boot_debugging)
        writer.write_str_value("boot_manager_security_version", self.boot_manager_security_version)
        writer.write_str_value("boot_manager_version", self.boot_manager_version)
        writer.write_str_value("boot_revision_list_info", self.boot_revision_list_info)
        writer.write_str_value("code_integrity", self.code_integrity)
        writer.write_str_value("code_integrity_check_version", self.code_integrity_check_version)
        writer.write_str_value("code_integrity_policy", self.code_integrity_policy)
        writer.write_str_value("content_namespace_url", self.content_namespace_url)
        writer.write_str_value("content_version", self.content_version)
        writer.write_str_value("data_excution_policy", self.data_excution_policy)
        writer.write_str_value("device_health_attestation_status", self.device_health_attestation_status)
        writer.write_str_value("early_launch_anti_malware_driver_protection", self.early_launch_anti_malware_driver_protection)
        writer.write_str_value("health_attestation_supported_status", self.health_attestation_supported_status)
        writer.write_str_value("health_status_mismatch_info", self.health_status_mismatch_info)
        writer.write_datetime_value("issued_date_time", self.issued_date_time)
        writer.write_str_value("last_update_date_time", self.last_update_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operating_system_kernel_debugging", self.operating_system_kernel_debugging)
        writer.write_str_value("operating_system_rev_list_info", self.operating_system_rev_list_info)
        writer.write_str_value("pcr_hash_algorithm", self.pcr_hash_algorithm)
        writer.write_str_value("pcr0", self.pcr0)
        writer.write_int_value("reset_count", self.reset_count)
        writer.write_int_value("restart_count", self.restart_count)
        writer.write_str_value("safe_mode", self.safe_mode)
        writer.write_str_value("secure_boot", self.secure_boot)
        writer.write_str_value("secure_boot_configuration_policy_finger_print", self.secure_boot_configuration_policy_finger_print)
        writer.write_str_value("test_signing", self.test_signing)
        writer.write_str_value("tpm_version", self.tpm_version)
        writer.write_str_value("virtual_secure_mode", self.virtual_secure_mode)
        writer.write_str_value("windows_p_e", self.windows_p_e)
        writer.write_additional_data_value(self.additional_data)
    

