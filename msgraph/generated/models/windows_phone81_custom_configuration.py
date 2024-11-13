from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .oma_setting import OmaSetting

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsPhone81CustomConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the windowsPhone81CustomConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81CustomConfiguration"
    # OMA settings. This collection can contain a maximum of 1000 elements.
    oma_settings: Optional[List[OmaSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsPhone81CustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81CustomConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81CustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .oma_setting import OmaSetting

        from .device_configuration import DeviceConfiguration
        from .oma_setting import OmaSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "omaSettings": lambda n : setattr(self, 'oma_settings', n.get_collection_of_object_values(OmaSetting)),
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
        from .oma_setting import OmaSetting

        writer.write_collection_of_object_values("omaSettings", self.oma_settings)
    

