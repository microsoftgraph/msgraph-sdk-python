from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_app

from . import mobile_app

class WebApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WebApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.webApp"
        # The web app URL. This property cannot be PATCHed.
        self._app_url: Optional[str] = None
        # Whether or not to use managed browser. This property is only applicable for Android and IOS.
        self._use_managed_browser: Optional[bool] = None
    
    @property
    def app_url(self,) -> Optional[str]:
        """
        Gets the appUrl property value. The web app URL. This property cannot be PATCHed.
        Returns: Optional[str]
        """
        return self._app_url
    
    @app_url.setter
    def app_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appUrl property value. The web app URL. This property cannot be PATCHed.
        Args:
            value: Value to set for the app_url property.
        """
        self._app_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appUrl": lambda n : setattr(self, 'app_url', n.get_str_value()),
            "useManagedBrowser": lambda n : setattr(self, 'use_managed_browser', n.get_bool_value()),
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
        writer.write_bool_value("useManagedBrowser", self.use_managed_browser)
    
    @property
    def use_managed_browser(self,) -> Optional[bool]:
        """
        Gets the useManagedBrowser property value. Whether or not to use managed browser. This property is only applicable for Android and IOS.
        Returns: Optional[bool]
        """
        return self._use_managed_browser
    
    @use_managed_browser.setter
    def use_managed_browser(self,value: Optional[bool] = None) -> None:
        """
        Sets the useManagedBrowser property value. Whether or not to use managed browser. This property is only applicable for Android and IOS.
        Args:
            value: Value to set for the use_managed_browser property.
        """
        self._use_managed_browser = value
    

