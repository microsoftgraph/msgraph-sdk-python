from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_defender_product_status import WindowsDefenderProductStatus
    from .windows_device_health_state import WindowsDeviceHealthState
    from .windows_device_malware_state import WindowsDeviceMalwareState

from .entity import Entity

@dataclass
class WindowsProtectionState(Entity):
    """
    Device protection status entity.
    """
    # Current anti malware version
    anti_malware_version: Optional[str] = None
    # Device malware list
    detected_malware_state: Optional[List[WindowsDeviceMalwareState]] = None
    # Indicates device's health state. Possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical. Possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical.
    device_state: Optional[WindowsDeviceHealthState] = None
    # Current endpoint protection engine's version
    engine_version: Optional[str] = None
    # When TRUE indicates full scan is overdue, when FALSE indicates full scan is not overdue. Defaults to setting on client device.
    full_scan_overdue: Optional[bool] = None
    # When TRUE indicates full scan is required, when FALSE indicates full scan is not required. Defaults to setting on client device.
    full_scan_required: Optional[bool] = None
    # When TRUE indicates the device is a virtual machine, when FALSE indicates the device is not a virtual machine. Defaults to setting on client device.
    is_virtual_machine: Optional[bool] = None
    # Last quick scan datetime
    last_full_scan_date_time: Optional[datetime.datetime] = None
    # Last full scan signature version
    last_full_scan_signature_version: Optional[str] = None
    # Last quick scan datetime
    last_quick_scan_date_time: Optional[datetime.datetime] = None
    # Last quick scan signature version
    last_quick_scan_signature_version: Optional[str] = None
    # Last device health status reported time
    last_reported_date_time: Optional[datetime.datetime] = None
    # When TRUE indicates anti malware is enabled when FALSE indicates anti malware is not enabled.
    malware_protection_enabled: Optional[bool] = None
    # When TRUE indicates network inspection system enabled, when FALSE indicates network inspection system is not enabled. Defaults to setting on client device.
    network_inspection_system_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Product Status of Windows Defender Antivirus. Possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall. Possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall.
    product_status: Optional[WindowsDefenderProductStatus] = None
    # When TRUE indicates quick scan is overdue, when FALSE indicates quick scan is not overdue. Defaults to setting on client device.
    quick_scan_overdue: Optional[bool] = None
    # When TRUE indicates real time protection is enabled, when FALSE indicates real time protection is not enabled. Defaults to setting on client device.
    real_time_protection_enabled: Optional[bool] = None
    # When TRUE indicates reboot is required, when FALSE indicates when TRUE indicates reboot is not required. Defaults to setting on client device.
    reboot_required: Optional[bool] = None
    # When TRUE indicates signature is out of date, when FALSE indicates signature is not out of date. Defaults to setting on client device.
    signature_update_overdue: Optional[bool] = None
    # Current malware definitions version
    signature_version: Optional[str] = None
    # When TRUE indicates the Windows Defender tamper protection feature is enabled, when FALSE indicates the Windows Defender tamper protection feature is not enabled. Defaults to setting on client device.
    tamper_protection_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsProtectionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsProtectionState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsProtectionState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_defender_product_status import WindowsDefenderProductStatus
        from .windows_device_health_state import WindowsDeviceHealthState
        from .windows_device_malware_state import WindowsDeviceMalwareState

        from .entity import Entity
        from .windows_defender_product_status import WindowsDefenderProductStatus
        from .windows_device_health_state import WindowsDeviceHealthState
        from .windows_device_malware_state import WindowsDeviceMalwareState

        fields: Dict[str, Callable[[Any], None]] = {
            "anti_malware_version": lambda n : setattr(self, 'anti_malware_version', n.get_str_value()),
            "detected_malware_state": lambda n : setattr(self, 'detected_malware_state', n.get_collection_of_object_values(WindowsDeviceMalwareState)),
            "device_state": lambda n : setattr(self, 'device_state', n.get_collection_of_enum_values(WindowsDeviceHealthState)),
            "engine_version": lambda n : setattr(self, 'engine_version', n.get_str_value()),
            "full_scan_overdue": lambda n : setattr(self, 'full_scan_overdue', n.get_bool_value()),
            "full_scan_required": lambda n : setattr(self, 'full_scan_required', n.get_bool_value()),
            "is_virtual_machine": lambda n : setattr(self, 'is_virtual_machine', n.get_bool_value()),
            "last_full_scan_date_time": lambda n : setattr(self, 'last_full_scan_date_time', n.get_datetime_value()),
            "last_full_scan_signature_version": lambda n : setattr(self, 'last_full_scan_signature_version', n.get_str_value()),
            "last_quick_scan_date_time": lambda n : setattr(self, 'last_quick_scan_date_time', n.get_datetime_value()),
            "last_quick_scan_signature_version": lambda n : setattr(self, 'last_quick_scan_signature_version', n.get_str_value()),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malware_protection_enabled": lambda n : setattr(self, 'malware_protection_enabled', n.get_bool_value()),
            "network_inspection_system_enabled": lambda n : setattr(self, 'network_inspection_system_enabled', n.get_bool_value()),
            "product_status": lambda n : setattr(self, 'product_status', n.get_collection_of_enum_values(WindowsDefenderProductStatus)),
            "quick_scan_overdue": lambda n : setattr(self, 'quick_scan_overdue', n.get_bool_value()),
            "real_time_protection_enabled": lambda n : setattr(self, 'real_time_protection_enabled', n.get_bool_value()),
            "reboot_required": lambda n : setattr(self, 'reboot_required', n.get_bool_value()),
            "signature_update_overdue": lambda n : setattr(self, 'signature_update_overdue', n.get_bool_value()),
            "signature_version": lambda n : setattr(self, 'signature_version', n.get_str_value()),
            "tamper_protection_enabled": lambda n : setattr(self, 'tamper_protection_enabled', n.get_bool_value()),
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
        writer.write_str_value("anti_malware_version", self.anti_malware_version)
        writer.write_collection_of_object_values("detected_malware_state", self.detected_malware_state)
        writer.write_enum_value("device_state", self.device_state)
        writer.write_str_value("engine_version", self.engine_version)
        writer.write_bool_value("full_scan_overdue", self.full_scan_overdue)
        writer.write_bool_value("full_scan_required", self.full_scan_required)
        writer.write_bool_value("is_virtual_machine", self.is_virtual_machine)
        writer.write_datetime_value("last_full_scan_date_time", self.last_full_scan_date_time)
        writer.write_str_value("last_full_scan_signature_version", self.last_full_scan_signature_version)
        writer.write_datetime_value("last_quick_scan_date_time", self.last_quick_scan_date_time)
        writer.write_str_value("last_quick_scan_signature_version", self.last_quick_scan_signature_version)
        writer.write_datetime_value("last_reported_date_time", self.last_reported_date_time)
        writer.write_bool_value("malware_protection_enabled", self.malware_protection_enabled)
        writer.write_bool_value("network_inspection_system_enabled", self.network_inspection_system_enabled)
        writer.write_enum_value("product_status", self.product_status)
        writer.write_bool_value("quick_scan_overdue", self.quick_scan_overdue)
        writer.write_bool_value("real_time_protection_enabled", self.real_time_protection_enabled)
        writer.write_bool_value("reboot_required", self.reboot_required)
        writer.write_bool_value("signature_update_overdue", self.signature_update_overdue)
        writer.write_str_value("signature_version", self.signature_version)
        writer.write_bool_value("tamper_protection_enabled", self.tamper_protection_enabled)
    

