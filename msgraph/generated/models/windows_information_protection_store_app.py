from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_information_protection_app

from . import windows_information_protection_app

class WindowsInformationProtectionStoreApp(windows_information_protection_app.WindowsInformationProtectionApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsInformationProtectionStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsInformationProtectionStoreApp"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_information_protection_app

        fields: Dict[str, Callable[[Any], None]] = {
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
    

