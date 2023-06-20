from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_contained_app, mobile_lob_app, windows_architecture, windows_device_type, windows_minimum_operating_system

from . import mobile_lob_app

@dataclass
class WindowsUniversalAppX(mobile_lob_app.MobileLobApp):
    odata_type = "#microsoft.graph.windowsUniversalAppX"
    # Contains properties for Windows architecture.
    applicable_architectures: Optional[windows_architecture.WindowsArchitecture] = None
    # Contains properties for Windows device type.
    applicable_device_types: Optional[windows_device_type.WindowsDeviceType] = None
    # The collection of contained apps in the committed mobileAppContent of a windowsUniversalAppX app.
    committed_contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
    # The Identity Name.
    identity_name: Optional[str] = None
    # The Identity Publisher Hash.
    identity_publisher_hash: Optional[str] = None
    # The Identity Resource Identifier.
    identity_resource_identifier: Optional[str] = None
    # The identity version.
    identity_version: Optional[str] = None
    # Whether or not the app is a bundle.
    is_bundle: Optional[bool] = None
    # The minimum operating system required for a Windows mobile app.
    minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUniversalAppX:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUniversalAppX
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsUniversalAppX()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_contained_app, mobile_lob_app, windows_architecture, windows_device_type, windows_minimum_operating_system

        from . import mobile_contained_app, mobile_lob_app, windows_architecture, windows_device_type, windows_minimum_operating_system

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableArchitectures": lambda n : setattr(self, 'applicable_architectures', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "applicableDeviceTypes": lambda n : setattr(self, 'applicable_device_types', n.get_enum_value(windows_device_type.WindowsDeviceType)),
            "committedContainedApps": lambda n : setattr(self, 'committed_contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
            "identityName": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identityPublisherHash": lambda n : setattr(self, 'identity_publisher_hash', n.get_str_value()),
            "identityResourceIdentifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "isBundle": lambda n : setattr(self, 'is_bundle', n.get_bool_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_enum_value("applicableDeviceTypes", self.applicable_device_types)
        writer.write_collection_of_object_values("committedContainedApps", self.committed_contained_apps)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisherHash", self.identity_publisher_hash)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_bool_value("isBundle", self.is_bundle)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

