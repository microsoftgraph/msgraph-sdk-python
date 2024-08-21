from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detected_app_platform_type import DetectedAppPlatformType
    from .entity import Entity
    from .managed_device import ManagedDevice

from .entity import Entity

@dataclass
class DetectedApp(Entity):
    """
    A managed or unmanaged app that is installed on a managed device. Unmanaged apps will only appear for devices marked as corporate owned.
    """
    # The number of devices that have installed this application
    device_count: Optional[int] = None
    # Name of the discovered application. Read-only
    display_name: Optional[str] = None
    # The devices that have the discovered application installed
    managed_devices: Optional[List[ManagedDevice]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the operating system / platform of the discovered application.  Some possible values are Windows, iOS, macOS. The default value is unknown (0).
    platform: Optional[DetectedAppPlatformType] = None
    # Indicates the publisher of the discovered application. For example: 'Microsoft'.  The default value is an empty string.
    publisher: Optional[str] = None
    # Discovered application size in bytes. Read-only
    size_in_byte: Optional[int] = None
    # Version of the discovered application. Read-only
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectedApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectedApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .detected_app_platform_type import DetectedAppPlatformType
        from .entity import Entity
        from .managed_device import ManagedDevice

        from .detected_app_platform_type import DetectedAppPlatformType
        from .entity import Entity
        from .managed_device import ManagedDevice

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(DetectedAppPlatformType)),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "sizeInByte": lambda n : setattr(self, 'size_in_byte', n.get_int_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("sizeInByte", self.size_in_byte)
        writer.write_str_value("version", self.version)
    

