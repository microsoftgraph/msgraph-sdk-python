from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app = lazy_import('msgraph.generated.models.mobile_app')

class WebApp(mobile_app.MobileApp):
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
            value: Value to set for the appUrl property.
        """
        self._app_url = value
    
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
        fields = {
            "app_url": lambda n : setattr(self, 'app_url', n.get_str_value()),
            "use_managed_browser": lambda n : setattr(self, 'use_managed_browser', n.get_bool_value()),
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
            value: Value to set for the useManagedBrowser property.
        """
        self._use_managed_browser = value
    

