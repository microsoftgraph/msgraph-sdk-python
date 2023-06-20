from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item_version, document_set_version, field_value_set

from . import base_item_version

@dataclass
class ListItemVersion(base_item_version.BaseItemVersion):
    odata_type = "#microsoft.graph.listItemVersion"
    # A collection of the fields and values for this version of the list item.
    fields: Optional[field_value_set.FieldValueSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ListItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ListItemVersion
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from . import document_set_version

            return document_set_version.DocumentSetVersion()
        return ListItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item_version, document_set_version, field_value_set

        from . import base_item_version, document_set_version, field_value_set

        fields: Dict[str, Callable[[Any], None]] = {
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(field_value_set.FieldValueSet)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("fields", self.fields)
    

