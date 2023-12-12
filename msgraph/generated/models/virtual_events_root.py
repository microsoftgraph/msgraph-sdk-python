from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event import VirtualEvent
    from .virtual_event_webinar import VirtualEventWebinar

from .entity import Entity

@dataclass
class VirtualEventsRoot(Entity):
    # The events property
    events: Optional[List[VirtualEvent]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The webinars property
    webinars: Optional[List[VirtualEventWebinar]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> VirtualEventsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event import VirtualEvent
        from .virtual_event_webinar import VirtualEventWebinar

        from .entity import Entity
        from .virtual_event import VirtualEvent
        from .virtual_event_webinar import VirtualEventWebinar

        fields: Dict[str, Callable[[Any], None]] = {
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(VirtualEvent)),
            "webinars": lambda n : setattr(self, 'webinars', n.get_collection_of_object_values(VirtualEventWebinar)),
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
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("webinars", self.webinars)
    

