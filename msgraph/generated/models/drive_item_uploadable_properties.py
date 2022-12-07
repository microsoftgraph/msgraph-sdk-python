from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

file_system_info = lazy_import('msgraph.generated.models.file_system_info')

class DriveItemUploadableProperties(AdditionalDataHolder, Parsable):
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
        Instantiates a new driveItemUploadableProperties and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Provides a user-visible description of the item. Read-write. Only on OneDrive Personal.
        self._description: Optional[str] = None
        # Provides an expected file size to perform a quota check prior to upload. Only on OneDrive Personal.
        self._file_size: Optional[int] = None
        # File system information on client. Read-write.
        self._file_system_info: Optional[file_system_info.FileSystemInfo] = None
        # The name of the item (filename and extension). Read-write.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveItemUploadableProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemUploadableProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriveItemUploadableProperties()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Provides a user-visible description of the item. Read-write. Only on OneDrive Personal.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Provides a user-visible description of the item. Read-write. Only on OneDrive Personal.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def file_size(self,) -> Optional[int]:
        """
        Gets the fileSize property value. Provides an expected file size to perform a quota check prior to upload. Only on OneDrive Personal.
        Returns: Optional[int]
        """
        return self._file_size
    
    @file_size.setter
    def file_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fileSize property value. Provides an expected file size to perform a quota check prior to upload. Only on OneDrive Personal.
        Args:
            value: Value to set for the fileSize property.
        """
        self._file_size = value
    
    @property
    def file_system_info(self,) -> Optional[file_system_info.FileSystemInfo]:
        """
        Gets the fileSystemInfo property value. File system information on client. Read-write.
        Returns: Optional[file_system_info.FileSystemInfo]
        """
        return self._file_system_info
    
    @file_system_info.setter
    def file_system_info(self,value: Optional[file_system_info.FileSystemInfo] = None) -> None:
        """
        Sets the fileSystemInfo property value. File system information on client. Read-write.
        Args:
            value: Value to set for the fileSystemInfo property.
        """
        self._file_system_info = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "file_size": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "file_system_info": lambda n : setattr(self, 'file_system_info', n.get_object_value(file_system_info.FileSystemInfo)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the item (filename and extension). Read-write.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the item (filename and extension). Read-write.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_str_value("description", self.description)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_object_value("fileSystemInfo", self.file_system_info)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

