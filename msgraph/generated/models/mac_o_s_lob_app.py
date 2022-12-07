from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mac_o_s_lob_child_app = lazy_import('msgraph.generated.models.mac_o_s_lob_child_app')
mac_o_s_minimum_operating_system = lazy_import('msgraph.generated.models.mac_o_s_minimum_operating_system')
mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')

class MacOSLobApp(mobile_lob_app.MobileLobApp):
    @property
    def build_number(self,) -> Optional[str]:
        """
        Gets the buildNumber property value. The build number of the package. This should match the package CFBundleShortVersionString of the .pkg file.
        Returns: Optional[str]
        """
        return self._build_number
    
    @build_number.setter
    def build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the buildNumber property value. The build number of the package. This should match the package CFBundleShortVersionString of the .pkg file.
        Args:
            value: Value to set for the buildNumber property.
        """
        self._build_number = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The primary bundleId of the package.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The primary bundleId of the package.
        Args:
            value: Value to set for the bundleId property.
        """
        self._bundle_id = value
    
    @property
    def child_apps(self,) -> Optional[List[mac_o_s_lob_child_app.MacOSLobChildApp]]:
        """
        Gets the childApps property value. List of ComplexType macOSLobChildApp objects. Represents the apps expected to be installed by the package.
        Returns: Optional[List[mac_o_s_lob_child_app.MacOSLobChildApp]]
        """
        return self._child_apps
    
    @child_apps.setter
    def child_apps(self,value: Optional[List[mac_o_s_lob_child_app.MacOSLobChildApp]] = None) -> None:
        """
        Sets the childApps property value. List of ComplexType macOSLobChildApp objects. Represents the apps expected to be installed by the package.
        Args:
            value: Value to set for the childApps property.
        """
        self._child_apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSLobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSLobApp"
        # The build number of the package. This should match the package CFBundleShortVersionString of the .pkg file.
        self._build_number: Optional[str] = None
        # The primary bundleId of the package.
        self._bundle_id: Optional[str] = None
        # List of ComplexType macOSLobChildApp objects. Represents the apps expected to be installed by the package.
        self._child_apps: Optional[List[mac_o_s_lob_child_app.MacOSLobChildApp]] = None
        # When TRUE, indicates that the app's version will NOT be used to detect if the app is installed on a device. When FALSE, indicates that the app's version will be used to detect if the app is installed on a device. Set this to true for apps that use a self update feature.
        self._ignore_version_detection: Optional[bool] = None
        # When TRUE, indicates that the app will be installed as managed (requires macOS 11.0 and other managed package restrictions). When FALSE, indicates that the app will be installed as unmanaged.
        self._install_as_managed: Optional[bool] = None
        # The MD5 hash codes. This is empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        self._md5_hash: Optional[List[str]] = None
        # The chunk size for MD5 hash. This is '0' or empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        self._md5_hash_chunk_size: Optional[int] = None
        # ComplexType macOSMinimumOperatingSystem that indicates the minimum operating system applicable for the application.
        self._minimum_supported_operating_system: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem] = None
        # The version number of the package. This should match the package CFBundleVersion in the packageinfo file.
        self._version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSLobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOSLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "build_number": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "child_apps": lambda n : setattr(self, 'child_apps', n.get_collection_of_object_values(mac_o_s_lob_child_app.MacOSLobChildApp)),
            "ignore_version_detection": lambda n : setattr(self, 'ignore_version_detection', n.get_bool_value()),
            "install_as_managed": lambda n : setattr(self, 'install_as_managed', n.get_bool_value()),
            "md5_hash": lambda n : setattr(self, 'md5_hash', n.get_collection_of_primitive_values(str)),
            "md5_hash_chunk_size": lambda n : setattr(self, 'md5_hash_chunk_size', n.get_int_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem)),
            "version_number": lambda n : setattr(self, 'version_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ignore_version_detection(self,) -> Optional[bool]:
        """
        Gets the ignoreVersionDetection property value. When TRUE, indicates that the app's version will NOT be used to detect if the app is installed on a device. When FALSE, indicates that the app's version will be used to detect if the app is installed on a device. Set this to true for apps that use a self update feature.
        Returns: Optional[bool]
        """
        return self._ignore_version_detection
    
    @ignore_version_detection.setter
    def ignore_version_detection(self,value: Optional[bool] = None) -> None:
        """
        Sets the ignoreVersionDetection property value. When TRUE, indicates that the app's version will NOT be used to detect if the app is installed on a device. When FALSE, indicates that the app's version will be used to detect if the app is installed on a device. Set this to true for apps that use a self update feature.
        Args:
            value: Value to set for the ignoreVersionDetection property.
        """
        self._ignore_version_detection = value
    
    @property
    def install_as_managed(self,) -> Optional[bool]:
        """
        Gets the installAsManaged property value. When TRUE, indicates that the app will be installed as managed (requires macOS 11.0 and other managed package restrictions). When FALSE, indicates that the app will be installed as unmanaged.
        Returns: Optional[bool]
        """
        return self._install_as_managed
    
    @install_as_managed.setter
    def install_as_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the installAsManaged property value. When TRUE, indicates that the app will be installed as managed (requires macOS 11.0 and other managed package restrictions). When FALSE, indicates that the app will be installed as unmanaged.
        Args:
            value: Value to set for the installAsManaged property.
        """
        self._install_as_managed = value
    
    @property
    def md5_hash(self,) -> Optional[List[str]]:
        """
        Gets the md5Hash property value. The MD5 hash codes. This is empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        Returns: Optional[List[str]]
        """
        return self._md5_hash
    
    @md5_hash.setter
    def md5_hash(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the md5Hash property value. The MD5 hash codes. This is empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        Args:
            value: Value to set for the md5Hash property.
        """
        self._md5_hash = value
    
    @property
    def md5_hash_chunk_size(self,) -> Optional[int]:
        """
        Gets the md5HashChunkSize property value. The chunk size for MD5 hash. This is '0' or empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        Returns: Optional[int]
        """
        return self._md5_hash_chunk_size
    
    @md5_hash_chunk_size.setter
    def md5_hash_chunk_size(self,value: Optional[int] = None) -> None:
        """
        Sets the md5HashChunkSize property value. The chunk size for MD5 hash. This is '0' or empty if the package was uploaded directly. If the Intune App Wrapping Tool is used to create a .intunemac, this value can be found inside the Detection.xml file.
        Args:
            value: Value to set for the md5HashChunkSize property.
        """
        self._md5_hash_chunk_size = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. ComplexType macOSMinimumOperatingSystem that indicates the minimum operating system applicable for the application.
        Returns: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[mac_o_s_minimum_operating_system.MacOSMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. ComplexType macOSMinimumOperatingSystem that indicates the minimum operating system applicable for the application.
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
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_collection_of_object_values("childApps", self.child_apps)
        writer.write_bool_value("ignoreVersionDetection", self.ignore_version_detection)
        writer.write_bool_value("installAsManaged", self.install_as_managed)
        writer.write_collection_of_primitive_values("md5Hash", self.md5_hash)
        writer.write_int_value("md5HashChunkSize", self.md5_hash_chunk_size)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("versionNumber", self.version_number)
    
    @property
    def version_number(self,) -> Optional[str]:
        """
        Gets the versionNumber property value. The version number of the package. This should match the package CFBundleVersion in the packageinfo file.
        Returns: Optional[str]
        """
        return self._version_number
    
    @version_number.setter
    def version_number(self,value: Optional[str] = None) -> None:
        """
        Sets the versionNumber property value. The version number of the package. This should match the package CFBundleVersion in the packageinfo file.
        Args:
            value: Value to set for the versionNumber property.
        """
        self._version_number = value
    

