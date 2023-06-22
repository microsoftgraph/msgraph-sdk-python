from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_device_type, ios_minimum_operating_system, managed_mobile_lob_app

from . import managed_mobile_lob_app

@dataclass
class ManagedIOSLobApp(managed_mobile_lob_app.ManagedMobileLobApp):
    odata_type = "#microsoft.graph.managedIOSLobApp"
    # Contains properties of the possible iOS device types the mobile app can run on.
    applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
    # The build number of managed iOS Line of Business (LoB) app.
    build_number: Optional[str] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The expiration time.
    expiration_date_time: Optional[datetime] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[ios_minimum_operating_system.IosMinimumOperatingSystem] = None
    # The version number of managed iOS Line of Business (LoB) app.
    version_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedIOSLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedIOSLobApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedIOSLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_device_type, ios_minimum_operating_system, managed_mobile_lob_app

        from . import ios_device_type, ios_minimum_operating_system, managed_mobile_lob_app

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "buildNumber": lambda n : setattr(self, 'build_number', n.get_str_value()),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(ios_minimum_operating_system.IosMinimumOperatingSystem)),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_str_value()),
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
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
        writer.write_str_value("buildNumber", self.build_number)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("versionNumber", self.version_number)
    

