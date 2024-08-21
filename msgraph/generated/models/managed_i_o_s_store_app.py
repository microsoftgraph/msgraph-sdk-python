from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_device_type import IosDeviceType
    from .ios_minimum_operating_system import IosMinimumOperatingSystem
    from .managed_app import ManagedApp

from .managed_app import ManagedApp

@dataclass
class ManagedIOSStoreApp(ManagedApp):
    """
    Contains properties and inherited properties for an iOS store app that you can manage with an Intune app protection policy.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedIOSStoreApp"
    # The Apple AppStoreUrl.
    app_store_url: Optional[str] = None
    # Contains properties of the possible iOS device types the mobile app can run on.
    applicable_device_type: Optional[IosDeviceType] = None
    # The app's Bundle ID.
    bundle_id: Optional[str] = None
    # Contains properties of the minimum operating system required for an iOS mobile app.
    minimum_supported_operating_system: Optional[IosMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedIOSStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedIOSStoreApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedIOSStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .managed_app import ManagedApp

        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .managed_app import ManagedApp

        fields: Dict[str, Callable[[Any], None]] = {
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(IosDeviceType)),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(IosMinimumOperatingSystem)),
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
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

