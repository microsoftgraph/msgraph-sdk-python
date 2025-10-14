from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_minimum_operating_system import AndroidMinimumOperatingSystem
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class AndroidStoreApp(MobileApp, Parsable):
    """
    Contains properties and inherited properties for Android store apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidStoreApp"
    # The Android app store URL.
    app_store_url: Optional[str] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[AndroidMinimumOperatingSystem] = None
    # The package identifier. This property is read-only.
    package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidStoreApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidStoreApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .mobile_app import MobileApp

        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .mobile_app import MobileApp

        fields: dict[str, Callable[[Any], None]] = {
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(AndroidMinimumOperatingSystem)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
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
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

