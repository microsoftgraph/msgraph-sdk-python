from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PhysicalOfficeAddress(AdditionalDataHolder, Parsable):
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
        Gets the city property value. The city.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. The city.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new physicalOfficeAddress and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The city.
        self._city: Optional[str] = None
        # The country or region. It's a free-format string value, for example, 'United States'.
        self._country_or_region: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Office location such as building and office number for an organizational contact.
        self._office_location: Optional[str] = None
        # The postal code.
        self._postal_code: Optional[str] = None
        # The state.
        self._state: Optional[str] = None
        # The street.
        self._street: Optional[str] = None
    
    @property
    def country_or_region(self,) -> Optional[str]:
        """
        Gets the countryOrRegion property value. The country or region. It's a free-format string value, for example, 'United States'.
        Returns: Optional[str]
        """
        return self._country_or_region
    
    @country_or_region.setter
    def country_or_region(self,value: Optional[str] = None) -> None:
        """
        Sets the countryOrRegion property value. The country or region. It's a free-format string value, for example, 'United States'.
        Args:
            value: Value to set for the countryOrRegion property.
        """
        self._country_or_region = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PhysicalOfficeAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PhysicalOfficeAddress
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PhysicalOfficeAddress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country_or_region": lambda n : setattr(self, 'country_or_region', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "office_location": lambda n : setattr(self, 'office_location', n.get_str_value()),
            "postal_code": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
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
    
    @property
    def office_location(self,) -> Optional[str]:
        """
        Gets the officeLocation property value. Office location such as building and office number for an organizational contact.
        Returns: Optional[str]
        """
        return self._office_location
    
    @office_location.setter
    def office_location(self,value: Optional[str] = None) -> None:
        """
        Sets the officeLocation property value. Office location such as building and office number for an organizational contact.
        Args:
            value: Value to set for the officeLocation property.
        """
        self._office_location = value
    
    @property
    def postal_code(self,) -> Optional[str]:
        """
        Gets the postalCode property value. The postal code.
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. The postal code.
        Args:
            value: Value to set for the postalCode property.
        """
        self._postal_code = value
    
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("officeLocation", self.office_location)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def street(self,) -> Optional[str]:
        """
        Gets the street property value. The street.
        Returns: Optional[str]
        """
        return self._street
    
    @street.setter
    def street(self,value: Optional[str] = None) -> None:
        """
        Sets the street property value. The street.
        Args:
            value: Value to set for the street property.
        """
        self._street = value
    

