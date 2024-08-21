from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .routing_mode import RoutingMode

from .entity import Entity

@dataclass
class AudioRoutingGroup(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # List of receiving participant ids.
    receivers: Optional[List[str]] = None
    # The routingMode property
    routing_mode: Optional[RoutingMode] = None
    # List of source participant ids.
    sources: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudioRoutingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudioRoutingGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AudioRoutingGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .routing_mode import RoutingMode

        from .entity import Entity
        from .routing_mode import RoutingMode

        fields: Dict[str, Callable[[Any], None]] = {
            "receivers": lambda n : setattr(self, 'receivers', n.get_collection_of_primitive_values(str)),
            "routingMode": lambda n : setattr(self, 'routing_mode', n.get_enum_value(RoutingMode)),
            "sources": lambda n : setattr(self, 'sources', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("receivers", self.receivers)
        writer.write_enum_value("routingMode", self.routing_mode)
        writer.write_collection_of_primitive_values("sources", self.sources)
    

