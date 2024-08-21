from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceGeoLocation(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device location
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Altitude, given in meters above sea level
    altitude: Optional[float] = None
    # Heading in degrees from true north
    heading: Optional[float] = None
    # Accuracy of longitude and latitude in meters
    horizontal_accuracy: Optional[float] = None
    # Time at which location was recorded, relative to UTC
    last_collected_date_time: Optional[datetime.datetime] = None
    # Latitude coordinate of the device's location
    latitude: Optional[float] = None
    # Longitude coordinate of the device's location
    longitude: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Speed the device is traveling in meters per second
    speed: Optional[float] = None
    # Accuracy of altitude in meters
    vertical_accuracy: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceGeoLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceGeoLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceGeoLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "altitude": lambda n : setattr(self, 'altitude', n.get_float_value()),
            "heading": lambda n : setattr(self, 'heading', n.get_float_value()),
            "horizontalAccuracy": lambda n : setattr(self, 'horizontal_accuracy', n.get_float_value()),
            "lastCollectedDateTime": lambda n : setattr(self, 'last_collected_date_time', n.get_datetime_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speed": lambda n : setattr(self, 'speed', n.get_float_value()),
            "verticalAccuracy": lambda n : setattr(self, 'vertical_accuracy', n.get_float_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_float_value("altitude", self.altitude)
        writer.write_float_value("heading", self.heading)
        writer.write_float_value("horizontalAccuracy", self.horizontal_accuracy)
        writer.write_datetime_value("lastCollectedDateTime", self.last_collected_date_time)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("speed", self.speed)
        writer.write_float_value("verticalAccuracy", self.vertical_accuracy)
        writer.write_additional_data_value(self.additional_data)
    

