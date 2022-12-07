from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

geo_coordinates = lazy_import('msgraph.generated.models.geo_coordinates')

class SignInLocation(AdditionalDataHolder, Parsable):
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
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new signInLocation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Provides the city where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        self._city: Optional[str] = None
        # Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.
        self._country_or_region: Optional[str] = None
        # Provides the latitude, longitude and altitude where the sign-in originated.
        self._geo_coordinates: Optional[geo_coordinates.GeoCoordinates] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        self._state: Optional[str] = None
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. Provides the country code info (2 letter code) where the sign-in originated.  This is calculated using latitude/longitude information from the sign-in activity.
        Args:
            value: Value to set for the countryOrRegion property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignInLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignInLocation()
    
    @property
    def geo_coordinates(self,) -> Optional[geo_coordinates.GeoCoordinates]:
        """
        Gets the geoCoordinates property value. Provides the latitude, longitude and altitude where the sign-in originated.
        Returns: Optional[geo_coordinates.GeoCoordinates]
        """
        return self._geo_coordinates
    
    @geo_coordinates.setter
    def geo_coordinates(self,value: Optional[geo_coordinates.GeoCoordinates] = None) -> None:
        """
        Sets the geoCoordinates property value. Provides the latitude, longitude and altitude where the sign-in originated.
        Args:
            value: Value to set for the geoCoordinates property.
        """
        self._geo_coordinates = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_or_region": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "geo_coordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(geo_coordinates.GeoCoordinates)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
        }
        return fields
    
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. Provides the State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

