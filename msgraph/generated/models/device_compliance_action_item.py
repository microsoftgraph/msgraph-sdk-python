from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_action_type, entity

from . import entity

@dataclass
class DeviceComplianceActionItem(entity.Entity):
    """
    Scheduled Action Configuration
    """
    # Scheduled Action Type Enum
    action_type: Optional[device_compliance_action_type.DeviceComplianceActionType] = None
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
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceActionItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceActionItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_action_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(device_compliance_action_type.DeviceComplianceActionType)),
            "gracePeriodHours": lambda n : setattr(self, 'grace_period_hours', n.get_int_value()),
            "notificationMessageCCList": lambda n : setattr(self, 'notification_message_c_c_list', n.get_collection_of_primitive_values(str)),
            "notificationTemplateId": lambda n : setattr(self, 'notification_template_id', n.get_str_value()),
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
        writer.write_enum_value("actionType", self.action_type)
        writer.write_int_value("gracePeriodHours", self.grace_period_hours)
        writer.write_collection_of_primitive_values("notificationMessageCCList", self.notification_message_c_c_list)
        writer.write_str_value("notificationTemplateId", self.notification_template_id)
    

