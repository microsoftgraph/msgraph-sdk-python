from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_action_type = lazy_import('msgraph.generated.models.device_compliance_action_type')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceComplianceActionItem(entity.Entity):
    """
    Scheduled Action Configuration
    """
    @property
    def action_type(self,) -> Optional[device_compliance_action_type.DeviceComplianceActionType]:
        """
        Gets the actionType property value. Scheduled Action Type Enum
        Returns: Optional[device_compliance_action_type.DeviceComplianceActionType]
        """
        return self._action_type
    
    @action_type.setter
    def action_type(self,value: Optional[device_compliance_action_type.DeviceComplianceActionType] = None) -> None:
        """
        Sets the actionType property value. Scheduled Action Type Enum
        Args:
            value: Value to set for the actionType property.
        """
        self._action_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceActionItem and sets the default values.
        """
        super().__init__()
        # Scheduled Action Type Enum
        self._action_type: Optional[device_compliance_action_type.DeviceComplianceActionType] = None
        # Number of hours to wait till the action will be enforced. Valid values 0 to 8760
        self._grace_period_hours: Optional[int] = None
        # A list of group IDs to speicify who to CC this notification message to.
        self._notification_message_c_c_list: Optional[List[str]] = None
        # What notification Message template to use
        self._notification_template_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
        fields = {
            "action_type": lambda n : setattr(self, 'action_type', n.get_enum_value(device_compliance_action_type.DeviceComplianceActionType)),
            "grace_period_hours": lambda n : setattr(self, 'grace_period_hours', n.get_int_value()),
            "notification_message_c_c_list": lambda n : setattr(self, 'notification_message_c_c_list', n.get_collection_of_primitive_values(str)),
            "notification_template_id": lambda n : setattr(self, 'notification_template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grace_period_hours(self,) -> Optional[int]:
        """
        Gets the gracePeriodHours property value. Number of hours to wait till the action will be enforced. Valid values 0 to 8760
        Returns: Optional[int]
        """
        return self._grace_period_hours
    
    @grace_period_hours.setter
    def grace_period_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the gracePeriodHours property value. Number of hours to wait till the action will be enforced. Valid values 0 to 8760
        Args:
            value: Value to set for the gracePeriodHours property.
        """
        self._grace_period_hours = value
    
    @property
    def notification_message_c_c_list(self,) -> Optional[List[str]]:
        """
        Gets the notificationMessageCCList property value. A list of group IDs to speicify who to CC this notification message to.
        Returns: Optional[List[str]]
        """
        return self._notification_message_c_c_list
    
    @notification_message_c_c_list.setter
    def notification_message_c_c_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notificationMessageCCList property value. A list of group IDs to speicify who to CC this notification message to.
        Args:
            value: Value to set for the notificationMessageCCList property.
        """
        self._notification_message_c_c_list = value
    
    @property
    def notification_template_id(self,) -> Optional[str]:
        """
        Gets the notificationTemplateId property value. What notification Message template to use
        Returns: Optional[str]
        """
        return self._notification_template_id
    
    @notification_template_id.setter
    def notification_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationTemplateId property value. What notification Message template to use
        Args:
            value: Value to set for the notificationTemplateId property.
        """
        self._notification_template_id = value
    
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
    

