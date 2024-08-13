from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceProtectionOverview(AdditionalDataHolder, BackedModel, Parsable):
    """
    Hardware information of a given device.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates number of devices reporting as clean
    clean_device_count: Optional[int] = None
    # Indicates number of devices with critical failures
    critical_failures_device_count: Optional[int] = None
    # Indicates number of devices with inactive threat agent
    inactive_threat_agent_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates number of devices pending full scan
    pending_full_scan_device_count: Optional[int] = None
    # Indicates number of devices with pending manual steps
    pending_manual_steps_device_count: Optional[int] = None
    # Indicates number of pending offline scan devices
    pending_offline_scan_device_count: Optional[int] = None
    # Indicates the number of devices that have a pending full scan. Valid values -2147483648 to 2147483647
    pending_quick_scan_device_count: Optional[int] = None
    # Indicates number of devices pending restart
    pending_restart_device_count: Optional[int] = None
    # Indicates number of devices with an old signature
    pending_signature_update_device_count: Optional[int] = None
    # Total device count.
    total_reported_device_count: Optional[int] = None
    # Indicates number of devices with threat agent state as unknown
    unknown_state_threat_agent_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceProtectionOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceProtectionOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceProtectionOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "cleanDeviceCount": lambda n : setattr(self, 'clean_device_count', n.get_int_value()),
            "criticalFailuresDeviceCount": lambda n : setattr(self, 'critical_failures_device_count', n.get_int_value()),
            "inactiveThreatAgentDeviceCount": lambda n : setattr(self, 'inactive_threat_agent_device_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pendingFullScanDeviceCount": lambda n : setattr(self, 'pending_full_scan_device_count', n.get_int_value()),
            "pendingManualStepsDeviceCount": lambda n : setattr(self, 'pending_manual_steps_device_count', n.get_int_value()),
            "pendingOfflineScanDeviceCount": lambda n : setattr(self, 'pending_offline_scan_device_count', n.get_int_value()),
            "pendingQuickScanDeviceCount": lambda n : setattr(self, 'pending_quick_scan_device_count', n.get_int_value()),
            "pendingRestartDeviceCount": lambda n : setattr(self, 'pending_restart_device_count', n.get_int_value()),
            "pendingSignatureUpdateDeviceCount": lambda n : setattr(self, 'pending_signature_update_device_count', n.get_int_value()),
            "totalReportedDeviceCount": lambda n : setattr(self, 'total_reported_device_count', n.get_int_value()),
            "unknownStateThreatAgentDeviceCount": lambda n : setattr(self, 'unknown_state_threat_agent_device_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("cleanDeviceCount", self.clean_device_count)
        writer.write_int_value("criticalFailuresDeviceCount", self.critical_failures_device_count)
        writer.write_int_value("inactiveThreatAgentDeviceCount", self.inactive_threat_agent_device_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pendingFullScanDeviceCount", self.pending_full_scan_device_count)
        writer.write_int_value("pendingManualStepsDeviceCount", self.pending_manual_steps_device_count)
        writer.write_int_value("pendingOfflineScanDeviceCount", self.pending_offline_scan_device_count)
        writer.write_int_value("pendingQuickScanDeviceCount", self.pending_quick_scan_device_count)
        writer.write_int_value("pendingRestartDeviceCount", self.pending_restart_device_count)
        writer.write_int_value("pendingSignatureUpdateDeviceCount", self.pending_signature_update_device_count)
        writer.write_int_value("totalReportedDeviceCount", self.total_reported_device_count)
        writer.write_int_value("unknownStateThreatAgentDeviceCount", self.unknown_state_threat_agent_device_count)
        writer.write_additional_data_value(self.additional_data)
    

