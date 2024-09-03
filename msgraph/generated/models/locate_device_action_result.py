from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_action_result import DeviceActionResult
    from .device_geo_location import DeviceGeoLocation

from .device_action_result import DeviceActionResult

@dataclass
class LocateDeviceActionResult(DeviceActionResult):
    """
    Locate device action result
    """
    # device location
    device_location: Optional[DeviceGeoLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LocateDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LocateDeviceActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LocateDeviceActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_action_result import DeviceActionResult
        from .device_geo_location import DeviceGeoLocation

        from .device_action_result import DeviceActionResult
        from .device_geo_location import DeviceGeoLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceLocation": lambda n : setattr(self, 'device_location', n.get_object_value(DeviceGeoLocation)),
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
        writer.write_object_value("deviceLocation", self.device_location)
    

