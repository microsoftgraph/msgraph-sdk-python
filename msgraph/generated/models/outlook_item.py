from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import calendar_sharing_message, contact, entity, event, event_message, event_message_request, event_message_response, message, post

from . import entity

@dataclass
class OutlookItem(entity.Entity):
    # The categories associated with the item
    categories: Optional[List[str]] = None
    # Identifies the version of the item. Every time the item is changed, changeKey changes as well. This allows Exchange to apply changes to the correct version of the object. Read-only.
    change_key: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.calendarSharingMessage":
                from . import calendar_sharing_message

                return calendar_sharing_message.CalendarSharingMessage()
            if mapping_value == "#microsoft.graph.contact":
                from . import contact

                return contact.Contact()
            if mapping_value == "#microsoft.graph.event":
                from . import event

                return event.Event()
            if mapping_value == "#microsoft.graph.eventMessage":
                from . import event_message

                return event_message.EventMessage()
            if mapping_value == "#microsoft.graph.eventMessageRequest":
                from . import event_message_request

                return event_message_request.EventMessageRequest()
            if mapping_value == "#microsoft.graph.eventMessageResponse":
                from . import event_message_response

                return event_message_response.EventMessageResponse()
            if mapping_value == "#microsoft.graph.message":
                from . import message

                return message.Message()
            if mapping_value == "#microsoft.graph.post":
                from . import post

                return post.Post()
        return OutlookItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import calendar_sharing_message, contact, entity, event, event_message, event_message_request, event_message_response, message, post

        fields: Dict[str, Callable[[Any], None]] = {
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "changeKey": lambda n : setattr(self, 'change_key', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_str_value("changeKey", self.change_key)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

