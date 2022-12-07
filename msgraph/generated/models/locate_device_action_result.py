from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_action_result = lazy_import('msgraph.generated.models.device_action_result')
device_geo_location = lazy_import('msgraph.generated.models.device_geo_location')

class LocateDeviceActionResult(device_action_result.DeviceActionResult):
    def __init__(self,) -> None:
        """
        Instantiates a new LocateDeviceActionResult and sets the default values.
        """
        super().__init__()
        # device location
        self._device_location: Optional[device_geo_location.DeviceGeoLocation] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LocateDeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LocateDeviceActionResult
        """
        if parse_node is None:
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("deviceLocation", self.device_location)
    

