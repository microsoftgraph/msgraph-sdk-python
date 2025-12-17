from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .windows_defender_product_status import WindowsDefenderProductStatus
    from .windows_device_health_state import WindowsDeviceHealthState
    from .windows_device_malware_state import WindowsDeviceMalwareState

from .entity import Entity

@dataclass
class WindowsProtectionState(Entity, Parsable):
    """
    Device protection status entity.
    """
    # Current anti malware version
    anti_malware_version: Optional[str] = None
    # Device malware list
    detected_malware_state: Optional[list[WindowsDeviceMalwareState]] = None
    # Indicates device's health state. The possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical. The possible values are: clean, fullScanPending, rebootPending, manualStepsPending, offlineScanPending, critical.
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
    # Product Status of Windows Defender Antivirus. The possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall. The possible values are: noStatus, serviceNotRunning, serviceStartedWithoutMalwareProtection, pendingFullScanDueToThreatAction, pendingRebootDueToThreatAction, pendingManualStepsDueToThreatAction, avSignaturesOutOfDate, asSignaturesOutOfDate, noQuickScanHappenedForSpecifiedPeriod, noFullScanHappenedForSpecifiedPeriod, systemInitiatedScanInProgress, systemInitiatedCleanInProgress, samplesPendingSubmission, productRunningInEvaluationMode, productRunningInNonGenuineMode, productExpired, offlineScanRequired, serviceShutdownAsPartOfSystemShutdown, threatRemediationFailedCritically, threatRemediationFailedNonCritically, noStatusFlagsSet, platformOutOfDate, platformUpdateInProgress, platformAboutToBeOutdated, signatureOrPlatformEndOfLifeIsPastOrIsImpending, windowsSModeSignaturesInUseOnNonWin10SInstall.
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
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsProtectionState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsProtectionState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsProtectionState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .windows_defender_product_status import WindowsDefenderProductStatus
        from .windows_device_health_state import WindowsDeviceHealthState
        from .windows_device_malware_state import WindowsDeviceMalwareState

        from .entity import Entity
        from .windows_defender_product_status import WindowsDefenderProductStatus
        from .windows_device_health_state import WindowsDeviceHealthState
        from .windows_device_malware_state import WindowsDeviceMalwareState

        fields: dict[str, Callable[[Any], None]] = {
            "antiMalwareVersion": lambda n : setattr(self, 'anti_malware_version', n.get_str_value()),
            "detectedMalwareState": lambda n : setattr(self, 'detected_malware_state', n.get_collection_of_object_values(WindowsDeviceMalwareState)),
            "deviceState": lambda n : setattr(self, 'device_state', n.get_collection_of_enum_values(WindowsDeviceHealthState)),
            "engineVersion": lambda n : setattr(self, 'engine_version', n.get_str_value()),
            "fullScanOverdue": lambda n : setattr(self, 'full_scan_overdue', n.get_bool_value()),
            "fullScanRequired": lambda n : setattr(self, 'full_scan_required', n.get_bool_value()),
            "isVirtualMachine": lambda n : setattr(self, 'is_virtual_machine', n.get_bool_value()),
            "lastFullScanDateTime": lambda n : setattr(self, 'last_full_scan_date_time', n.get_datetime_value()),
            "lastFullScanSignatureVersion": lambda n : setattr(self, 'last_full_scan_signature_version', n.get_str_value()),
            "lastQuickScanDateTime": lambda n : setattr(self, 'last_quick_scan_date_time', n.get_datetime_value()),
            "lastQuickScanSignatureVersion": lambda n : setattr(self, 'last_quick_scan_signature_version', n.get_str_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "malwareProtectionEnabled": lambda n : setattr(self, 'malware_protection_enabled', n.get_bool_value()),
            "networkInspectionSystemEnabled": lambda n : setattr(self, 'network_inspection_system_enabled', n.get_bool_value()),
            "productStatus": lambda n : setattr(self, 'product_status', n.get_collection_of_enum_values(WindowsDefenderProductStatus)),
            "quickScanOverdue": lambda n : setattr(self, 'quick_scan_overdue', n.get_bool_value()),
            "realTimeProtectionEnabled": lambda n : setattr(self, 'real_time_protection_enabled', n.get_bool_value()),
            "rebootRequired": lambda n : setattr(self, 'reboot_required', n.get_bool_value()),
            "signatureUpdateOverdue": lambda n : setattr(self, 'signature_update_overdue', n.get_bool_value()),
            "signatureVersion": lambda n : setattr(self, 'signature_version', n.get_str_value()),
            "tamperProtectionEnabled": lambda n : setattr(self, 'tamper_protection_enabled', n.get_bool_value()),
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
        writer.write_str_value("antiMalwareVersion", self.anti_malware_version)
        writer.write_collection_of_object_values("detectedMalwareState", self.detected_malware_state)
        writer.write_enum_value("deviceState", self.device_state)
        writer.write_str_value("engineVersion", self.engine_version)
        writer.write_bool_value("fullScanOverdue", self.full_scan_overdue)
        writer.write_bool_value("fullScanRequired", self.full_scan_required)
        writer.write_bool_value("isVirtualMachine", self.is_virtual_machine)
        writer.write_datetime_value("lastFullScanDateTime", self.last_full_scan_date_time)
        writer.write_str_value("lastFullScanSignatureVersion", self.last_full_scan_signature_version)
        writer.write_datetime_value("lastQuickScanDateTime", self.last_quick_scan_date_time)
        writer.write_str_value("lastQuickScanSignatureVersion", self.last_quick_scan_signature_version)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_bool_value("malwareProtectionEnabled", self.malware_protection_enabled)
        writer.write_bool_value("networkInspectionSystemEnabled", self.network_inspection_system_enabled)
        writer.write_enum_value("productStatus", self.product_status)
        writer.write_bool_value("quickScanOverdue", self.quick_scan_overdue)
        writer.write_bool_value("realTimeProtectionEnabled", self.real_time_protection_enabled)
        writer.write_bool_value("rebootRequired", self.reboot_required)
        writer.write_bool_value("signatureUpdateOverdue", self.signature_update_overdue)
        writer.write_str_value("signatureVersion", self.signature_version)
        writer.write_bool_value("tamperProtectionEnabled", self.tamper_protection_enabled)
    

