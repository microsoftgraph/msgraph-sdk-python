from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_device_type, ios_minimum_operating_system, managed_app

from . import managed_app

@dataclass
class ManagedIOSStoreApp(managed_app.ManagedApp):
    odata_type = "#microsoft.graph.managedIOSStoreApp"
    # The Apple AppStoreUrl.
    app_store_url: Optional[str] = None
    # Contains properties of the possible iOS device types the mobile app can run on.
    applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
    # The app's Bundle ID.
    bundle_id: Optional[str] = None
    # Contains properties of the minimum operating system required for an iOS mobile app.
    minimum_supported_operating_system: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedIOSStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedIOSStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedIOSStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_device_type, ios_minimum_operating_system, managed_app

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(ios_minimum_operating_system.IosMinimumOperatingSystem)),
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
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

