from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_contained_app = lazy_import('msgraph.generated.models.mobile_contained_app')
mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')
windows_architecture = lazy_import('msgraph.generated.models.windows_architecture')
windows_device_type = lazy_import('msgraph.generated.models.windows_device_type')
windows_minimum_operating_system = lazy_import('msgraph.generated.models.windows_minimum_operating_system')

class WindowsUniversalAppX(mobile_lob_app.MobileLobApp):
    @property
    def applicable_architectures(self,) -> Optional[windows_architecture.WindowsArchitecture]:
        """
        Gets the applicableArchitectures property value. Contains properties for Windows architecture.
        Returns: Optional[windows_architecture.WindowsArchitecture]
        """
        return self._applicable_architectures
    
    @applicable_architectures.setter
    def applicable_architectures(self,value: Optional[windows_architecture.WindowsArchitecture] = None) -> None:
        """
        Sets the applicableArchitectures property value. Contains properties for Windows architecture.
        Args:
            value: Value to set for the applicableArchitectures property.
        """
        self._applicable_architectures = value
    
    @property
    def applicable_device_types(self,) -> Optional[windows_device_type.WindowsDeviceType]:
        """
        Gets the applicableDeviceTypes property value. Contains properties for Windows device type.
        Returns: Optional[windows_device_type.WindowsDeviceType]
        """
        return self._applicable_device_types
    
    @applicable_device_types.setter
    def applicable_device_types(self,value: Optional[windows_device_type.WindowsDeviceType] = None) -> None:
        """
        Sets the applicableDeviceTypes property value. Contains properties for Windows device type.
        Args:
            value: Value to set for the applicableDeviceTypes property.
        """
        self._applicable_device_types = value
    
    @property
    def committed_contained_apps(self,) -> Optional[List[mobile_contained_app.MobileContainedApp]]:
        """
        Gets the committedContainedApps property value. The collection of contained apps in the committed mobileAppContent of a windowsUniversalAppX app.
        Returns: Optional[List[mobile_contained_app.MobileContainedApp]]
        """
        return self._committed_contained_apps
    
    @committed_contained_apps.setter
    def committed_contained_apps(self,value: Optional[List[mobile_contained_app.MobileContainedApp]] = None) -> None:
        """
        Sets the committedContainedApps property value. The collection of contained apps in the committed mobileAppContent of a windowsUniversalAppX app.
        Args:
            value: Value to set for the committedContainedApps property.
        """
        self._committed_contained_apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsUniversalAppX and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUniversalAppX"
        # Contains properties for Windows architecture.
        self._applicable_architectures: Optional[windows_architecture.WindowsArchitecture] = None
        # Contains properties for Windows device type.
        self._applicable_device_types: Optional[windows_device_type.WindowsDeviceType] = None
        # The collection of contained apps in the committed mobileAppContent of a windowsUniversalAppX app.
        self._committed_contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
        # The Identity Name.
        self._identity_name: Optional[str] = None
        # The Identity Publisher Hash.
        self._identity_publisher_hash: Optional[str] = None
        # The Identity Resource Identifier.
        self._identity_resource_identifier: Optional[str] = None
        # The identity version.
        self._identity_version: Optional[str] = None
        # Whether or not the app is a bundle.
        self._is_bundle: Optional[bool] = None
        # The minimum operating system required for a Windows mobile app.
        self._minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUniversalAppX:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUniversalAppX
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUniversalAppX()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_architectures": lambda n : setattr(self, 'applicable_architectures', n.get_enum_value(windows_architecture.WindowsArchitecture)),
            "applicable_device_types": lambda n : setattr(self, 'applicable_device_types', n.get_enum_value(windows_device_type.WindowsDeviceType)),
            "committed_contained_apps": lambda n : setattr(self, 'committed_contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
            "identity_name": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identity_publisher_hash": lambda n : setattr(self, 'identity_publisher_hash', n.get_str_value()),
            "identity_resource_identifier": lambda n : setattr(self, 'identity_resource_identifier', n.get_str_value()),
            "identity_version": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "is_bundle": lambda n : setattr(self, 'is_bundle', n.get_bool_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_name(self,) -> Optional[str]:
        """
        Gets the identityName property value. The Identity Name.
        Returns: Optional[str]
        """
        return self._identity_name
    
    @identity_name.setter
    def identity_name(self,value: Optional[str] = None) -> None:
        """
        Sets the identityName property value. The Identity Name.
        Args:
            value: Value to set for the identityName property.
        """
        self._identity_name = value
    
    @property
    def identity_publisher_hash(self,) -> Optional[str]:
        """
        Gets the identityPublisherHash property value. The Identity Publisher Hash.
        Returns: Optional[str]
        """
        return self._identity_publisher_hash
    
    @identity_publisher_hash.setter
    def identity_publisher_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the identityPublisherHash property value. The Identity Publisher Hash.
        Args:
            value: Value to set for the identityPublisherHash property.
        """
        self._identity_publisher_hash = value
    
    @property
    def identity_resource_identifier(self,) -> Optional[str]:
        """
        Gets the identityResourceIdentifier property value. The Identity Resource Identifier.
        Returns: Optional[str]
        """
        return self._identity_resource_identifier
    
    @identity_resource_identifier.setter
    def identity_resource_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identityResourceIdentifier property value. The Identity Resource Identifier.
        Args:
            value: Value to set for the identityResourceIdentifier property.
        """
        self._identity_resource_identifier = value
    
    @property
    def identity_version(self,) -> Optional[str]:
        """
        Gets the identityVersion property value. The identity version.
        Returns: Optional[str]
        """
        return self._identity_version
    
    @identity_version.setter
    def identity_version(self,value: Optional[str] = None) -> None:
        """
        Sets the identityVersion property value. The identity version.
        Args:
            value: Value to set for the identityVersion property.
        """
        self._identity_version = value
    
    @property
    def is_bundle(self,) -> Optional[bool]:
        """
        Gets the isBundle property value. Whether or not the app is a bundle.
        Returns: Optional[bool]
        """
        return self._is_bundle
    
    @is_bundle.setter
    def is_bundle(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBundle property value. Whether or not the app is a bundle.
        Args:
            value: Value to set for the isBundle property.
        """
        self._is_bundle = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
        Returns: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
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
        writer.write_enum_value("applicableArchitectures", self.applicable_architectures)
        writer.write_enum_value("applicableDeviceTypes", self.applicable_device_types)
        writer.write_collection_of_object_values("committedContainedApps", self.committed_contained_apps)
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityPublisherHash", self.identity_publisher_hash)
        writer.write_str_value("identityResourceIdentifier", self.identity_resource_identifier)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_bool_value("isBundle", self.is_bundle)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
    

