from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .internet_explorer_mode import InternetExplorerMode

from .entity import Entity

@dataclass
class Edge(Entity, Parsable):
    # A container for Internet Explorer mode resources.
    internet_explorer_mode: Optional[InternetExplorerMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Edge:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Edge
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Edge()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .internet_explorer_mode import InternetExplorerMode

        from .entity import Entity
        from .internet_explorer_mode import InternetExplorerMode

        fields: dict[str, Callable[[Any], None]] = {
            "internetExplorerMode": lambda n : setattr(self, 'internet_explorer_mode', n.get_object_value(InternetExplorerMode)),
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
        writer.write_object_value("internetExplorerMode", self.internet_explorer_mode)
    

