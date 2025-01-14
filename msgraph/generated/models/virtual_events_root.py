from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .virtual_event import VirtualEvent
    from .virtual_event_townhall import VirtualEventTownhall
    from .virtual_event_webinar import VirtualEventWebinar

from .entity import Entity

@dataclass
class VirtualEventsRoot(Entity, Parsable):
    # The events property
    events: Optional[list[VirtualEvent]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of town halls. Nullable.
    townhalls: Optional[list[VirtualEventTownhall]] = None
    # A collection of webinars. Nullable.
    webinars: Optional[list[VirtualEventWebinar]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .virtual_event import VirtualEvent
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar

        from .entity import Entity
        from .virtual_event import VirtualEvent
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar

        fields: dict[str, Callable[[Any], None]] = {
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(VirtualEvent)),
            "townhalls": lambda n : setattr(self, 'townhalls', n.get_collection_of_object_values(VirtualEventTownhall)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_collection_of_object_values("townhalls", self.townhalls)
        writer.write_collection_of_object_values("webinars", self.webinars)
    

