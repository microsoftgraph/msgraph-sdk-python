from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_minimum_operating_system, managed_mobile_lob_app

from . import managed_mobile_lob_app

@dataclass
class ManagedAndroidLobApp(managed_mobile_lob_app.ManagedMobileLobApp):
    odata_type = "#microsoft.graph.managedAndroidLobApp"
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
    # The package identifier.
    package_id: Optional[str] = None
    # The version code of managed Android Line of Business (LoB) app.
    version_code: Optional[str] = None
    # The version name of managed Android Line of Business (LoB) app.
    version_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAndroidLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAndroidLobApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedAndroidLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_minimum_operating_system, managed_mobile_lob_app

        from . import android_minimum_operating_system, managed_mobile_lob_app

        fields: Dict[str, Callable[[Any], None]] = {
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(android_minimum_operating_system.AndroidMinimumOperatingSystem)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "versionCode": lambda n : setattr(self, 'version_code', n.get_str_value()),
            "versionName": lambda n : setattr(self, 'version_name', n.get_str_value()),
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
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("versionCode", self.version_code)
        writer.write_str_value("versionName", self.version_name)
    

