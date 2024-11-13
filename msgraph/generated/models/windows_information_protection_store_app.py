from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_information_protection_app import WindowsInformationProtectionApp

from .windows_information_protection_app import WindowsInformationProtectionApp

@dataclass
class WindowsInformationProtectionStoreApp(WindowsInformationProtectionApp, Parsable):
    """
    Store App for Windows information protection
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsInformationProtectionStoreApp"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionStoreApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .windows_information_protection_app import WindowsInformationProtectionApp

        from .windows_information_protection_app import WindowsInformationProtectionApp

        fields: Dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .windows_information_protection_app import WindowsInformationProtectionApp

    

