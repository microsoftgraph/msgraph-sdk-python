from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_included_app import MacOSIncludedApp
    from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class MacOSDmgApp(MobileLobApp):
    """
    Contains properties and inherited properties for the MacOS DMG (Apple Disk Image) App.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSDmgApp"
    # When TRUE, indicates that the app's version will NOT be used to detect if the app is installed on a device. When FALSE, indicates that the app's version will be used to detect if the app is installed on a device. Set this to true for apps that use a self update feature. The default value is FALSE.
    ignore_version_detection: Optional[bool] = None
    # The list of .apps expected to be installed by the DMG (Apple Disk Image). This collection can contain a maximum of 500 elements.
    included_apps: Optional[List[MacOSIncludedApp]] = None
    # ComplexType macOSMinimumOperatingSystem that indicates the minimum operating system applicable for the application.
    minimum_supported_operating_system: Optional[MacOSMinimumOperatingSystem] = None
    # The bundleId of the primary .app in the DMG (Apple Disk Image). This maps to the CFBundleIdentifier in the app's bundle configuration.
    primary_bundle_id: Optional[str] = None
    # The version of the primary .app in the DMG (Apple Disk Image). This maps to the CFBundleShortVersion in the app's bundle configuration.
    primary_bundle_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSDmgApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSDmgApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSDmgApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_included_app import MacOSIncludedApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        from .mac_o_s_included_app import MacOSIncludedApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        fields: Dict[str, Callable[[Any], None]] = {
            "ignoreVersionDetection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "includedApps": lambda n : setattr(self, 'included_apps', n.get_collection_of_object_values(MacOSIncludedApp)),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(MacOSMinimumOperatingSystem)),
            "primaryBundleId": lambda n : setattr(self, 'primary_bundle_id', n.get_str_value()),
            "primaryBundleVersion": lambda n : setattr(self, 'primary_bundle_version', n.get_str_value()),
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
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_collection_of_object_values("includedApps", self.included_apps)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("primaryBundleId", self.primary_bundle_id)
        writer.write_str_value("primaryBundleVersion", self.primary_bundle_version)
    

