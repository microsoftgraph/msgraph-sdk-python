from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_minimum_operating_system = lazy_import('msgraph.generated.models.android_minimum_operating_system')
mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')

class AndroidLobApp(mobile_lob_app.MobileLobApp):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidLobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidLobApp"
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
        # The package identifier.
        self._package_id: Optional[str] = None
        # The version code of Android Line of Business (LoB) app.
        self._version_code: Optional[str] = None
        # The version name of Android Line of Business (LoB) app.
        self._version_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidLobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(android_minimum_operating_system.AndroidMinimumOperatingSystem)),
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "version_code": lambda n : setattr(self, 'version_code', n.get_str_value()),
            "version_name": lambda n : setattr(self, 'version_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimumSupportedOperatingSystem property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. The package identifier.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. The package identifier.
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
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("versionCode", self.version_code)
        writer.write_str_value("versionName", self.version_name)
    
    @property
    def version_code(self,) -> Optional[str]:
        """
        Gets the versionCode property value. The version code of Android Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._version_code
    
    @version_code.setter
    def version_code(self,value: Optional[str] = None) -> None:
        """
        Sets the versionCode property value. The version code of Android Line of Business (LoB) app.
        Args:
            value: Value to set for the versionCode property.
        """
        self._version_code = value
    
    @property
    def version_name(self,) -> Optional[str]:
        """
        Gets the versionName property value. The version name of Android Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._version_name
    
    @version_name.setter
    def version_name(self,value: Optional[str] = None) -> None:
        """
        Sets the versionName property value. The version name of Android Line of Business (LoB) app.
        Args:
            value: Value to set for the versionName property.
        """
        self._version_name = value
    

