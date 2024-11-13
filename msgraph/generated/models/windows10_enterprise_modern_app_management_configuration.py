from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10EnterpriseModernAppManagementConfiguration(DeviceConfiguration, Parsable):
    """
    Windows10 Enterprise Modern App Management Configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration"
    # Indicates whether or not to uninstall a fixed list of built-in Windows apps.
    uninstall_built_in_apps: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10EnterpriseModernAppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnterpriseModernAppManagementConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10EnterpriseModernAppManagementConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration

        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "uninstallBuiltInApps": lambda n : setattr(self, 'uninstall_built_in_apps', n.get_bool_value()),
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
        from .device_configuration import DeviceConfiguration

        writer.write_bool_value("uninstallBuiltInApps", self.uninstall_built_in_apps)
    

