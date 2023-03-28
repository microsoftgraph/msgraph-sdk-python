from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_device_type, ios_minimum_operating_system, managed_app

from . import managed_app

class ManagedIOSStoreApp(managed_app.ManagedApp):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedIOSStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedIOSStoreApp"
        # The Apple AppStoreUrl.
        self._app_store_url: Optional[str] = None
        # Contains properties of the possible iOS device types the mobile app can run on.
        self._applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
        # The app's Bundle ID.
        self._bundle_id: Optional[str] = None
        # Contains properties of the minimum operating system required for an iOS mobile app.
        self._minimum_supported_operating_system: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Apple AppStoreUrl.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Apple AppStoreUrl.
        Args:
            value: Value to set for the app_store_url property.
        """
        self._app_store_url = value
    
    @property
    def applicable_device_type(self,) -> Optional[ios_device_type.IosDeviceType]:
        """
        Gets the applicableDeviceType property value. Contains properties of the possible iOS device types the mobile app can run on.
        Returns: Optional[ios_device_type.IosDeviceType]
        """
        return self._applicable_device_type
    
    @applicable_device_type.setter
    def applicable_device_type(self,value: Optional[ios_device_type.IosDeviceType] = None) -> None:
        """
        Sets the applicableDeviceType property value. Contains properties of the possible iOS device types the mobile app can run on.
        Args:
            value: Value to set for the applicable_device_type property.
        """
        self._applicable_device_type = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The app's Bundle ID.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The app's Bundle ID.
        Args:
            value: Value to set for the bundle_id property.
        """
        self._bundle_id = value
    
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
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[ios_minimum_operating_system.IosMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. Contains properties of the minimum operating system required for an iOS mobile app.
        Returns: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. Contains properties of the minimum operating system required for an iOS mobile app.
        Args:
            value: Value to set for the minimum_supported_operating_system property.
        """
        self._minimum_supported_operating_system = value
    
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
    

