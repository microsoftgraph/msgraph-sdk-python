from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

calendar_sharing_message_action = lazy_import('msgraph.generated.models.calendar_sharing_message_action')
message = lazy_import('msgraph.generated.models.message')

class CalendarSharingMessage(message.Message):
    @property
    def can_accept(self,) -> Optional[bool]:
        """
        Gets the canAccept property value. The canAccept property
        Returns: Optional[bool]
        """
        return self._can_accept
    
    @can_accept.setter
    def can_accept(self,value: Optional[bool] = None) -> None:
        """
        Sets the canAccept property value. The canAccept property
        Args:
            value: Value to set for the canAccept property.
        """
        self._can_accept = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CalendarSharingMessage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.calendarSharingMessage"
        # The canAccept property
        self._can_accept: Optional[bool] = None
        # The sharingMessageAction property
        self._sharing_message_action: Optional[calendar_sharing_message_action.CalendarSharingMessageAction] = None
        # The sharingMessageActions property
        self._sharing_message_actions: Optional[List[calendar_sharing_message_action.CalendarSharingMessageAction]] = None
        # The suggestedCalendarName property
        self._suggested_calendar_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarSharingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CalendarSharingMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "can_accept": lambda n : setattr(self, 'can_accept', n.get_bool_value()),
            "sharing_message_action": lambda n : setattr(self, 'sharing_message_action', n.get_object_value(calendar_sharing_message_action.CalendarSharingMessageAction)),
            "sharing_message_actions": lambda n : setattr(self, 'sharing_message_actions', n.get_collection_of_object_values(calendar_sharing_message_action.CalendarSharingMessageAction)),
            "suggested_calendar_name": lambda n : setattr(self, 'suggested_calendar_name', n.get_str_value()),
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
        writer.write_bool_value("canAccept", self.can_accept)
        writer.write_object_value("sharingMessageAction", self.sharing_message_action)
        writer.write_collection_of_object_values("sharingMessageActions", self.sharing_message_actions)
        writer.write_str_value("suggestedCalendarName", self.suggested_calendar_name)
    
    @property
    def sharing_message_action(self,) -> Optional[calendar_sharing_message_action.CalendarSharingMessageAction]:
        """
        Gets the sharingMessageAction property value. The sharingMessageAction property
        Returns: Optional[calendar_sharing_message_action.CalendarSharingMessageAction]
        """
        return self._sharing_message_action
    
    @sharing_message_action.setter
    def sharing_message_action(self,value: Optional[calendar_sharing_message_action.CalendarSharingMessageAction] = None) -> None:
        """
        Sets the sharingMessageAction property value. The sharingMessageAction property
        Args:
            value: Value to set for the sharingMessageAction property.
        """
        self._sharing_message_action = value
    
    @property
    def sharing_message_actions(self,) -> Optional[List[calendar_sharing_message_action.CalendarSharingMessageAction]]:
        """
        Gets the sharingMessageActions property value. The sharingMessageActions property
        Returns: Optional[List[calendar_sharing_message_action.CalendarSharingMessageAction]]
        """
        return self._sharing_message_actions
    
    @sharing_message_actions.setter
    def sharing_message_actions(self,value: Optional[List[calendar_sharing_message_action.CalendarSharingMessageAction]] = None) -> None:
        """
        Sets the sharingMessageActions property value. The sharingMessageActions property
        Args:
            value: Value to set for the sharingMessageActions property.
        """
        self._sharing_message_actions = value
    
    @property
    def suggested_calendar_name(self,) -> Optional[str]:
        """
        Gets the suggestedCalendarName property value. The suggestedCalendarName property
        Returns: Optional[str]
        """
        return self._suggested_calendar_name
    
    @suggested_calendar_name.setter
    def suggested_calendar_name(self,value: Optional[str] = None) -> None:
        """
        Sets the suggestedCalendarName property value. The suggestedCalendarName property
        Args:
            value: Value to set for the suggestedCalendarName property.
        """
        self._suggested_calendar_name = value
    

