from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
outlook_geo_coordinates = lazy_import('msgraph.generated.models.outlook_geo_coordinates')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class Place(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the address property value. The street address of the place.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the address property value. The street address of the place.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new place and sets the default values.
        """
        super().__init__()
        # The street address of the place.
        self._address: Optional[physical_address.PhysicalAddress] = None
        # The name associated with the place.
        self._display_name: Optional[str] = None
        # Specifies the place location in latitude, longitude and (optionally) altitude coordinates.
        self._geo_coordinates: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The phone number of the place.
        self._phone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Place:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Place
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Place()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name associated with the place.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name associated with the place.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def geo_coordinates(self,) -> Optional[outlook_geo_coordinates.OutlookGeoCoordinates]:
        """
        Gets the geoCoordinates property value. Specifies the place location in latitude, longitude and (optionally) altitude coordinates.
        Returns: Optional[outlook_geo_coordinates.OutlookGeoCoordinates]
        """
        return self._geo_coordinates
    
    @geo_coordinates.setter
    def geo_coordinates(self,value: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None) -> None:
        """
        Sets the geoCoordinates property value. Specifies the place location in latitude, longitude and (optionally) altitude coordinates.
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
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geo_coordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(outlook_geo_coordinates.OutlookGeoCoordinates)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def phone(self,) -> Optional[str]:
        """
        Gets the phone property value. The phone number of the place.
        Returns: Optional[str]
        """
        return self._phone
    
    @phone.setter
    def phone(self,value: Optional[str] = None) -> None:
        """
        Sets the phone property value. The phone number of the place.
        Args:
            value: Value to set for the phone property.
        """
        self._phone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("phone", self.phone)
    

