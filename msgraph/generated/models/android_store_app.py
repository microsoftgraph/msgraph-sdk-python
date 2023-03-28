from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_minimum_operating_system, mobile_app

from . import mobile_app

class AndroidStoreApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidStoreApp"
        # The Android app store URL.
        self._app_store_url: Optional[str] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
        # The package identifier.
        self._package_id: Optional[str] = None
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Android app store URL.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Android app store URL.
        Args:
            value: Value to set for the app_store_url property.
        """
        self._app_store_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_minimum_operating_system, mobile_app

        fields: Dict[str, Callable[[Any], None]] = {
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(android_minimum_operating_system.AndroidMinimumOperatingSystem)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimum_supported_operating_system property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. The package identifier.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. The package identifier.
        Args:
            value: Value to set for the package_id property.
        """
        self._package_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
    

