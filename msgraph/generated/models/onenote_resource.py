from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

onenote_entity_base_model = lazy_import('msgraph.generated.models.onenote_entity_base_model')

class OnenoteResource(onenote_entity_base_model.OnenoteEntityBaseModel):
    def __init__(self,) -> None:
        """
        Instantiates a new OnenoteResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onenoteResource"
        # The content stream
        self._content: Optional[bytes] = None
        # The URL for downloading the content
        self._content_url: Optional[str] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content stream
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content stream
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def content_url(self,) -> Optional[str]:
        """
        Gets the contentUrl property value. The URL for downloading the content
        Returns: Optional[str]
        """
        return self._content_url
    
    @content_url.setter
    def content_url(self,value: Optional[str] = None) -> None:
        """
        Sets the contentUrl property value. The URL for downloading the content
        Args:
            value: Value to set for the contentUrl property.
        """
        self._content_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenoteResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenoteResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "content_url": lambda n : setattr(self, 'content_url', n.get_str_value()),
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
        writer.write_object_value("content", self.content)
        writer.write_str_value("contentUrl", self.content_url)
    

