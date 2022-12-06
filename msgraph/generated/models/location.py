from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

location_type = lazy_import('msgraph.generated.models.location_type')
location_unique_id_type = lazy_import('msgraph.generated.models.location_unique_id_type')
outlook_geo_coordinates = lazy_import('msgraph.generated.models.outlook_geo_coordinates')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class Location(AdditionalDataHolder, Parsable):
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
    def address(self,) -> Optional[physical_address.PhysicalAddress]:
        """
        Gets the address property value. The street address of the location.
        Returns: Optional[physical_address.PhysicalAddress]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[physical_address.PhysicalAddress] = None) -> None:
        """
        Sets the address property value. The street address of the location.
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new location and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The street address of the location.
        self._address: Optional[physical_address.PhysicalAddress] = None
        # The geographic coordinates and elevation of the location.
        self._coordinates: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None
        # The name associated with the location.
        self._display_name: Optional[str] = None
        # Optional email address of the location.
        self._location_email_address: Optional[str] = None
        # The type of location. The possible values are: default, conferenceRoom, homeAddress, businessAddress,geoCoordinates, streetAddress, hotel, restaurant, localBusiness, postalAddress. Read-only.
        self._location_type: Optional[location_type.LocationType] = None
        # Optional URI representing the location.
        self._location_uri: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For internal use only.
        self._unique_id: Optional[str] = None
        # For internal use only.
        self._unique_id_type: Optional[location_unique_id_type.LocationUniqueIdType] = None
    
    @property
    def coordinates(self,) -> Optional[outlook_geo_coordinates.OutlookGeoCoordinates]:
        """
        Gets the coordinates property value. The geographic coordinates and elevation of the location.
        Returns: Optional[outlook_geo_coordinates.OutlookGeoCoordinates]
        """
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self,value: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None) -> None:
        """
        Sets the coordinates property value. The geographic coordinates and elevation of the location.
        Args:
            value: Value to set for the coordinates property.
        """
        self._coordinates = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Location:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Location
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Location()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name associated with the location.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name associated with the location.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "coordinates": lambda n : setattr(self, 'coordinates', n.get_object_value(outlook_geo_coordinates.OutlookGeoCoordinates)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "location_email_address": lambda n : setattr(self, 'location_email_address', n.get_str_value()),
            "location_type": lambda n : setattr(self, 'location_type', n.get_enum_value(location_type.LocationType)),
            "location_uri": lambda n : setattr(self, 'location_uri', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unique_id": lambda n : setattr(self, 'unique_id', n.get_str_value()),
            "unique_id_type": lambda n : setattr(self, 'unique_id_type', n.get_enum_value(location_unique_id_type.LocationUniqueIdType)),
        }
        return fields
    
    @property
    def location_email_address(self,) -> Optional[str]:
        """
        Gets the locationEmailAddress property value. Optional email address of the location.
        Returns: Optional[str]
        """
        return self._location_email_address
    
    @location_email_address.setter
    def location_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the locationEmailAddress property value. Optional email address of the location.
        Args:
            value: Value to set for the locationEmailAddress property.
        """
        self._location_email_address = value
    
    @property
    def location_type(self,) -> Optional[location_type.LocationType]:
        """
        Gets the locationType property value. The type of location. The possible values are: default, conferenceRoom, homeAddress, businessAddress,geoCoordinates, streetAddress, hotel, restaurant, localBusiness, postalAddress. Read-only.
        Returns: Optional[location_type.LocationType]
        """
        return self._location_type
    
    @location_type.setter
    def location_type(self,value: Optional[location_type.LocationType] = None) -> None:
        """
        Sets the locationType property value. The type of location. The possible values are: default, conferenceRoom, homeAddress, businessAddress,geoCoordinates, streetAddress, hotel, restaurant, localBusiness, postalAddress. Read-only.
        Args:
            value: Value to set for the locationType property.
        """
        self._location_type = value
    
    @property
    def location_uri(self,) -> Optional[str]:
        """
        Gets the locationUri property value. Optional URI representing the location.
        Returns: Optional[str]
        """
        return self._location_uri
    
    @location_uri.setter
    def location_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the locationUri property value. Optional URI representing the location.
        Args:
            value: Value to set for the locationUri property.
        """
        self._location_uri = value
    
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
        writer.write_object_value("address", self.address)
        writer.write_object_value("coordinates", self.coordinates)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("locationEmailAddress", self.location_email_address)
        writer.write_enum_value("locationType", self.location_type)
        writer.write_str_value("locationUri", self.location_uri)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_enum_value("uniqueIdType", self.unique_id_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def unique_id(self,) -> Optional[str]:
        """
        Gets the uniqueId property value. For internal use only.
        Returns: Optional[str]
        """
        return self._unique_id
    
    @unique_id.setter
    def unique_id(self,value: Optional[str] = None) -> None:
        """
        Sets the uniqueId property value. For internal use only.
        Args:
            value: Value to set for the uniqueId property.
        """
        self._unique_id = value
    
    @property
    def unique_id_type(self,) -> Optional[location_unique_id_type.LocationUniqueIdType]:
        """
        Gets the uniqueIdType property value. For internal use only.
        Returns: Optional[location_unique_id_type.LocationUniqueIdType]
        """
        return self._unique_id_type
    
    @unique_id_type.setter
    def unique_id_type(self,value: Optional[location_unique_id_type.LocationUniqueIdType] = None) -> None:
        """
        Sets the uniqueIdType property value. For internal use only.
        Args:
            value: Value to set for the uniqueIdType property.
        """
        self._unique_id_type = value
    

