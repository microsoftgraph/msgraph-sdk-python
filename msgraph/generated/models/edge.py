from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, internet_explorer_mode

from . import entity

@dataclass
class Edge(entity.Entity):
    # A container for Internet Explorer mode resources.
    internet_explorer_mode: Optional[internet_explorer_mode.InternetExplorerMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Edge:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Edge
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Edge()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, internet_explorer_mode

        fields: Dict[str, Callable[[Any], None]] = {
            "internetExplorerMode": lambda n : setattr(self, 'internet_explorer_mode', n.get_object_value(internet_explorer_mode.InternetExplorerMode)),
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
        writer.write_object_value("internetExplorerMode", self.internet_explorer_mode)
    

