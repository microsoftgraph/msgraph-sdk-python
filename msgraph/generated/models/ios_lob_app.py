from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_device_type import IosDeviceType
    from .ios_minimum_operating_system import IosMinimumOperatingSystem
    from .mobile_lob_app import MobileLobApp

from .mobile_lob_app import MobileLobApp

@dataclass
class IosLobApp(MobileLobApp):
    """
    Contains properties and inherited properties for iOS Line Of Business apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosLobApp"
    # Contains properties of the possible iOS device types the mobile app can run on.
    applicable_device_type: Optional[IosDeviceType] = None
    # The build number of iOS Line of Business (LoB) app.
    build_number: Optional[str] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The expiration time.
    expiration_date_time: Optional[datetime.datetime] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[IosMinimumOperatingSystem] = None
    # The version number of iOS Line of Business (LoB) app.
    version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosLobApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        from .ios_device_type import IosDeviceType
        from .ios_minimum_operating_system import IosMinimumOperatingSystem
        from .mobile_lob_app import MobileLobApp

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(IosDeviceType)),
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(IosMinimumOperatingSystem)),
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
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("versionNumber", self.version_number)
    

