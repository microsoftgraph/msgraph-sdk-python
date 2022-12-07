from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment_info = lazy_import('msgraph.generated.models.attachment_info')

class CreateUploadSessionPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the createUploadSession method.
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
    
    @property
    def attachment_info(self,) -> Optional[attachment_info.AttachmentInfo]:
        """
        Gets the attachmentInfo property value. The attachmentInfo property
        Returns: Optional[attachment_info.AttachmentInfo]
        """
        return self._attachment_info
    
    @attachment_info.setter
    def attachment_info(self,value: Optional[attachment_info.AttachmentInfo] = None) -> None:
        """
        Sets the attachmentInfo property value. The attachmentInfo property
        Args:
            value: Value to set for the attachmentInfo property.
        """
        self._attachment_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new createUploadSessionPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The attachmentInfo property
        self._attachment_info: Optional[attachment_info.AttachmentInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CreateUploadSessionPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CreateUploadSessionPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CreateUploadSessionPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attachment_info": lambda n : setattr(self, 'attachment_info', n.get_object_value(attachment_info.AttachmentInfo)),
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
        writer.write_object_value("attachmentInfo", self.attachment_info)
        writer.write_additional_data_value(self.additional_data)
    

