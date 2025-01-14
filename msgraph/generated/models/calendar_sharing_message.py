from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_sharing_message_action import CalendarSharingMessageAction
    from .message import Message

from .message import Message

@dataclass
class CalendarSharingMessage(Message, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.calendarSharingMessage"
    # The canAccept property
    can_accept: Optional[bool] = None
    # The sharingMessageAction property
    sharing_message_action: Optional[CalendarSharingMessageAction] = None
    # The sharingMessageActions property
    sharing_message_actions: Optional[list[CalendarSharingMessageAction]] = None
    # The suggestedCalendarName property
    suggested_calendar_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalendarSharingMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalendarSharingMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_sharing_message_action import CalendarSharingMessageAction
        from .message import Message

        from .calendar_sharing_message_action import CalendarSharingMessageAction
        from .message import Message

        fields: dict[str, Callable[[Any], None]] = {
            "canAccept": lambda n : setattr(self, 'can_accept', n.get_bool_value()),
            "sharingMessageAction": lambda n : setattr(self, 'sharing_message_action', n.get_object_value(CalendarSharingMessageAction)),
            "sharingMessageActions": lambda n : setattr(self, 'sharing_message_actions', n.get_collection_of_object_values(CalendarSharingMessageAction)),
            "suggestedCalendarName": lambda n : setattr(self, 'suggested_calendar_name', n.get_str_value()),
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
        writer.write_bool_value("canAccept", self.can_accept)
        writer.write_object_value("sharingMessageAction", self.sharing_message_action)
        writer.write_collection_of_object_values("sharingMessageActions", self.sharing_message_actions)
        writer.write_str_value("suggestedCalendarName", self.suggested_calendar_name)
    

