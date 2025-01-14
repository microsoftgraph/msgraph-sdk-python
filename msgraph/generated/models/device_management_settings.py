from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceManagementSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The number of days a device is allowed to go without checking in to remain compliant.
    device_compliance_checkin_threshold_days: Optional[int] = None
    # Is feature enabled or not for scheduled action for rule.
    is_scheduled_action_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device should be noncompliant when there is no compliance policy targeted when this is true
    secure_by_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagementSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deviceComplianceCheckinThresholdDays": lambda n : setattr(self, 'device_compliance_checkin_threshold_days', n.get_int_value()),
            "isScheduledActionEnabled": lambda n : setattr(self, 'is_scheduled_action_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secureByDefault": lambda n : setattr(self, 'secure_by_default', n.get_bool_value()),
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
        writer.write_int_value("deviceComplianceCheckinThresholdDays", self.device_compliance_checkin_threshold_days)
        writer.write_bool_value("isScheduledActionEnabled", self.is_scheduled_action_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("secureByDefault", self.secure_by_default)
        writer.write_additional_data_value(self.additional_data)
    

