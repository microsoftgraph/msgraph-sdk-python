from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class GeoCoordinates(AdditionalDataHolder, Parsable):
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
        Gets the altitude property value. Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
        Returns: Optional[float]
        """
        return self._altitude
    
    @altitude.setter
    def altitude(self,value: Optional[float] = None) -> None:
        """
        Sets the altitude property value. Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
        Args:
            value: Value to set for the altitude property.
        """
        self._altitude = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new geoCoordinates and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
        self._altitude: Optional[float] = None
        # Optional. The latitude, in decimal, for the item. Read-only.
        self._latitude: Optional[float] = None
        # Optional. The longitude, in decimal, for the item. Read-only.
        self._longitude: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GeoCoordinates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GeoCoordinates
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GeoCoordinates()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "altitude": lambda n : setattr(self, 'altitude', n.get_float_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def latitude(self,) -> Optional[float]:
        """
        Gets the latitude property value. Optional. The latitude, in decimal, for the item. Read-only.
        Returns: Optional[float]
        """
        return self._latitude
    
    @latitude.setter
    def latitude(self,value: Optional[float] = None) -> None:
        """
        Sets the latitude property value. Optional. The latitude, in decimal, for the item. Read-only.
        Args:
            value: Value to set for the latitude property.
        """
        self._latitude = value
    
    @property
    def longitude(self,) -> Optional[float]:
        """
        Gets the longitude property value. Optional. The longitude, in decimal, for the item. Read-only.
        Returns: Optional[float]
        """
        return self._longitude
    
    @longitude.setter
    def longitude(self,value: Optional[float] = None) -> None:
        """
        Sets the longitude property value. Optional. The longitude, in decimal, for the item. Read-only.
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
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

