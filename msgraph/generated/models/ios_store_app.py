from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_device_type = lazy_import('msgraph.generated.models.ios_device_type')
ios_minimum_operating_system = lazy_import('msgraph.generated.models.ios_minimum_operating_system')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')

class IosStoreApp(mobile_app.MobileApp):
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
            value: Value to set for the applicableDeviceType property.
        """
        self._applicable_device_type = value
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Apple App Store URL
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Apple App Store URL
        Args:
            value: Value to set for the appStoreUrl property.
        """
        self._app_store_url = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The Identity Name.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The Identity Name.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosStoreApp"
        # Contains properties of the possible iOS device types the mobile app can run on.
        self._applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
        # The Apple App Store URL
        self._app_store_url: Optional[str] = None
        # The Identity Name.
        self._bundle_id: Optional[str] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_device_type": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(ios_minimum_operating_system.IosMinimumOperatingSystem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[ios_minimum_operating_system.IosMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
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
    

