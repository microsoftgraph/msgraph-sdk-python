from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_lob_child_app import MacOSLobChildApp
    from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class MacOSLobApp(MobileLobApp, Parsable):
    """
    Contains properties and inherited properties for the macOS LOB App.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSLobApp"
    # The build number of the package. This should match the package CFBundleShortVersionString of the .pkg file.
    build_number: Optional[str] = None
    # The primary bundleId of the package.
    bundle_id: Optional[str] = None
    # List of ComplexType macOSLobChildApp objects. Represents the apps expected to be installed by the package.
    child_apps: Optional[list[MacOSLobChildApp]] = None
    # When TRUE, indicates that the app's version will NOT be used to detect if the app is installed on a device. When FALSE, indicates that the app's version will be used to detect if the app is installed on a device. Set this to true for apps that use a self update feature. The default value is FALSE.
    ignore_version_detection: Optional[bool] = None
    # When TRUE, indicates that the app will be installed as managed (requires macOS 11.0 and other managed package restrictions). When FALSE, indicates that the app will be installed as unmanaged. The default value is FALSE.
    install_as_managed: Optional[bool] = None
    # The MD5 hash codes. This is empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
    md5_hash: Optional[list[str]] = None
    # The chunk size for MD5 hash. This is '0' or empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
    md5_hash_chunk_size: Optional[int] = None
    # ComplexType macOSMinimumOperatingSystem that indicates the minimum operating system applicable for the application.
    minimum_supported_operating_system: Optional[MacOSMinimumOperatingSystem] = None
    # The version number of the package. This should match the package CFBundleVersion in the packageinfo file.
    version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSLobApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSLobApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_lob_child_app import MacOSLobChildApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        from .mac_o_s_lob_child_app import MacOSLobChildApp
        from .mac_o_s_minimum_operating_system import MacOSMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        fields: dict[str, Callable[[Any], None]] = {
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "childApps": lambda n : setattr(self, 'child_apps', n.get_collection_of_object_values(MacOSLobChildApp)),
            "ignoreVersionDetection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "installAsManaged": lambda n : setattr(self, 'install_as_managed', n.get_bool_value()),
            "md5Hash": lambda n : setattr(self, 'md5_hash', n.get_collection_of_primitive_values(str)),
            "md5HashChunkSize": lambda n : setattr(self, 'md5_hash_chunk_size', n.get_int_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(MacOSMinimumOperatingSystem)),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_str_value()),
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
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_collection_of_object_values("childApps", self.child_apps)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_bool_value("installAsManaged", self.install_as_managed)
        writer.write_collection_of_primitive_values("md5Hash", self.md5_hash)
        writer.write_int_value("md5HashChunkSize", self.md5_hash_chunk_size)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("versionNumber", self.version_number)
    

