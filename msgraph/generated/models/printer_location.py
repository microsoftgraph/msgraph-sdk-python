from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PrinterLocation(AdditionalDataHolder, Parsable):
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
    def altitude_in_meters(self,) -> Optional[int]:
        """
        Gets the altitudeInMeters property value. The altitude, in meters, that the printer is located at.
        Returns: Optional[int]
        """
        return self._altitude_in_meters
    
    @altitude_in_meters.setter
    def altitude_in_meters(self,value: Optional[int] = None) -> None:
        """
        Sets the altitudeInMeters property value. The altitude, in meters, that the printer is located at.
        Args:
            value: Value to set for the altitudeInMeters property.
        """
        self._altitude_in_meters = value
    
    @property
    def building(self,) -> Optional[str]:
        """
        Gets the building property value. The building that the printer is located in.
        Returns: Optional[str]
        """
        return self._building
    
    @building.setter
    def building(self,value: Optional[str] = None) -> None:
        """
        Sets the building property value. The building that the printer is located in.
        Args:
            value: Value to set for the building property.
        """
        self._building = value
    
    @property
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. The city that the printer is located in.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city that the printer is located in.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printerLocation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The altitude, in meters, that the printer is located at.
        self._altitude_in_meters: Optional[int] = None
        # The building that the printer is located in.
        self._building: Optional[str] = None
        # The city that the printer is located in.
        self._city: Optional[str] = None
        # The country or region that the printer is located in.
        self._country_or_region: Optional[str] = None
        # The floor that the printer is located on. Only numerical values are supported right now.
        self._floor: Optional[str] = None
        # The description of the floor that the printer is located on.
        self._floor_description: Optional[str] = None
        # The latitude that the printer is located at.
        self._latitude: Optional[float] = None
        # The longitude that the printer is located at.
        self._longitude: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The organizational hierarchy that the printer belongs to. The elements should be in hierarchical order.
        self._organization: Optional[List[str]] = None
        # The postal code that the printer is located in.
        self._postal_code: Optional[str] = None
        # The description of the room that the printer is located in.
        self._room_description: Optional[str] = None
        # The room that the printer is located in. Only numerical values are supported right now.
        self._room_name: Optional[str] = None
        # The site that the printer is located in.
        self._site: Optional[str] = None
        # The state or province that the printer is located in.
        self._state_or_province: Optional[str] = None
        # The street address where the printer is located.
        self._street_address: Optional[str] = None
        # The subdivision that the printer is located in. The elements should be in hierarchical order.
        self._subdivision: Optional[List[str]] = None
        # The subunit property
        self._subunit: Optional[List[str]] = None
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. The country or region that the printer is located in.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. The country or region that the printer is located in.
        Args:
            value: Value to set for the countryOrRegion property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterLocation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterLocation()
    
    @property
    def floor(self,) -> Optional[str]:
        """
        Gets the floor property value. The floor that the printer is located on. Only numerical values are supported right now.
        Returns: Optional[str]
        """
        return self._floor
    
    @floor.setter
    def floor(self,value: Optional[str] = None) -> None:
        """
        Sets the floor property value. The floor that the printer is located on. Only numerical values are supported right now.
        Args:
            value: Value to set for the floor property.
        """
        self._floor = value
    
    @property
    def floor_description(self,) -> Optional[str]:
        """
        Gets the floorDescription property value. The description of the floor that the printer is located on.
        Returns: Optional[str]
        """
        return self._floor_description
    
    @floor_description.setter
    def floor_description(self,value: Optional[str] = None) -> None:
        """
        Sets the floorDescription property value. The description of the floor that the printer is located on.
        Args:
            value: Value to set for the floorDescription property.
        """
        self._floor_description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "altitude_in_meters": lambda n : setattr(self, 'altitude_in_meters', n.get_int_value()),
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_or_region": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "floor": lambda n : setattr(self, 'floor', n.get_str_value()),
            "floor_description": lambda n : setattr(self, 'floor_description', n.get_str_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_collection_of_primitive_values(str)),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "room_description": lambda n : setattr(self, 'room_description', n.get_str_value()),
            "room_name": lambda n : setattr(self, 'room_name', n.get_str_value()),
            "site": lambda n : setattr(self, 'site', n.get_str_value()),
            "state_or_province": lambda n : setattr(self, 'state_or_province', n.get_str_value()),
            "street_address": lambda n : setattr(self, 'street_address', n.get_str_value()),
            "subdivision": lambda n : setattr(self, 'subdivision', n.get_collection_of_primitive_values(str)),
            "subunit": lambda n : setattr(self, 'subunit', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    @property
    def latitude(self,) -> Optional[float]:
        """
        Gets the latitude property value. The latitude that the printer is located at.
        Returns: Optional[float]
        """
        return self._latitude
    
    @latitude.setter
    def latitude(self,value: Optional[float] = None) -> None:
        """
        Sets the latitude property value. The latitude that the printer is located at.
        Args:
            value: Value to set for the latitude property.
        """
        self._latitude = value
    
    @property
    def longitude(self,) -> Optional[float]:
        """
        Gets the longitude property value. The longitude that the printer is located at.
        Returns: Optional[float]
        """
        return self._longitude
    
    @longitude.setter
    def longitude(self,value: Optional[float] = None) -> None:
        """
        Sets the longitude property value. The longitude that the printer is located at.
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
    
    @property
    def organization(self,) -> Optional[List[str]]:
        """
        Gets the organization property value. The organizational hierarchy that the printer belongs to. The elements should be in hierarchical order.
        Returns: Optional[List[str]]
        """
        return self._organization
    
    @organization.setter
    def organization(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the organization property value. The organizational hierarchy that the printer belongs to. The elements should be in hierarchical order.
        Args:
            value: Value to set for the organization property.
        """
        self._organization = value
    
    @property
    def postal_code(self,) -> Optional[str]:
        """
        Gets the postalCode property value. The postal code that the printer is located in.
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. The postal code that the printer is located in.
        Args:
            value: Value to set for the postalCode property.
        """
        self._postal_code = value
    
    @property
    def room_description(self,) -> Optional[str]:
        """
        Gets the roomDescription property value. The description of the room that the printer is located in.
        Returns: Optional[str]
        """
        return self._room_description
    
    @room_description.setter
    def room_description(self,value: Optional[str] = None) -> None:
        """
        Sets the roomDescription property value. The description of the room that the printer is located in.
        Args:
            value: Value to set for the roomDescription property.
        """
        self._room_description = value
    
    @property
    def room_name(self,) -> Optional[str]:
        """
        Gets the roomName property value. The room that the printer is located in. Only numerical values are supported right now.
        Returns: Optional[str]
        """
        return self._room_name
    
    @room_name.setter
    def room_name(self,value: Optional[str] = None) -> None:
        """
        Sets the roomName property value. The room that the printer is located in. Only numerical values are supported right now.
        Args:
            value: Value to set for the roomName property.
        """
        self._room_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("altitudeInMeters", self.altitude_in_meters)
        writer.write_str_value("building", self.building)
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryOrRegion", self.country_or_region)
        writer.write_str_value("floor", self.floor)
        writer.write_str_value("floorDescription", self.floor_description)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("organization", self.organization)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("roomDescription", self.room_description)
        writer.write_str_value("roomName", self.room_name)
        writer.write_str_value("site", self.site)
        writer.write_str_value("stateOrProvince", self.state_or_province)
        writer.write_str_value("streetAddress", self.street_address)
        writer.write_collection_of_primitive_values("subdivision", self.subdivision)
        writer.write_collection_of_primitive_values("subunit", self.subunit)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def site(self,) -> Optional[str]:
        """
        Gets the site property value. The site that the printer is located in.
        Returns: Optional[str]
        """
        return self._site
    
    @site.setter
    def site(self,value: Optional[str] = None) -> None:
        """
        Sets the site property value. The site that the printer is located in.
        Args:
            value: Value to set for the site property.
        """
        self._site = value
    
    @property
    def state_or_province(self,) -> Optional[str]:
        """
        Gets the stateOrProvince property value. The state or province that the printer is located in.
        Returns: Optional[str]
        """
        return self._state_or_province
    
    @state_or_province.setter
    def state_or_province(self,value: Optional[str] = None) -> None:
        """
        Sets the stateOrProvince property value. The state or province that the printer is located in.
        Args:
            value: Value to set for the stateOrProvince property.
        """
        self._state_or_province = value
    
    @property
    def street_address(self,) -> Optional[str]:
        """
        Gets the streetAddress property value. The street address where the printer is located.
        Returns: Optional[str]
        """
        return self._street_address
    
    @street_address.setter
    def street_address(self,value: Optional[str] = None) -> None:
        """
        Sets the streetAddress property value. The street address where the printer is located.
        Args:
            value: Value to set for the streetAddress property.
        """
        self._street_address = value
    
    @property
    def subdivision(self,) -> Optional[List[str]]:
        """
        Gets the subdivision property value. The subdivision that the printer is located in. The elements should be in hierarchical order.
        Returns: Optional[List[str]]
        """
        return self._subdivision
    
    @subdivision.setter
    def subdivision(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the subdivision property value. The subdivision that the printer is located in. The elements should be in hierarchical order.
        Args:
            value: Value to set for the subdivision property.
        """
        self._subdivision = value
    
    @property
    def subunit(self,) -> Optional[List[str]]:
        """
        Gets the subunit property value. The subunit property
        Returns: Optional[List[str]]
        """
        return self._subunit
    
    @subunit.setter
    def subunit(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the subunit property value. The subunit property
        Args:
            value: Value to set for the subunit property.
        """
        self._subunit = value
    

