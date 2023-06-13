from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceManagementSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The number of days a device is allowed to go without checking in to remain compliant.
    device_compliance_checkin_threshold_days: Optional[int] = None
    # Is feature enabled or not for scheduled action for rule.
    is_scheduled_action_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device should be noncompliant when there is no compliance policy targeted when this is true
    secure_by_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deviceComplianceCheckinThresholdDays": lambda n : setattr(self, 'device_compliance_checkin_threshold_days', n.get_int_value()),
            "isScheduledActionEnabled": lambda n : setattr(self, 'is_scheduled_action_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secureByDefault": lambda n : setattr(self, 'secure_by_default', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("deviceComplianceCheckinThresholdDays", self.device_compliance_checkin_threshold_days)
        writer.write_bool_value("isScheduledActionEnabled", self.is_scheduled_action_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("secureByDefault", self.secure_by_default)
        writer.write_additional_data_value(self.additional_data)
    

