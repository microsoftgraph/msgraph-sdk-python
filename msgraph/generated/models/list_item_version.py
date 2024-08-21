from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item_version import BaseItemVersion
    from .document_set_version import DocumentSetVersion
    from .field_value_set import FieldValueSet

from .base_item_version import BaseItemVersion

@dataclass
class ListItemVersion(BaseItemVersion):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.listItemVersion"
    # A collection of the fields and values for this version of the list item.
    fields: Optional[FieldValueSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListItemVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from .document_set_version import DocumentSetVersion

            return DocumentSetVersion()
        return ListItemVersion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .base_item_version import BaseItemVersion
        from .document_set_version import DocumentSetVersion
        from .field_value_set import FieldValueSet

        from .base_item_version import BaseItemVersion
        from .document_set_version import DocumentSetVersion
        from .field_value_set import FieldValueSet

        fields: Dict[str, Callable[[Any], None]] = {
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(FieldValueSet)),
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
        writer.write_object_value("fields", self.fields)
    

