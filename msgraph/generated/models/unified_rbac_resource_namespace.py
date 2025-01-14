from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_rbac_resource_action import UnifiedRbacResourceAction

from .entity import Entity

@dataclass
class UnifiedRbacResourceNamespace(Entity, Parsable):
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceActions property
    resource_actions: Optional[list[UnifiedRbacResourceAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRbacResourceNamespace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRbacResourceNamespace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRbacResourceNamespace()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_rbac_resource_action import UnifiedRbacResourceAction

        from .entity import Entity
        from .unified_rbac_resource_action import UnifiedRbacResourceAction

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "resourceActions": lambda n : setattr(self, 'resource_actions', n.get_collection_of_object_values(UnifiedRbacResourceAction)),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("resourceActions", self.resource_actions)
    

