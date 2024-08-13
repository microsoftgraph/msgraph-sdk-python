from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mobile_app_assignment_settings import MobileAppAssignmentSettings

from .mobile_app_assignment_settings import MobileAppAssignmentSettings

@dataclass
class MacOsLobAppAssignmentSettings(MobileAppAssignmentSettings):
    """
    Contains properties used to assign a macOS LOB app to a group.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOsLobAppAssignmentSettings"
    # When TRUE, indicates that the app should be uninstalled when the device is removed from Intune. When FALSE, indicates that the app will not be uninstalled when the device is removed from Intune.
    uninstall_on_device_removal: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOsLobAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOsLobAppAssignmentSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOsLobAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        from .mobile_app_assignment_settings import MobileAppAssignmentSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "uninstallOnDeviceRemoval": lambda n : setattr(self, 'uninstall_on_device_removal', n.get_bool_value()),
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
        writer.write_bool_value("uninstallOnDeviceRemoval", self.uninstall_on_device_removal)
    

