from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

extension = lazy_import('msgraph.generated.models.extension')

class OpenTypeExtension(extension.Extension):
    def __init__(self,) -> None:
        """
        Instantiates a new OpenTypeExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.openTypeExtension"
        # A unique text identifier for an open type data extension. Required.
        self._extension_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenTypeExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenTypeExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OpenTypeExtension()
    
    @property
    def extension_name(self,) -> Optional[str]:
        """
        Gets the extensionName property value. A unique text identifier for an open type data extension. Required.
        Returns: Optional[str]
        """
        return self._extension_name
    
    @extension_name.setter
    def extension_name(self,value: Optional[str] = None) -> None:
        """
        Sets the extensionName property value. A unique text identifier for an open type data extension. Required.
        Args:
            value: Value to set for the extensionName property.
        """
        self._extension_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "extension_name": lambda n : setattr(self, 'extension_name', n.get_str_value()),
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
        writer.write_str_value("extensionName", self.extension_name)
    

