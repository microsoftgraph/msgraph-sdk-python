from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import calendar_sharing_message_action, message

from . import message

@dataclass
class CalendarSharingMessage(message.Message):
    odata_type = "#microsoft.graph.calendarSharingMessage"
    # The canAccept property
    can_accept: Optional[bool] = None
    # The sharingMessageAction property
    sharing_message_action: Optional[calendar_sharing_message_action.CalendarSharingMessageAction] = None
    # The sharingMessageActions property
    sharing_message_actions: Optional[List[calendar_sharing_message_action.CalendarSharingMessageAction]] = None
    # The suggestedCalendarName property
    suggested_calendar_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarSharingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CalendarSharingMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import calendar_sharing_message_action, message

        from . import calendar_sharing_message_action, message

        fields: Dict[str, Callable[[Any], None]] = {
            "canAccept": lambda n : setattr(self, 'can_accept', n.get_bool_value()),
            "sharingMessageAction": lambda n : setattr(self, 'sharing_message_action', n.get_object_value(calendar_sharing_message_action.CalendarSharingMessageAction)),
            "sharingMessageActions": lambda n : setattr(self, 'sharing_message_actions', n.get_collection_of_object_values(calendar_sharing_message_action.CalendarSharingMessageAction)),
            "suggestedCalendarName": lambda n : setattr(self, 'suggested_calendar_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("canAccept", self.can_accept)
        writer.write_object_value("sharingMessageAction", self.sharing_message_action)
        writer.write_collection_of_object_values("sharingMessageActions", self.sharing_message_actions)
        writer.write_str_value("suggestedCalendarName", self.suggested_calendar_name)
    

