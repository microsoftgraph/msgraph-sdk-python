from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy import ConditionalAccessPolicy
    from .entity import Entity
    from .named_location import NamedLocation

from .entity import Entity

@dataclass
class CaPoliciesDeletableRoot(Entity, Parsable):
    # The namedLocations property
    named_locations: Optional[list[NamedLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policies property
    policies: Optional[list[ConditionalAccessPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CaPoliciesDeletableRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CaPoliciesDeletableRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CaPoliciesDeletableRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy import ConditionalAccessPolicy
        from .entity import Entity
        from .named_location import NamedLocation

        from .conditional_access_policy import ConditionalAccessPolicy
        from .entity import Entity
        from .named_location import NamedLocation

        fields: dict[str, Callable[[Any], None]] = {
            "namedLocations": lambda n : setattr(self, 'named_locations', n.get_collection_of_object_values(NamedLocation)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
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
        writer.write_collection_of_object_values("namedLocations", self.named_locations)
        writer.write_collection_of_object_values("policies", self.policies)
    

