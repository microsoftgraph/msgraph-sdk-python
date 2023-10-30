from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_device_type import IosDeviceType
    from .ios_minimum_operating_system import IosMinimumOperatingSystem
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class IosStoreApp(MobileApp):
    """
    Contains properties and inherited properties for iOS store apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosStoreApp"
    # The Apple App Store URL
    app_store_url: Optional[str] = None
    # Contains properties of the possible iOS device types the mobile app can run on.
    applicable_device_type: Optional[IosDeviceType] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[IosMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosStoreApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .mobile_app import MobileApp

        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .mobile_app import MobileApp

        fields: Dict[str, Callable[[Any], None]] = {
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "applicable_device_type": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(IosDeviceType)),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(IosMinimumOperatingSystem)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("app_store_url", self.app_store_url)
        writer.write_object_value("applicable_device_type", self.applicable_device_type)
        writer.write_str_value("bundle_id", self.bundle_id)
        writer.write_object_value("minimum_supported_operating_system", self.minimum_supported_operating_system)
    

