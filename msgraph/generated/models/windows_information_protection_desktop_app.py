from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_information_protection_app

from . import windows_information_protection_app

@dataclass
class WindowsInformationProtectionDesktopApp(windows_information_protection_app.WindowsInformationProtectionApp):
    odata_type = "#microsoft.graph.windowsInformationProtectionDesktopApp"
    # The binary name.
    binary_name: Optional[str] = None
    # The high binary version.
    binary_version_high: Optional[str] = None
    # The lower binary version.
    binary_version_low: Optional[str] = None
    
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
        from . import windows_information_protection_app

        fields: Dict[str, Callable[[Any], None]] = {
            "binaryName": lambda n : setattr(self, 'binary_name', n.get_str_value()),
            "binaryVersionHigh": lambda n : setattr(self, 'binary_version_high', n.get_str_value()),
            "binaryVersionLow": lambda n : setattr(self, 'binary_version_low', n.get_str_value()),
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
    

