from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_action_type import DeviceComplianceActionType
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceComplianceActionItem(Entity):
    """
    Scheduled Action Configuration
    """
    # Scheduled Action Type Enum
    action_type: Optional[DeviceComplianceActionType] = None
    # Number of hours to wait till the action will be enforced. Valid values 0 to 8760
    grace_period_hours: Optional[int] = None
    # A list of group IDs to speicify who to CC this notification message to.
    notification_message_c_c_list: Optional[List[str]] = None
    # What notification Message template to use
    notification_template_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceActionItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceActionItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceActionItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_action_type import DeviceComplianceActionType
        from .entity import Entity

        from .device_compliance_action_type import DeviceComplianceActionType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "action_type": lambda n : setattr(self, 'action_type', n.get_enum_value(DeviceComplianceActionType)),
            "grace_period_hours": lambda n : setattr(self, 'grace_period_hours', n.get_int_value()),
            "notification_message_c_c_list": lambda n : setattr(self, 'notification_message_c_c_list', n.get_collection_of_primitive_values(str)),
            "notification_template_id": lambda n : setattr(self, 'notification_template_id', n.get_str_value()),
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
        writer.write_enum_value("action_type", self.action_type)
        writer.write_int_value("grace_period_hours", self.grace_period_hours)
        writer.write_collection_of_primitive_values("notification_message_c_c_list", self.notification_message_c_c_list)
        writer.write_str_value("notification_template_id", self.notification_template_id)
    

