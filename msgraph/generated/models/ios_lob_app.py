from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_device_type = lazy_import('msgraph.generated.models.ios_device_type')
ios_minimum_operating_system = lazy_import('msgraph.generated.models.ios_minimum_operating_system')
mobile_lob_app = lazy_import('msgraph.generated.models.mobile_lob_app')

class IosLobApp(mobile_lob_app.MobileLobApp):
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
    def build_number(self,) -> Optional[str]:
        """
        Gets the buildNumber property value. The build number of iOS Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._build_number
    
    @build_number.setter
    def build_number(self,value: Optional[str] = None) -> None:
        """
        Sets the buildNumber property value. The build number of iOS Line of Business (LoB) app.
        Args:
            value: Value to set for the buildNumber property.
        """
        self._build_number = value
    
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
        Instantiates a new IosLobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosLobApp"
        # Contains properties of the possible iOS device types the mobile app can run on.
        self._applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
        # The build number of iOS Line of Business (LoB) app.
        self._build_number: Optional[str] = None
        # The Identity Name.
        self._bundle_id: Optional[str] = None
        # The expiration time.
        self._expiration_date_time: Optional[datetime] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None
        # The version number of iOS Line of Business (LoB) app.
        self._version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosLobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosLobApp()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. The expiration time.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. The expiration time.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applicable_device_type": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "build_number": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundle_id": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "minimum_supported_operating_system": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(ios_minimum_operating_system.IosMinimumOperatingSystem)),
            "version_number": lambda n : setattr(self, 'version_number', n.get_str_value()),
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
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("versionNumber", self.version_number)
    
    @property
    def version_number(self,) -> Optional[str]:
        """
        Gets the versionNumber property value. The version number of iOS Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._version_number
    
    @version_number.setter
    def version_number(self,value: Optional[str] = None) -> None:
        """
        Sets the versionNumber property value. The version number of iOS Line of Business (LoB) app.
        Args:
            value: Value to set for the versionNumber property.
        """
        self._version_number = value
    

