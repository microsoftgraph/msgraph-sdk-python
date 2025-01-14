from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_minimum_operating_system import AndroidMinimumOperatingSystem
    from .managed_app import ManagedApp

from .managed_app import ManagedApp

@dataclass
class ManagedAndroidStoreApp(ManagedApp, Parsable):
    """
    Contains properties and inherited properties for Android store apps that you can manage with an Intune app protection policy.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedAndroidStoreApp"
    # The Android AppStoreUrl.
    app_store_url: Optional[str] = None
    # Contains properties for the minimum operating system required for an Android mobile app.
    minimum_supported_operating_system: Optional[AndroidMinimumOperatingSystem] = None
    # The app's package ID.
    package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAndroidStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAndroidStoreApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAndroidStoreApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .managed_app import ManagedApp

        from .android_minimum_operating_system import AndroidMinimumOperatingSystem
        from .managed_app import ManagedApp

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
        writer.write_str_value("packageId", self.package_id)
    

