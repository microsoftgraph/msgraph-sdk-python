from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item_version = lazy_import('msgraph.generated.models.base_item_version')
field_value_set = lazy_import('msgraph.generated.models.field_value_set')

class ListItemVersion(base_item_version.BaseItemVersion):
    def __init__(self,) -> None:
        """
        Instantiates a new ListItemVersion and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.listItemVersion"
        # A collection of the fields and values for this version of the list item.
        self._fields: Optional[field_value_set.FieldValueSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ListItemVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ListItemVersion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ListItemVersion()
    
    @property
    def fields(self,) -> Optional[field_value_set.FieldValueSet]:
        """
        Gets the fields property value. A collection of the fields and values for this version of the list item.
        Returns: Optional[field_value_set.FieldValueSet]
        """
        return self._fields
    
    @fields.setter
    def fields(self,value: Optional[field_value_set.FieldValueSet] = None) -> None:
        """
        Sets the fields property value. A collection of the fields and values for this version of the list item.
        Args:
            value: Value to set for the fields property.
        """
        self._fields = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("fields", self.fields)
    

