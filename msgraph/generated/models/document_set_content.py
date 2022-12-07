from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

content_type_info = lazy_import('msgraph.generated.models.content_type_info')

class DocumentSetContent(AdditionalDataHolder, Parsable):
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
        Instantiates a new documentSetContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Content type information of the file.
        self._content_type: Optional[content_type_info.ContentTypeInfo] = None
        # Name of the file in resource folder that should be added as a default content or a template in the document set.
        self._file_name: Optional[str] = None
        # Folder name in which the file will be placed when a new document set is created in the library.
        self._folder_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def content_type(self,) -> Optional[content_type_info.ContentTypeInfo]:
        """
        Gets the contentType property value. Content type information of the file.
        Returns: Optional[content_type_info.ContentTypeInfo]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[content_type_info.ContentTypeInfo] = None) -> None:
        """
        Sets the contentType property value. Content type information of the file.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSetContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSetContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentSetContent()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. Name of the file in resource folder that should be added as a default content or a template in the document set.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. Name of the file in resource folder that should be added as a default content or a template in the document set.
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    @property
    def folder_name(self,) -> Optional[str]:
        """
        Gets the folderName property value. Folder name in which the file will be placed when a new document set is created in the library.
        Returns: Optional[str]
        """
        return self._folder_name
    
    @folder_name.setter
    def folder_name(self,value: Optional[str] = None) -> None:
        """
        Sets the folderName property value. Folder name in which the file will be placed when a new document set is created in the library.
        Args:
            value: Value to set for the folderName property.
        """
        self._folder_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_type": lambda n : setattr(self, 'content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "folder_name": lambda n : setattr(self, 'folder_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the OdataType property.
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
        writer.write_object_value("contentType", self.content_type)
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("folderName", self.folder_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

