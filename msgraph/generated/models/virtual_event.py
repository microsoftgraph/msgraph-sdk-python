from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_identity_set import CommunicationsIdentitySet
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .item_body import ItemBody
    from .virtual_event_session import VirtualEventSession
    from .virtual_event_status import VirtualEventStatus
    from .virtual_event_webinar import VirtualEventWebinar

from .entity import Entity

@dataclass
class VirtualEvent(Entity):
    # Identity information for the creator of the virtual event. Inherited from virtualEvent.
    created_by: Optional[CommunicationsIdentitySet] = None
    # Description of the virtual event.
    description: Optional[ItemBody] = None
    # Display name of the virtual event.
    display_name: Optional[str] = None
    # End time of the virtual event. The timeZone property can be set to any of the time zones currently supported by Windows.
    end_date_time: Optional[DateTimeTimeZone] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sessions for the virtual event.
    sessions: Optional[List[VirtualEventSession]] = None
    # Start time of the virtual event. The timeZone property can be set to any of the time zones currently supported by Windows.
    start_date_time: Optional[DateTimeTimeZone] = None
    # Status of the virtual event. The possible values are: draft, published, canceled, unknownFutureValue.
    status: Optional[VirtualEventStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEvent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinar".casefold():
            from .virtual_event_webinar import VirtualEventWebinar

            return VirtualEventWebinar()
        return VirtualEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .communications_identity_set import CommunicationsIdentitySet
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .item_body import ItemBody
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_status import VirtualEventStatus
        from .virtual_event_webinar import VirtualEventWebinar

        from .communications_identity_set import CommunicationsIdentitySet
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .item_body import ItemBody
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_status import VirtualEventStatus
        from .virtual_event_webinar import VirtualEventWebinar

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(CommunicationsIdentitySet)),
            "description": lambda n : setattr(self, 'description', n.get_object_value(ItemBody)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "sessions": lambda n : setattr(self, 'sessions', n.get_collection_of_object_values(VirtualEventSession)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(VirtualEventStatus)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_object_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_collection_of_object_values("sessions", self.sessions)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

