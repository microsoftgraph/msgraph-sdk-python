from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import device_action_result, device_geo_location

class LocateDeviceActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new LocateDeviceActionResult and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.locateDeviceActionResult"
        # device location
        self._device_location: Optional[device_geo_location.DeviceGeoLocation] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocateDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocateDeviceActionResult
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return LocateDeviceActionResult()

    @property
    def device_location(self,) -> Optional[device_geo_location.DeviceGeoLocation]:
        """
        Gets the deviceLocation property value. device location
        Returns: Optional[device_geo_location.DeviceGeoLocation]
        """
        return self._device_location

    @device_location.setter
    def device_location(self,value: Optional[device_geo_location.DeviceGeoLocation] = None) -> None:
        """
        Sets the deviceLocation property value. device location
        Args:
            value: Value to set for the deviceLocation property.
        """
        self._device_location = value

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_location": lambda n : setattr(self, 'device_location', n.get_object_value(device_geo_location.DeviceGeoLocation)),
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
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("deviceLocation", self.device_location)


