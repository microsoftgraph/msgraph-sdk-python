from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_minimum_operating_system, mobile_app

from . import mobile_app

@dataclass
class AndroidStoreApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.androidStoreApp"
    # The Android app store URL.
    app_store_url: Optional[str] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
    # The package identifier.
    package_id: Optional[str] = None
    
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
    

