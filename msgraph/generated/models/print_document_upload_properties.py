from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class PrintDocumentUploadProperties(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new printDocumentUploadProperties and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The document's content (MIME) type.
        self._content_type: Optional[str] = None
        # The document's name.
        self._document_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The document's size in bytes.
        self._size: Optional[int] = None
    
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
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The document's content (MIME) type.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The document's content (MIME) type.
        Args:
            value: Value to set for the content_type property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintDocumentUploadProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintDocumentUploadProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintDocumentUploadProperties()
    
    @property
    def document_name(self,) -> Optional[str]:
        """
        Gets the documentName property value. The document's name.
        Returns: Optional[str]
        """
        return self._document_name
    
    @document_name.setter
    def document_name(self,value: Optional[str] = None) -> None:
        """
        Sets the documentName property value. The document's name.
        Args:
            value: Value to set for the document_name property.
        """
        self._document_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "documentName": lambda n : setattr(self, 'document_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contentType", self.content_type)
        writer.write_str_value("documentName", self.document_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("size", self.size)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. The document's size in bytes.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. The document's size in bytes.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    

