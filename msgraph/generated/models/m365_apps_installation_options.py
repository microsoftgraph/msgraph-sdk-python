from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
    from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
    from .apps_update_channel_type import AppsUpdateChannelType
    from .entity import Entity

from .entity import Entity

@dataclass
class M365AppsInstallationOptions(Entity):
    # The appsForMac property
    apps_for_mac: Optional[AppsInstallationOptionsForMac] = None
    # The appsForWindows property
    apps_for_windows: Optional[AppsInstallationOptionsForWindows] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The updateChannel property
    update_channel: Optional[AppsUpdateChannelType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> M365AppsInstallationOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: M365AppsInstallationOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return M365AppsInstallationOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
        from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
        from .apps_update_channel_type import AppsUpdateChannelType
        from .entity import Entity

        from .apps_installation_options_for_mac import AppsInstallationOptionsForMac
        from .apps_installation_options_for_windows import AppsInstallationOptionsForWindows
        from .apps_update_channel_type import AppsUpdateChannelType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appsForMac": lambda n : setattr(self, 'apps_for_mac', n.get_object_value(AppsInstallationOptionsForMac)),
            "appsForWindows": lambda n : setattr(self, 'apps_for_windows', n.get_object_value(AppsInstallationOptionsForWindows)),
            "updateChannel": lambda n : setattr(self, 'update_channel', n.get_enum_value(AppsUpdateChannelType)),
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
        writer.write_object_value("appsForMac", self.apps_for_mac)
        writer.write_object_value("appsForWindows", self.apps_for_windows)
        writer.write_enum_value("updateChannel", self.update_channel)
    

