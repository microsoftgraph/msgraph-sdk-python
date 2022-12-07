from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_minimum_operating_system = lazy_import('msgraph.generated.models.android_minimum_operating_system')
managed_app = lazy_import('msgraph.generated.models.managed_app')

class ManagedAndroidStoreApp(managed_app.ManagedApp):
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Android AppStoreUrl.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Android AppStoreUrl.
        Args:
            value: Value to set for the appStoreUrl property.
        """
        self._app_store_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAndroidStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedAndroidStoreApp"
        # The Android AppStoreUrl.
        self._app_store_url: Optional[str] = None
        # Contains properties for the minimum operating system required for an Android mobile app.
        self._minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
        # The app's package ID.
        self._package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAndroidStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAndroidStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAndroidStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(android_minimum_operating_system.AndroidMinimumOperatingSystem)),
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. Contains properties for the minimum operating system required for an Android mobile app.
        Returns: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. Contains properties for the minimum operating system required for an Android mobile app.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. The app's package ID.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. The app's package ID.
        Args:
            value: Value to set for the packageId property.
        """
        self._package_id = value
    
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
    

