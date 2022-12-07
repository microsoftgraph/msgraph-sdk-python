from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceGeoLocation(AdditionalDataHolder, Parsable):
    """
    Device location
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def altitude(self,) -> Optional[float]:
        """
        Gets the altitude property value. Altitude, given in meters above sea level
        Returns: Optional[float]
        """
        return self._altitude
    
    @altitude.setter
    def altitude(self,value: Optional[float] = None) -> None:
        """
        Sets the altitude property value. Altitude, given in meters above sea level
        Args:
            value: Value to set for the altitude property.
        """
        self._altitude = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceGeoLocation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Altitude, given in meters above sea level
        self._altitude: Optional[float] = None
        # Heading in degrees from true north
        self._heading: Optional[float] = None
        # Accuracy of longitude and latitude in meters
        self._horizontal_accuracy: Optional[float] = None
        # Time at which location was recorded, relative to UTC
        self._last_collected_date_time: Optional[datetime] = None
        # Latitude coordinate of the device's location
        self._latitude: Optional[float] = None
        # Longitude coordinate of the device's location
        self._longitude: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Speed the device is traveling in meters per second
        self._speed: Optional[float] = None
        # Accuracy of altitude in meters
        self._vertical_accuracy: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceGeoLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceGeoLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceGeoLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "altitude": lambda n : setattr(self, 'altitude', n.get_float_value()),
            "heading": lambda n : setattr(self, 'heading', n.get_float_value()),
            "horizontal_accuracy": lambda n : setattr(self, 'horizontal_accuracy', n.get_float_value()),
            "last_collected_date_time": lambda n : setattr(self, 'last_collected_date_time', n.get_datetime_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "speed": lambda n : setattr(self, 'speed', n.get_float_value()),
            "vertical_accuracy": lambda n : setattr(self, 'vertical_accuracy', n.get_float_value()),
        }
        return fields
    
    @property
    def heading(self,) -> Optional[float]:
        """
        Gets the heading property value. Heading in degrees from true north
        Returns: Optional[float]
        """
        return self._heading
    
    @heading.setter
    def heading(self,value: Optional[float] = None) -> None:
        """
        Sets the heading property value. Heading in degrees from true north
        Args:
            value: Value to set for the heading property.
        """
        self._heading = value
    
    @property
    def horizontal_accuracy(self,) -> Optional[float]:
        """
        Gets the horizontalAccuracy property value. Accuracy of longitude and latitude in meters
        Returns: Optional[float]
        """
        return self._horizontal_accuracy
    
    @horizontal_accuracy.setter
    def horizontal_accuracy(self,value: Optional[float] = None) -> None:
        """
        Sets the horizontalAccuracy property value. Accuracy of longitude and latitude in meters
        Args:
            value: Value to set for the horizontalAccuracy property.
        """
        self._horizontal_accuracy = value
    
    @property
    def last_collected_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCollectedDateTime property value. Time at which location was recorded, relative to UTC
        Returns: Optional[datetime]
        """
        return self._last_collected_date_time
    
    @last_collected_date_time.setter
    def last_collected_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCollectedDateTime property value. Time at which location was recorded, relative to UTC
        Args:
            value: Value to set for the lastCollectedDateTime property.
        """
        self._last_collected_date_time = value
    
    @property
    def latitude(self,) -> Optional[float]:
        """
        Gets the latitude property value. Latitude coordinate of the device's location
        Returns: Optional[float]
        """
        return self._latitude
    
    @latitude.setter
    def latitude(self,value: Optional[float] = None) -> None:
        """
        Sets the latitude property value. Latitude coordinate of the device's location
        Args:
            value: Value to set for the latitude property.
        """
        self._latitude = value
    
    @property
    def longitude(self,) -> Optional[float]:
        """
        Gets the longitude property value. Longitude coordinate of the device's location
        Returns: Optional[float]
        """
        return self._longitude
    
    @longitude.setter
    def longitude(self,value: Optional[float] = None) -> None:
        """
        Sets the longitude property value. Longitude coordinate of the device's location
        Args:
            value: Value to set for the longitude property.
        """
        self._longitude = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def speed(self,) -> Optional[float]:
        """
        Gets the speed property value. Speed the device is traveling in meters per second
        Returns: Optional[float]
        """
        return self._speed
    
    @speed.setter
    def speed(self,value: Optional[float] = None) -> None:
        """
        Sets the speed property value. Speed the device is traveling in meters per second
        Args:
            value: Value to set for the speed property.
        """
        self._speed = value
    
    @property
    def vertical_accuracy(self,) -> Optional[float]:
        """
        Gets the verticalAccuracy property value. Accuracy of altitude in meters
        Returns: Optional[float]
        """
        return self._vertical_accuracy
    
    @vertical_accuracy.setter
    def vertical_accuracy(self,value: Optional[float] = None) -> None:
        """
        Sets the verticalAccuracy property value. Accuracy of altitude in meters
        Args:
            value: Value to set for the verticalAccuracy property.
        """
        self._vertical_accuracy = value
    

