from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_information_protection_app = lazy_import('msgraph.generated.models.windows_information_protection_app')

class WindowsInformationProtectionDesktopApp(windows_information_protection_app.WindowsInformationProtectionApp):
    @property
    def binary_name(self,) -> Optional[str]:
        """
        Gets the binaryName property value. The binary name.
        Returns: Optional[str]
        """
        return self._binary_name
    
    @binary_name.setter
    def binary_name(self,value: Optional[str] = None) -> None:
        """
        Sets the binaryName property value. The binary name.
        Args:
            value: Value to set for the binaryName property.
        """
        self._binary_name = value
    
    @property
    def binary_version_high(self,) -> Optional[str]:
        """
        Gets the binaryVersionHigh property value. The high binary version.
        Returns: Optional[str]
        """
        return self._binary_version_high
    
    @binary_version_high.setter
    def binary_version_high(self,value: Optional[str] = None) -> None:
        """
        Sets the binaryVersionHigh property value. The high binary version.
        Args:
            value: Value to set for the binaryVersionHigh property.
        """
        self._binary_version_high = value
    
    @property
    def binary_version_low(self,) -> Optional[str]:
        """
        Gets the binaryVersionLow property value. The lower binary version.
        Returns: Optional[str]
        """
        return self._binary_version_low
    
    @binary_version_low.setter
    def binary_version_low(self,value: Optional[str] = None) -> None:
        """
        Sets the binaryVersionLow property value. The lower binary version.
        Args:
            value: Value to set for the binaryVersionLow property.
        """
        self._binary_version_low = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsInformationProtectionDesktopApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsInformationProtectionDesktopApp"
        # The binary name.
        self._binary_name: Optional[str] = None
        # The high binary version.
        self._binary_version_high: Optional[str] = None
        # The lower binary version.
        self._binary_version_low: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionDesktopApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionDesktopApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionDesktopApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "binary_name": lambda n : setattr(self, 'binary_name', n.get_str_value()),
            "binary_version_high": lambda n : setattr(self, 'binary_version_high', n.get_str_value()),
            "binary_version_low": lambda n : setattr(self, 'binary_version_low', n.get_str_value()),
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
        writer.write_str_value("binaryName", self.binary_name)
        writer.write_str_value("binaryVersionHigh", self.binary_version_high)
        writer.write_str_value("binaryVersionLow", self.binary_version_low)
    

