from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_action_result, device_geo_location

from . import device_action_result

@dataclass
class LocateDeviceActionResult(device_action_result.DeviceActionResult):
    # device location
    device_location: Optional[device_geo_location.DeviceGeoLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocateDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocateDeviceActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LocateDeviceActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_action_result, device_geo_location

        from . import device_action_result, device_geo_location

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceLocation": lambda n : setattr(self, 'device_location', n.get_object_value(device_geo_location.DeviceGeoLocation)),
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
        writer.write_object_value("deviceLocation", self.device_location)
    

