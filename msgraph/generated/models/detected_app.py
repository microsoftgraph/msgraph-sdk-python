from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

detected_app_platform_type = lazy_import('msgraph.generated.models.detected_app_platform_type')
entity = lazy_import('msgraph.generated.models.entity')
managed_device = lazy_import('msgraph.generated.models.managed_device')

class DetectedApp(entity.Entity):
    """
    A managed or unmanaged app that is installed on a managed device. Unmanaged apps will only appear for devices marked as corporate owned.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new detectedApp and sets the default values.
        """
        super().__init__()
        # The number of devices that have installed this application
        self._device_count: Optional[int] = None
        # Name of the discovered application. Read-only
        self._display_name: Optional[str] = None
        # The devices that have the discovered application installed
        self._managed_devices: Optional[List[managed_device.ManagedDevice]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the operating system / platform of the discovered application.  Some possible values are Windows, iOS, macOS. The default value is unknown (0).
        self._platform: Optional[detected_app_platform_type.DetectedAppPlatformType] = None
        # Indicates the publisher of the discovered application. For example: 'Microsoft'.  The default value is an empty string.
        self._publisher: Optional[str] = None
        # Discovered application size in bytes. Read-only
        self._size_in_byte: Optional[int] = None
        # Version of the discovered application. Read-only
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DetectedApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DetectedApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DetectedApp()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. The number of devices that have installed this application
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. The number of devices that have installed this application
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the discovered application. Read-only
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the discovered application. Read-only
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(detected_app_platform_type.DetectedAppPlatformType)),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
            "size_in_byte": lambda n : setattr(self, 'size_in_byte', n.get_int_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_devices(self,) -> Optional[List[managed_device.ManagedDevice]]:
        """
        Gets the managedDevices property value. The devices that have the discovered application installed
        Returns: Optional[List[managed_device.ManagedDevice]]
        """
        return self._managed_devices
    
    @managed_devices.setter
    def managed_devices(self,value: Optional[List[managed_device.ManagedDevice]] = None) -> None:
        """
        Sets the managedDevices property value. The devices that have the discovered application installed
        Args:
            value: Value to set for the managedDevices property.
        """
        self._managed_devices = value
    
    @property
    def platform(self,) -> Optional[detected_app_platform_type.DetectedAppPlatformType]:
        """
        Gets the platform property value. Indicates the operating system / platform of the discovered application.  Some possible values are Windows, iOS, macOS. The default value is unknown (0).
        Returns: Optional[detected_app_platform_type.DetectedAppPlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[detected_app_platform_type.DetectedAppPlatformType] = None) -> None:
        """
        Sets the platform property value. Indicates the operating system / platform of the discovered application.  Some possible values are Windows, iOS, macOS. The default value is unknown (0).
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. Indicates the publisher of the discovered application. For example: 'Microsoft'.  The default value is an empty string.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. Indicates the publisher of the discovered application. For example: 'Microsoft'.  The default value is an empty string.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("publisher", self.publisher)
        writer.write_int_value("sizeInByte", self.size_in_byte)
        writer.write_str_value("version", self.version)
    
    @property
    def size_in_byte(self,) -> Optional[int]:
        """
        Gets the sizeInByte property value. Discovered application size in bytes. Read-only
        Returns: Optional[int]
        """
        return self._size_in_byte
    
    @size_in_byte.setter
    def size_in_byte(self,value: Optional[int] = None) -> None:
        """
        Sets the sizeInByte property value. Discovered application size in bytes. Read-only
        Args:
            value: Value to set for the sizeInByte property.
        """
        self._size_in_byte = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the discovered application. Read-only
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the discovered application. Read-only
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

