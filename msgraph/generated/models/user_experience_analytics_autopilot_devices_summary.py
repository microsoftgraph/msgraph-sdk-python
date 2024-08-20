from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceAnalyticsAutopilotDevicesSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience analytics summary of Devices not windows autopilot ready.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The count of intune devices that are not autopilot registerd. Read-only.
    devices_not_autopilot_registered: Optional[int] = None
    # The count of intune devices not autopilot profile assigned. Read-only.
    devices_without_autopilot_profile_assigned: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The count of windows 10 devices that are Intune and co-managed. Read-only.
    total_windows10_devices_without_tenant_attached: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAutopilotDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAutopilotDevicesSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAutopilotDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "devicesNotAutopilotRegistered": lambda n : setattr(self, 'devices_not_autopilot_registered', n.get_int_value()),
            "devicesWithoutAutopilotProfileAssigned": lambda n : setattr(self, 'devices_without_autopilot_profile_assigned', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalWindows10DevicesWithoutTenantAttached": lambda n : setattr(self, 'total_windows10_devices_without_tenant_attached', n.get_int_value()),
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
        writer.write_int_value("devicesNotAutopilotRegistered", self.devices_not_autopilot_registered)
        writer.write_int_value("devicesWithoutAutopilotProfileAssigned", self.devices_without_autopilot_profile_assigned)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalWindows10DevicesWithoutTenantAttached", self.total_windows10_devices_without_tenant_attached)
        writer.write_additional_data_value(self.additional_data)
    

