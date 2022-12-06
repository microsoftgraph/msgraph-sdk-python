from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AddCopyFromContentTypeHubPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the addCopyFromContentTypeHub method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new addCopyFromContentTypeHubPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The contentTypeId property
        self._content_type_id: Optional[str] = None
    
    @property
    def content_type_id(self,) -> Optional[str]:
        """
        Gets the contentTypeId property value. The contentTypeId property
        Returns: Optional[str]
        """
        return self._content_type_id
    
    @content_type_id.setter
    def content_type_id(self,value: Optional[str] = None) -> None:
        """
        Sets the contentTypeId property value. The contentTypeId property
        Args:
            value: Value to set for the contentTypeId property.
        """
        self._content_type_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddCopyFromContentTypeHubPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddCopyFromContentTypeHubPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddCopyFromContentTypeHubPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_type_id": lambda n : setattr(self, 'content_type_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contentTypeId", self.content_type_id)
        writer.write_additional_data_value(self.additional_data)
    

