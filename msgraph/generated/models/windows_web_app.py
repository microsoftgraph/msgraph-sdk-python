from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app

from . import mobile_app

class WindowsWebApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsWebApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsWebApp"
        # Indicates the Windows web app URL. Example: 'https://www.contoso.com'
        self._app_url: Optional[str] = None
    
    @property
    def app_url(self,) -> Optional[str]:
        """
        Gets the appUrl property value. Indicates the Windows web app URL. Example: 'https://www.contoso.com'
        Returns: Optional[str]
        """
        return self._app_url
    
    @app_url.setter
    def app_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appUrl property value. Indicates the Windows web app URL. Example: 'https://www.contoso.com'
        Args:
            value: Value to set for the app_url property.
        """
        self._app_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsWebApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsWebApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsWebApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appUrl": lambda n : setattr(self, 'app_url', n.get_str_value()),
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
        writer.write_str_value("appUrl", self.app_url)
    

