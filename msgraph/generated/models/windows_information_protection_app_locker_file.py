from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class WindowsInformationProtectionAppLockerFile(entity.Entity):
    """
    Windows Information Protection AppLocker File
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsInformationProtectionAppLockerFile and sets the default values.
        """
        super().__init__()
        # The friendly name
        self._display_name: Optional[str] = None
        # File as a byte array
        self._file: Optional[bytes] = None
        # SHA256 hash of the file
        self._file_hash: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Version of the entity.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionAppLockerFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionAppLockerFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionAppLockerFile()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The friendly name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The friendly name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def file(self,) -> Optional[bytes]:
        """
        Gets the file property value. File as a byte array
        Returns: Optional[bytes]
        """
        return self._file
    
    @file.setter
    def file(self,value: Optional[bytes] = None) -> None:
        """
        Sets the file property value. File as a byte array
        Args:
            value: Value to set for the file property.
        """
        self._file = value
    
    @property
    def file_hash(self,) -> Optional[str]:
        """
        Gets the fileHash property value. SHA256 hash of the file
        Returns: Optional[str]
        """
        return self._file_hash
    
    @file_hash.setter
    def file_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the fileHash property value. SHA256 hash of the file
        Args:
            value: Value to set for the fileHash property.
        """
        self._file_hash = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file": lambda n : setattr(self, 'file', n.get_bytes_value()),
            "file_hash": lambda n : setattr(self, 'file_hash', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("file", self.file)
        writer.write_str_value("fileHash", self.file_hash)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the entity.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the entity.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

