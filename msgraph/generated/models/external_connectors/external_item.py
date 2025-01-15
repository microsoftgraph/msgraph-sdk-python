from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .acl import Acl
    from .external_activity import ExternalActivity
    from .external_item_content import ExternalItemContent
    from .properties import Properties

from ..entity import Entity

@dataclass
class ExternalItem(Entity, Parsable):
    # An array of access control entries. Each entry specifies the access granted to a user or group. Required.
    acl: Optional[list[Acl]] = None
    # Returns a list of activities performed on the item. Write-only.
    activities: Optional[list[ExternalActivity]] = None
    # A plain-text  representation of the contents of the item. The text in this property is full-text indexed. Optional.
    content: Optional[ExternalItemContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A property bag with the properties of the item. The properties MUST conform to the schema defined for the externalConnection. Required.
    properties: Optional[Properties] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExternalItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExternalItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExternalItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .acl import Acl
        from .external_activity import ExternalActivity
        from .external_item_content import ExternalItemContent
        from .properties import Properties

        from ..entity import Entity
        from .acl import Acl
        from .external_activity import ExternalActivity
        from .external_item_content import ExternalItemContent
        from .properties import Properties

        fields: dict[str, Callable[[Any], None]] = {
            "acl": lambda n : setattr(self, 'acl', n.get_collection_of_object_values(Acl)),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(ExternalActivity)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(ExternalItemContent)),
            "properties": lambda n : setattr(self, 'properties', n.get_object_value(Properties)),
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
        writer.write_collection_of_object_values("acl", self.acl)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_object_value("content", self.content)
        writer.write_object_value("properties", self.properties)
    

