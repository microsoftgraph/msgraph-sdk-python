from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class WindowsWebApp(MobileApp):
    """
    Contains properties and inherited properties for Windows web apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsWebApp"
    # Indicates the Windows web app URL. Example: 'https://www.contoso.com'
    app_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsWebApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWebApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsWebApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app import MobileApp

        from .mobile_app import MobileApp

        fields: Dict[str, Callable[[Any], None]] = {
            "appUrl": lambda n : setattr(self, 'app_url', n.get_str_value()),
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
        writer.write_str_value("appUrl", self.app_url)
    

