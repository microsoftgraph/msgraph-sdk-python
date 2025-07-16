from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .property_ import Property_

from ..entity import Entity

@dataclass
class Schema(Entity, Parsable):
    # Must be set to microsoft.graph.externalConnector.externalItem. Required.
    base_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The properties defined for the items in the connection. The minimum number of properties is one, the maximum is 128.
    properties: Optional[list[Property_]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Schema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Schema
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Schema()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .property_ import Property_

        from ..entity import Entity
        from .property_ import Property_

        fields: dict[str, Callable[[Any], None]] = {
            "baseType": lambda n : setattr(self, 'base_type', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(Property_)),
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
        writer.write_str_value("baseType", self.base_type)
        writer.write_collection_of_object_values("properties", self.properties)
    

