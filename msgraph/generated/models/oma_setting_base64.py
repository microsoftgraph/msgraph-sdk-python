from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

oma_setting = lazy_import('msgraph.generated.models.oma_setting')

class OmaSettingBase64(oma_setting.OmaSetting):
    def __init__(self,) -> None:
        """
        Instantiates a new OmaSettingBase64 and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.omaSettingBase64"
        # File name associated with the Value property (.cer
        self._file_name: Optional[str] = None
        # Value. (Base64 encoded string)
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OmaSettingBase64:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OmaSettingBase64
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OmaSettingBase64()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. File name associated with the Value property (.cer
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. File name associated with the Value property (.cer
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("value", self.value)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Value. (Base64 encoded string)
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Value. (Base64 encoded string)
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

